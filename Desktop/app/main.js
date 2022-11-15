const localPort = 5000;
const electron = require('electron')
const { app, BrowserWindow, screen, ipcMain } = electron;

const express = require("express");
const localExpress = express();
localExpress.listen(localPort, "localhost");
const path = require('path')

app.requestSingleInstanceLock();
app.name = "FaceCCTV";

process.env["ELECTRON_DISABLE_SECURITY_WARNINGS"] = "true";

/*const createWindow = () => {
	const win = new BrowserWindow({
	  width: 800,
	  height: 600,
	  webPreferences: {
		preload: path.join(__dirname, 'preload.js'),
	  },
	})
  
	ipcMain.handle('ping', () => 'pong')
	win.loadFile('index.html')
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
	if (process.platform !== 'darwin') app.quit()
  })*/

app.on("ready", function() {
	const debugMode = false;

	const { width, height } = screen.getPrimaryDisplay().workAreaSize;

	let windowWidth = 1250;
	let windowHeight = 800;

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
		resizable: true,
		transparent: false,
		x: 0,
		y: 0,
		webPreferences: {
			preload: path.join(app.getAppPath(), 'preload.js'),
			contextIsolation: false,
			nodeIntegration: true,
			nodeIntegrationInWorker: true
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

	localExpress.use("/assets", express.static(path.join(__dirname, "assets")));

	ipcMain.handle('ping', () => 'pong')
	localWindow.loadURL("http://127.0.0.1:" + localPort);
	localWindow.loadFile("./displays/index.html");
	if(debugMode) {
		localWindow.webContents.openDevTools();
	}

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
		}

		ipcMain.on("set-window-state", (error, req) => {
			let state = req.toString();
			switch(state) {
				case "closed":
					(process.platform === "darwin") ? app.hide() : app.quit();
					break;
				case "minimized":
					localWindow.minimize();
					break;
				case "maximized":
					if(process.platform === "darwin") {
						localWindow.isFullScreen() ? localWindow.setFullScreen(false) : localWindow.setFullScreen(true);
					}
					else {
						localWindow.isMaximized() ? localWindow.restore() : localWindow.maximize();
					}
					
					break;		
			}
		});
	
});
