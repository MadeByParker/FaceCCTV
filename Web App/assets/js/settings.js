// Add events to the navbar elements.
addNavbarEvents();

// Add events to the elements of the "Settings" page's navbar.
addSettingsNavbarEvents();

let divSettingsNavbar = document.getElementById("settings-navbar");
let divPageSettings = document.getElementById("settings-page");
let divSettingsDonate = document.getElementById("settings-section-donate");

let buttonsDonate = divSettingsDonate.getElementsByClassName("action-button");

let settingsToggleTheme = document.getElementById("settings-toggle-theme");
let settingsToggleSounds = document.getElementById("settings-toggle-sounds");



// User settings between the web and desktop app are normally synced, but this can be disabled.
let settingsDataSync = "enabled";

let applicationSettings = {};
let applicationChoices = {};


let divPageActivity = document.getElementById("activity-page");
let divActivityList = document.getElementById("activity-list");


// When the app first loads, the user's settings are fetched and set.
(async () => {
	applicationSettings = await getSettings();
	applicationChoices = await getSettingsChoices();

	await setTheme(applicationSettings.theme);
	await setSounds(applicationSettings.sounds);
	setSettingsChoices(applicationChoices);
})();

// Used to keep track of the last 5 elements the user has clicked on. This is only used to enable/disable the desktop app mode for debugging.
let clickTargets = [];

// Set the background image of the app.
function setBackground(theme, alternate) {
	if(alternate) {
		document.documentElement.classList.add("alternate-background");
		divBackground.style.backgroundImage = `url("./assets/img/BG-Alt.jpg")`;
	} else {
		document.documentElement.classList.remove("alternate-background");
		divBackground.style.backgroundImage = theme === "light" ? `url("./assets/img/BG-White.png")` : `url("./assets/img/BG-Black.png")`;
	}
}

// Clear the "active" status of all settings pages.
function clearActiveSettingsPage() {
	let pages = divPageSettings.getElementsByClassName("settings-page");
	for(let i = 0; i < pages.length; i++) {
		pages[i].classList.add("hidden");
	}
}

// Add events to the "Settings" page's choice buttons.
function addSettingsChoiceEvents() {
	let buttons = divPageSettings.getElementsByClassName("choice-button");
	for(let i = 0; i < buttons.length; i++) {
		let button = buttons[i];

		button.addEventListener("click", async () => {
			let key = button.parentElement.parentElement.getAttribute("data-key");
			let value = button.getAttribute("data-value");
			await setChoice(key, value);
			let choices = await getSettingsChoices();
			setSettingsChoices(choices);
			syncSettings(true);
		});
	}
}

// Set the value of a settings choice.
async function setChoice(key, value) {
	return new Promise(async (resolve, reject) => {
		try {
			let choicesJSON = await appStorage.getItem("choices");
			let choices = defaultChoices;

			if(!empty(choicesJSON) && validJSON(choicesJSON)) {
				let parsed = JSON.parse(choicesJSON);

				Object.keys(parsed).map(choice => {
					choices[choice] = parsed[choice];
				});
			}
			
			choices[key] = value;

			await appStorage.setItem("choices", JSON.stringify(choices));

			resolve();
		} catch(error) {
			console.log(error);
			errorNotification("Couldn't update choice...");
			reject(error);
		}
	});
}

// Fetch and return user settings.
async function fetchSettings() {
	let userID = await appStorage.getItem("userID");
	let token = await appStorage.getItem("token");
	let key = await appStorage.getItem("key");

	return new Promise(async (resolve, reject) => {
		if(settingsDataSync === "disabled") {
			let currentSettings = await getSettings();
			let currentChoices = await getSettingsChoices();
			let settings = JSON.stringify({ ...currentSettings, choices:JSON.stringify(currentChoices) });
			resolve(settings);
			return;
		}

		readSetting(token, userID).then(result => {
			if(!("errors" in result)) {
				let current = CryptoFN.decryptAES(result.data.readSetting.userSettings, key);
				resolve(current);
			} else {
				errorNotification(result.errors[0]);
			}
		}).catch(error => {
			reject(error);
		});
	});
}

// Return user settings.
async function getSettings() {
	return new Promise(async (resolve, reject) => {
		try {
			let settings = {};

			let theme = await appStorage.getItem("theme");
			let sounds = await appStorage.getItem("sounds");

			settings["theme"] = empty(theme) ? defaultSettings.theme : theme;
			settings["sounds"] = empty(sounds) ? defaultSettings.sounds : sounds;

			resolve(settings);
		} catch(error) {
			console.log(error);
			resolve(defaultSettings);
		}
	});
}

// Return settings choices.
async function getSettingsChoices() {
	return new Promise(async (resolve, reject) => {
		try {
			let choicesJSON = await appStorage.getItem("choices");

			if(empty(choicesJSON) || !validJSON(choicesJSON)) {
				resolve(defaultChoices);
			} else {
				resolve(JSON.parse(choicesJSON));
			}
		} catch(error) {
			console.log(error);
			resolve(defaultChoices);
		}
	});
}

// Set settings choices.
function setSettingsChoices(choices) {
	let sections = divPageSettings.getElementsByClassName("settings-section");

	for(let i = 0; i < sections.length; i++) {
		let section = sections[i];
		let key = section.getAttribute("data-key");
		let buttons = section.getElementsByClassName("choice-button");

		for(let j = 0; j < buttons.length; j++) {
			let button = buttons[j];
			let value = button.getAttribute("data-value");
			
			button.classList.remove("active");

			if(value === choices[key]) {
				button.classList.add("active");
				processChoice(key, value);
			}
		}
	}
}

// Process choice change for some settings.
async function processChoice(key, value) {
	switch(key) {
		case "settingsSync":
			settingsDataSync = value;
			break;
		case "navbarStyle":
			if(value === "compact") {
				document.documentElement.classList.add("navbar-compact");
			} else {
				document.documentElement.classList.remove("navbar-compact");
			}
			
			break;
		case "alternateBackground":
			let settings = await getSettings();

			if(value === "disabled") {
				setBackground(settings.theme, false);
			} else {
				setBackground(settings.theme, true);
			}

			break;
	}
}

// Set user settings.
function setSettings(settings) {
	return new Promise(async (resolve, reject) => {
		try {
			if(empty(settings)) {
				settings = { ...defaultSettings, choices:JSON.stringify(defaultChoices) };
			}

			Object.keys(settings).map(async key => {
				let value = settings[key];
				await appStorage.setItem(key, value);
			});

			applicationSettings = await getSettings();
			applicationChoices = await getSettingsChoices();

			setTheme(applicationSettings.theme);
			setSounds(applicationSettings.sounds);

			setSettingsChoices(applicationChoices);

			resolve();
		} catch(error) {
			console.log(error);
			reject(error);
		}
	});
}

// Set settings page.
function setSettingsPage(page) {
	page = empty(page) ? defaultChoices.defaultSettingsPage : page.toLowerCase();

	clearActiveSettingsNavbarItem();
	clearActiveSettingsPage();

	document.getElementById(`settings-navbar-${page}`).classList.add("active");
	document.getElementById(`settings-page-${page}`).classList.remove("hidden");
}

// Reset user settings.
async function resetSettings() {
	try {
		let token = await appStorage.getItem("token");
		let userID = await appStorage.getItem("userID");

		showLoading(4000, "Resetting Settings...");
		
		await appStorage.removeItem("theme");
		await appStorage.removeItem("sounds");
		await appStorage.removeItem("choices");

		await updateSetting(token, userID, "");

		setTimeout(() => {
			window.location.reload();
		}, 3500);
	} catch(error) {
		console.log(error);
		errorNotification("Something went wrong... - EW58");
		
		setTimeout(() => {
			window.location.reload();
		}, 3500);
	}
}

// Update user settings.
function syncSettings(update) {
	return new Promise(async (resolve, reject) => {
		try {
			if(settingsDataSync === "disabled") {
				update = false;
			}

			let token = await appStorage.getItem("token");
			let userID = await appStorage.getItem("userID");
			let key = await appStorage.getItem("key");

			let currentSettings = await getSettings();
			let currentChoices = await getSettingsChoices();

			if(settingsDataSync !== "disabled") {
				currentChoices.settingsSync = "enabled";
			}

			let settings = { ...currentSettings, choices:JSON.stringify(currentChoices) };

			let current = await fetchSettings();

			if(validJSON(current)) {
				current = JSON.parse(current);

				Object.keys(current).map(settingKey => {
					if(settingKey in settings) {
						current[settingKey] = settings[settingKey];
					}
				});
			} else {
				current = settings;
			}

			await setSettings(current);

			if(update) {
				console.log("Updating Settings...");

				let choices = JSON.parse(current.choices);
				delete choices.settingsSync;
				current.choices = JSON.stringify(choices);

				let encrypted = CryptoFN.encryptAES(JSON.stringify(current), key);

				updateSetting(token, userID, encrypted).then(result => {
					if(!("data" in result) && !("updateSetting" in result.data) && result.data.updateSetting !== "Done") {
						errorNotification("Couldn't update / sync setting.");
						console.log(result);
						reject(error);
						return;
					}

					resolve();
				}).catch(error => {
					errorNotification(error);
					console.log(error);
					reject(error);
				});
			} else {
				resolve();
			}
		} catch(error) {
			errorNotification("Couldn't update settings.");
			console.log(error);
			reject(error);
		}
	});
}