chrome.app.runtime.onLaunched.addListener(function (launchData) {
    chrome.app.window.create('app/index.html', {
        id: "Ticker",
        bounds: {
            width: 500,
            height: 600
        },
        minWidth: 500,
        minHeight: 600
    });
});