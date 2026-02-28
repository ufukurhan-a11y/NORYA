import React from 'react';
import { StatusBar } from 'expo-status-bar';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { AuthProvider } from './src/context/AuthContext';
import HomeScreen from './src/screens/HomeScreen';
import LoginScreen from './src/screens/LoginScreen';
import RegisterScreen from './src/screens/RegisterScreen';
import AnalyzeScreen from './src/screens/AnalyzeScreen';
import ReportScreen from './src/screens/ReportScreen';
import HistoryScreen from './src/screens/HistoryScreen';
import { colors } from './src/theme/colors';

export type RootStackParamList = {
  Home: undefined;
  Login: undefined;
  Register: undefined;
  Analyze: undefined;
  Report: { result: string };
  History: undefined;
};

const Stack = createNativeStackNavigator<RootStackParamList>();

export default function App() {
  return (
    <AuthProvider>
      <NavigationContainer>
        <StatusBar style="light" />
        <Stack.Navigator
          screenOptions={{
            headerShown: false,
            contentStyle: { backgroundColor: colors.navy[900] },
            animation: 'slide_from_right',
          }}
        >
          <Stack.Screen name="Home">
            {({ navigation }) => (
              <HomeScreen
                onAnalyze={() => navigation.navigate('Analyze')}
                onHistory={() => navigation.navigate('History')}
                onLogin={() => navigation.navigate('Login')}
                onRegister={() => navigation.navigate('Register')}
              />
            )}
          </Stack.Screen>
          <Stack.Screen name="Login">
            {({ navigation }) => (
              <LoginScreen onRegister={() => navigation.replace('Register')} />
            )}
          </Stack.Screen>
          <Stack.Screen name="Register">
            {({ navigation }) => (
              <RegisterScreen onBack={() => navigation.goBack()} />
            )}
          </Stack.Screen>
          <Stack.Screen name="Analyze">
            {({ navigation }) => (
              <AnalyzeScreen
                onResult={(result) => navigation.navigate('Report', { result })}
              />
            )}
          </Stack.Screen>
          <Stack.Screen name="Report">
            {({ navigation, route }) => (
              <ReportScreen
                result={route.params.result}
                onBack={() => navigation.goBack()}
              />
            )}
          </Stack.Screen>
          <Stack.Screen name="History">
            {({ navigation }) => (
              <HistoryScreen
                onOpenReport={(text) => navigation.navigate('Report', { result: text })}
                onBack={() => navigation.goBack()}
              />
            )}
          </Stack.Screen>
        </Stack.Navigator>
      </NavigationContainer>
    </AuthProvider>
  );
}
