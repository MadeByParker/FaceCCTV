const localPort = 5000;
const { autoUpdater } = require('electron');
const electron = require('electron')
const { app, BrowserWindow, screen, ipcMain } = electron;

const express = require("express");
const localExpress = express();
localExpress.listen(localPort, "localhost");
const path = require('path')

require('electron-reload')(__dirname);

app.requestSingleInstanceLock();
app.name = "FaceCCTV";

process.env["ELECTRON_DISABLE_SECURITY_WARNINGS"] = "true";

app.on("ready", function() {
	const debugMode = false;


	if(debugMode) {
		windowWidth += 220;
	}

    const localWindow = new BrowserWindow({
            icon: path.join(__dirname, "/assets/img/logos/logo.ico"),
		width: 1920,
		height: 1080,
		resizable: true,
		frame: true,
		transparent: false,
            autoHideMenuBar: true,
		x: 0,
		y: 0,
            title: "FaceCCTV",
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
