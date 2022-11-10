function showLoading(limit, text = "") {
	hideLoading();

	let element = document.createElement("div");
	element.classList.add("loading-screen");
	element.innerHTML = '<div class="loading-icon"><div></div><div></div></div><span id="loading-text">' + text + '</span>';
	document.body.appendChild(element);

	setTimeout(() => {
		element.remove();
	}, limit);
}

function hideLoading() {
	for(let i = 0; i < document.getElementsByClassName("loading-screen").length; i++) {
		document.getElementsByClassName("loading-screen")[i].remove();
	}
}

let applicationSettings = {};
let applicationChoices = {};

// When the app first loads, the user's settings are fetched and set.
(async () => {
	applicationSettings = await getSettings();
	applicationChoices = await getSettingsChoices();

	await setTheme(applicationSettings.theme);
	await setSounds(applicationSettings.sounds);
	setSettingsChoices(applicationChoices);
})();

 
// Close window (desktop app only).
buttonWindowClose.addEventListener("click", () => {
	if(!empty(ipcRenderer)) {
		ipcRenderer.send("set-window-state", "closed");
	}
});

// Minimize window (desktop app only).
buttonWindowMinimize.addEventListener("click", () => {
	if(!empty(ipcRenderer)) {
		ipcRenderer.send("set-window-state", "minimized");
	}
});

// Maximize window (desktop app only).
buttonWindowMaximize.addEventListener("click", () => {
	if(!empty(ipcRenderer)) {
		ipcRenderer.send("set-window-state", "maximized");
	}
});

// Used to enable "desktop" mode, and play sounds when buttons are clicked on.
document.addEventListener("click", (event) => {
	clickTargets.push(event.target.id);
	clickTargets = clickTargets.slice(-3);

	if(clickTargets.join("-") === "span-login-title-span-login-title-span-login-title") {
		clickTargets = [];
		appToggle();
	}

	let audible = audibleElement(event.target);
	if(applicationSettings.sounds === "enabled" && audioPlayable && audible.audible) {
		if(audible.type === "switch") {
			audioSwitch.currentTime = 0;
			audioSwitch.play();
		} else {
			audioPop.currentTime = 0;
			audioPop.play();
		}
	}
});

closeBtn.addEventListener("click", ()=>{
  sidebar.classList.toggle("open");
  menuBtnChange();//calling the function(optional)
});

searchBtn.addEventListener("click", ()=>{ // Sidebar open when you click on the search iocn
  sidebar.classList.toggle("open");
  menuBtnChange(); //calling the function(optional)
});

// following are the code to change sidebar button(optional)
function menuBtnChange() {
 if(sidebar.classList.contains("open")){
   closeBtn.classList.replace("bx-menu", "bx-menu-alt-right");//replacing the iocns class
 }else {
   closeBtn.classList.replace("bx-menu-alt-right","bx-menu");//replacing the iocns class
 }
}