import { useEffect, useRef, useState } from 'react';
import * as Notifications from 'expo-notifications';
import * as Device from 'expo-device';
import { Platform } from 'react-native';
import { registerPushToken } from '../api/push';

Notifications.setNotificationHandler({
  handleNotification: async () => ({
    shouldShowAlert: true,
    shouldPlaySound: true,
    shouldSetBadge: true,
    shouldShowBanner: true,
    shouldShowList: true,
  }),
});

/**
 * Push notification hook:
 * - Requests permission on mount
 * - Registers Expo push token with backend
 * - Listens for incoming notifications and notification responses
 */
export function usePushNotifications() {
  const [expoPushToken, setExpoPushToken] = useState<string | null>(null);
  const [permissionGranted, setPermissionGranted] = useState(false);
  const notificationListener = useRef<Notifications.Subscription | null>(null);
  const responseListener = useRef<Notifications.Subscription | null>(null);

  useEffect(() => {
    if (!Device.isDevice) return; // simulators don't support push

    (async () => {
      const { status: existingStatus } = await Notifications.getPermissionsAsync();
      let finalStatus = existingStatus;

      if (existingStatus !== 'granted') {
        const { status } = await Notifications.requestPermissionsAsync();
        finalStatus = status;
      }

      if (finalStatus !== 'granted') {
        setPermissionGranted(false);
        return;
      }

      setPermissionGranted(true);

      try {
        const token = (
          await Notifications.getExpoPushTokenAsync({
            projectId: process.env.EXPO_PUBLIC_EAS_PROJECT_ID,
          })
        ).data;
        setExpoPushToken(token);

        // Register with backend
        await registerPushToken(token);
      } catch (e) {
        console.warn('Failed to get/register push token:', e);
      }
    })();

    // Listen for incoming notifications while app is foregrounded
    notificationListener.current = Notifications.addNotificationReceivedListener((notification) => {
      console.log('Notification received:', notification);
    });

    // Listen for notification response (user taps notification)
    responseListener.current = Notifications.addNotificationResponseReceivedListener((response) => {
      console.log('Notification tapped:', response);
      // Can navigate based on response.notification.request.content.data
    });

    return () => {
      if (notificationListener.current) {
        notificationListener.current.remove();
      }
      if (responseListener.current) {
        responseListener.current.remove();
      }
    };
  }, []);

  return { expoPushToken, permissionGranted };
}
