importScripts("https://js.pusher.com/beams/service-worker.js");

importScripts('https://storage.googleapis.com/workbox-cdn/releases/6.5.4/workbox-sw.js');

if (workbox) {
  workbox.routing.registerRoute(
    () => true, 
    new workbox.strategies.NetworkFirst({
      cacheName: 'user-data',
      plugins: [
        new workbox.expiration.ExpirationPlugin({
          maxEntries: Infinity,
        }),
      ],
    })
  );
} else {
  console.log('Workbox could not be loaded.');
}

// const CACHE_NAME = 'ayah-cache-v1';

// self.addEventListener('install', (event) => {
//   console.log('[SW] Installing...');
//   self.skipWaiting();
// });

// self.addEventListener('activate', (event) => {
//   console.log('[SW] Activating...');
//   event.waitUntil(
//     caches.keys().then((cacheNames) =>
//       Promise.all(
//         cacheNames
//           .filter((name) => name !== CACHE_NAME)
//           .map((name) => caches.delete(name))
//       )
//     )
//   );
//   self.clients.claim();
// });

// self.addEventListener('fetch', (event) => {
//   if (event.request.method !== 'GET') return;

//   event.respondWith(
//     caches.match(event.request).then((cachedResponse) => {
//       if (cachedResponse) return cachedResponse;

//       return fetch(event.request)
//         .then((response) => {
//           if (!response || response.status !== 200) return response;

//           const responseClone = response.clone();
//           caches.open(CACHE_NAME).then((cache) => {
//             cache.put(event.request, responseClone);
//           });

//           return response;
//         })
//         .catch((err) => {
//           console.warn('[SW] Fetch failed, offline?', err);
//         });
//     })
//   );
// });