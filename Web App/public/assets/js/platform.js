// The app's platform ("web" or "app") depends on the ID of the document element.
const appPlatform = document.documentElement.id;

// In order to have the same codebase across the web and desktop app, there are a few empty variables that are only given a value when the app platform is set to "app".
let electron = null;
let ipcRenderer = null;

if(appPlatform !== "app" && typeof require === "undefined") {
	var require = () => { 
		return "";
	};
}

if(appPlatform === "app") {
	var sha256 = require("sha256");
	window.$ = window.jQuery = require("jquery");
	electron = require("electron");
	ipcRenderer = electron.ipcRenderer;
}
