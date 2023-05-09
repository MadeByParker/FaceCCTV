// Retrieve saved settings from localStorage (if any)
const savedNavbarBackground = localStorage.getItem('navbarBackground');
const savedAppBackground = localStorage.getItem('appBackground');
const savedTextColor = localStorage.getItem('textColor');
const savedTextSize = localStorage.getItem('textSize');

// Set the selected options based on the saved settings (if available)
document.getElementById('settings-navbar').value = savedNavbarBackground || 'default';
document.getElementById('settings-background-color').value = savedAppBackground || 'default';
document.getElementById('settings-text-color').value = savedTextColor || 'white';
document.getElementById('settings-text-size').value = savedTextSize || 'base';

// Function to apply the selected settings to the page
function applySettings() {
    const navbarBackground = document.getElementById('settings-navbar').value;
    const appBackground = document.getElementById('settings-background-color').value;
    const textColor = document.getElementById('settings-text-color').value;
    const textSize = document.getElementById('settings-text-size').value;
  
    // Update navbar background
    const navbar = document.getElementsByTagName('nav');
    navbar.classList.remove('default', 'black-and-white', 'blue-and-pink', 'white', 'gray', 'black', 'dark-blue');
    navbar.classList.add(navbarBackground);
  
    // Update app background
    const app = document.body;
    const slider = document.querySelector('.image-slider');
    app.classList.remove('default', 'black-and-white', 'blue-and-pink', 'white', 'gray', 'black', 'dark-blue');
    if (appBackground !== 'default') {
        app.classList.add(appBackground);
        slider.classList.add('invisible');
    }
    else {
        slider.classList.remove('invisible');
        app.classList.add('default');
    }
  
    // Update text color
    const textElements = document.body.querySelectorAll('h1, h2, h3, h4, h5, h6, p, a, li, span');
    textElements.forEach((element) => {
      element.classList.remove('text-white', 'text-black', 'text-gray');
      element.classList.add(textColor);
    });
  
    // Update text size
    const textContainer = document.body;
    textContainer.style.fontSize = textSize + 'rem';
  }

// Function to handle changes in the settings
function handleSettingsChange() {
  const navbarBackground = document.getElementById('settings-navbar').value;
  const appBackground = document.getElementById('settings-background-color').value;
  const textColor = document.getElementById('settings-text-color').value;
  const textSize = document.getElementById('settings-text-size').value;

  // Save the settings to localStorage
  localStorage.setItem('navbarBackground', navbarBackground);
  localStorage.setItem('appBackground', appBackground);
  localStorage.setItem('textColor', textColor);
  localStorage.setItem('textSize', textSize);

  // Apply the selected settings to the page
  applySettings();
}

// Listen for changes in the settings and call the handleSettingsChange function
document.getElementById('settings-navbar').addEventListener('change', handleSettingsChange);
document.getElementById('settings-background-color').addEventListener('change', handleSettingsChange);
document.getElementById('settings-text-color').addEventListener('change', handleSettingsChange);
document.getElementById('settings-text-size').addEventListener('change', handleSettingsChange);
