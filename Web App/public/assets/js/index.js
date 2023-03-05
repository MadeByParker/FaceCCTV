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
// Converts HTML tags to avoid them being rendered. Prevents XSS attacks.
function stripHTMLCharacters(string) {
	string = replaceAll(string, "<", "&lt;");
	string = replaceAll(string, ">", "&gt;");
	return string;
}

const mobile_icon = document.getElementById('mobile-icon');
const mobile_menu = document.getElementById('mobile-menu');
const hamburger_icon = document.querySelector("#bars svg");

function openCloseMenu() {
  mobile_menu.classList.toggle('block');
  mobile_menu.classList.toggle('active');
}

function changeIcon(icon) {
  icon.classList.toggle("fa-xmark");
}

mobile_icon.addEventListener('click', openCloseMenu);
