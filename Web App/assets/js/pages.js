// Returns the currently active page.
function getActivePage() {

	let pages = divPageApp.getElementsByClassName("page");
	for(let i = 0; i < pages.length; i++) {
		if(!pages[i].classList.contains("hidden")) {
			return pages[i];
		}
	}
}

// Clear the "active" status of all navbar elements.
function clearActiveNavbarItem() {
	let items = divNavbar.getElementsByClassName("item");
	for(let i = 0; i < items.length; i++) {
		items[i].classList.remove("active");
	}
}

// Clear the "active" status of all app pages.
function clearActivePage() {
	let pages = divPageApp.getElementsByClassName("page");
	for(let i = 0; i < pages.length; i++) {
		pages[i].classList.add("hidden");
	}
}

// Set active app page.
function setPage(page) {
	page = empty(page) ? defaultChoices.defaultPage.toLowerCase() : page.toLowerCase().replace(" ", "");

	clearActiveNavbarItem();
	clearActivePage();

	document.getElementById(`navbar-${page}`).classList.add("active");
	document.getElementById(`navbar-${page}`).classList.add("animate");
	document.getElementById(`${page}-page`).classList.remove("hidden");

	setTimeout(() => {
		document.getElementById(`navbar-${page}`).classList.remove("animate");
	}, 1000);

	switch(page) {
		case "start":
			firstFetch.homePage = false;
			break;
		case "detection":
			firstFetch.detectionPage = false;
			break;
		case "enhancer":
			firstFetch.imageEnhancementPage = false;
			break;
		case "notifications":

			firstFetch.notifications = false;
			break;
		case "settings":
			syncSettings(false);
			adminCheck();
			firstFetch.settings = false;
			break;
	}
}