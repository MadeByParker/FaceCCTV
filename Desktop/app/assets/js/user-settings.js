// Toggle app theme.
settingsToggleTheme.addEventListener("click", async () => {
	if(settingsToggleTheme.classList.contains("active")) {
		await setTheme("dark");
	} else {
		await setTheme("light");
	}

	syncSettings(true);
});

// Reset user settings.
buttonSettingsReset.addEventListener("click", () => {
	let popup = new Popup(300, "auto", "Reset Settings", `<span>Are you sure you want to reset your settings?</span>`, { page:"settings" });
	popup.show();

	popup.on("confirm", () => {
		popup.hide();
		resetSettings();
	});
});

// Set the theme of the app.
function setTheme(theme) {
	return new Promise(async (resolve, reject) => {
		try {
			applicationSettings.theme = theme;

			let themeToggles = document.getElementsByClassName("toggle-wrapper theme");
			let favicons = document.getElementsByClassName("favicon");
			let browserTheme = document.getElementsByClassName("browser-theme")[0];
			
			let choices = await getSettingsChoices();
			let alternate = choices?.alternateBackground === "disabled" ? false : true;

			if(theme === "light") {
				browserTheme.setAttribute("content", "#ffffff");

				for(let i = 0; i < favicons.length; i++) {
					favicons[i].href = favicons[i].href.replace("dark", "light");
				}

				for(let i = 0; i < themeToggles.length; i++) {
					themeToggles[i].classList.add("active");
				}

				await appStorage.setItem("theme", "light");

				document.documentElement.classList.add("light");
				document.documentElement.classList.remove("dark");

				setBackground(applicationSettings.theme, alternate);
			} else {
				browserTheme.setAttribute("content", "#000000");

				for(let i = 0; i < favicons.length; i++) {
					favicons[i].href = favicons[i].href.replace("light", "dark");
				}

				for(let i = 0; i < themeToggles.length; i++) {
					themeToggles[i].classList.remove("active");
				}

				await appStorage.setItem("theme", "dark");

				document.documentElement.classList.remove("light");
				document.documentElement.classList.add("dark");

				setBackground(applicationSettings.theme, alternate);
			}

			resolve();
		} catch(error) {
			console.log(error);
			reject(error);
		}
	});
}

// Set the background image of the app.
function setBackground(theme, alternate) {
	if(alternate) {
		document.documentElement.classList.add("alternate-background");
		divBackground.style.backgroundImage = `url("./assets/img/rose-petals.png")`;
	} else {
		document.documentElement.classList.remove("alternate-background");
		divBackground.style.backgroundImage = theme === "light" ? `url("./assets/img/rose-petals.png")` : `url("./assets/img/rose-petals.png")`;
	}
}