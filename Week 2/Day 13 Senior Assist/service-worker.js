self.addEventListener("install", event => {
    event.waitUntil(
        caches.open("senior-assist").then(cache => {
            return cache.addAll([
                "./",
                "./index.html",
                "./style.css",
                "./script.js"
            ]);
        })
    );
});
