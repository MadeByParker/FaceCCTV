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

// add our event listener for the click
btn.addEventListener("click", () => {
	sidebar.classList.toggle("-translate-x-full");
  });
  
  // close sidebar if user clicks outside of the sidebar
  document.addEventListener("click", (event) => {
	const isButtonClick = btn === event.target && btn.contains(event.target);
	const isOutsideClick =
	  sidebar !== event.target && !sidebar.contains(event.target);
  
	// bail out if sidebar isnt open
	if (sidebar.classList.contains("-translate-x-full")) return;
  
	// if the user clicks the button, then toggle the class
	if (isButtonClick) {
	  console.log("does not contain");
	  sidebar.classList.toggle("-translate-x-full");
	  return;
	}
  
	// check to see if user clicks outside the sidebar
	if (!isButtonClick && isOutsideClick) {
	  console.log("outside click");
	  sidebar.classList.add("-translate-x-full");
	  return;
	}
  });