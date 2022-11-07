const localPort = 5000;
const electron = require('electron')
const { app, BrowserWindow, screen, ipcMain, nativeTheme } = electron;
const path = require('path')

app.requestSingleInstanceLock();
app.name = "FaceCCTV";

const createWindow = () => {
	const win = new BrowserWindow({
	  width: 800,
	  height: 600,
	  webPreferences: {
		preload: path.join(__dirname, 'preload.js'),
	  },
	})
  
	ipcMain.handle('ping', () => 'pong')
	win.loadFile('index.html')

	ipcMain.handle('dark-mode:toggle', () => {
		if (nativeTheme.shouldUseDarkColors) {
		  nativeTheme.themeSource = 'light'
		} else {
		  nativeTheme.themeSource = 'dark'
		}
		return nativeTheme.shouldUseDarkColors
	  })
	
	  ipcMain.handle('dark-mode:system', () => {
		nativeTheme.themeSource = 'system'
	  })
  }
  
  app.whenReady().then(() => {
	createWindow();
  
	app.on('activate', () => {
	  if (BrowserWindow.getAllWindows().length === 0) {
		createWindow();
	  }
	});
  });
  
  app.on('window-all-closed', () => {
	if (process.platform !== 'darwin') {
	  app.quit();
	}
  });

/*app.on("ready", function() {
	const debugMode = false;

	const { width, height } = screen.getPrimaryDisplay().workAreaSize;

	let windowWidth = 1000;
	let windowHeight = 720;

	if(width > 1200 && height > 800) {
		windowWidth = 1160;
		windowHeight = 750;
	}

	if(debugMode) {
		windowWidth += 220;
	}

    const localWindow = new BrowserWindow({
		width: windowWidth,
		minWidth: 800,
		height: windowHeight,
		minHeight: 600,
		resizable: true,
		frame: false,
		transparent: false,
		x: 80,
		y: 80,
		webPreferences: {
            preload: path.join(__dirname, 'preload.js'),
			nodeIntegration: true,
			contextIsolation: false
		}
	});

    app.on('activate', () => {
        if (BrowserWindow.getAllWindows().length === 0) {
          createWindow();
        }
      });
    
    app.on('window-all-closed', () => {
      if (process.platform !== 'darwin') {
        app.quit();
      }
    });

    // macOS apps behave differently than Windows when it comes to closing an application.
	if(process.platform === "darwin") {
		let quit = true;

		localShortcut.register(localWindow, "Command+Q", () => {
			quit = true;
			app.quit();
		});
	
		localShortcut.register(localWindow, "Command+W", () => {
			quit = false;
			app.hide();
		});

		localWindow.on("close", (event) => {
			if(!quit) {
				event.preventDefault();
				quit = true;
			}
		});
    };
});
*/