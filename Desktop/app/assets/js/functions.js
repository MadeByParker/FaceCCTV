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

