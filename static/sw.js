/* Norya PWA Service Worker: cache shell + push notifications */
const CACHE_NAME = 'norya-v1';
const STATIC_CACHE = ['/', '/static/index.html', '/static/manifest.json', '/static/icon.svg', '/static/norya.svg', '/static/css/app.css'];

self.addEventListener('install', function (e) {
  e.waitUntil(
    caches.open(CACHE_NAME).then(function (cache) {
      return cache.addAll(STATIC_CACHE).catch(function () {});
    }).then(function () { return self.skipWaiting(); })
  );
});

self.addEventListener('activate', function (e) {
  e.waitUntil(
    caches.keys().then(function (keys) {
      return Promise.all(keys.filter(function (k) { return k !== CACHE_NAME; }).map(function (k) { return caches.delete(k); }));
    }).then(function () { return self.clients.claim(); })
  );
});

self.addEventListener('fetch', function (e) {
  var u = new URL(e.request.url);
  if (u.origin !== location.origin) return;
  if (u.pathname.startsWith('/api/') || u.pathname.startsWith('/auth/') || u.pathname.startsWith('/analyze')) {
    e.respondWith(fetch(e.request).catch(function () { return caches.match(e.request); }));
    return;
  }
  if (u.pathname === '/' || u.pathname === '/static/index.html' || u.pathname.startsWith('/static/')) {
    e.respondWith(
      fetch(e.request).then(function (r) {
        if (r && r.status === 200 && r.type === 'basic') {
          var clone = r.clone();
          caches.open(CACHE_NAME).then(function (cache) { cache.put(e.request, clone); });
        }
        return r;
      }).catch(function () { return caches.match(e.request).then(function (c) { return c || caches.match('/static/index.html'); }); })
    );
    return;
  }
});

self.addEventListener('push', function (e) {
  var data = {};
  try {
    data = e.data ? e.data.json() : {};
  } catch (_) {}
  var title = data.title || 'Norya';
  var options = {
    body: data.body || 'Raporunuz hazır.',
    icon: '/static/icon.svg',
    badge: '/static/icon.svg',
    tag: data.tag || 'norya-notification',
    data: data.url ? { url: data.url } : {},
    requireInteraction: !!data.requireInteraction,
    vibrate: [200, 100, 200]
  };
  e.waitUntil(self.registration.showNotification(title, options));
});

self.addEventListener('notificationclick', function (e) {
  e.notification.close();
  var url = e.notification.data && e.notification.data.url ? e.notification.data.url : '/';
  e.waitUntil(
    self.clients.matchAll({ type: 'window', includeUncontrolled: true }).then(function (clientList) {
      for (var i = 0; i < clientList.length; i++) {
        if (clientList[i].url.indexOf(self.location.origin) === 0 && 'focus' in clientList[i]) {
          clientList[i].navigate(url);
          return clientList[i].focus();
        }
      }
      if (self.clients.openWindow) return self.clients.openWindow(url);
    })
  );
});
