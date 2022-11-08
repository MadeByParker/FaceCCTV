// The app's platform ("web" or "app") depends on the ID of the document element.
const appPlatform = document.documentElement.id;

// In order to have the same codebase across the web and desktop app, there are a few empty variables that are only given a value when the app platform is set to "app".
let electron = null;
let ipcRenderer = null;