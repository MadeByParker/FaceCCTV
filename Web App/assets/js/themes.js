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