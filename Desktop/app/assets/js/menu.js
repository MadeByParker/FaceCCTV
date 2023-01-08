function closeApplication(){
      ipcRenderer.send('close-btn', true);
}

function minimizeApplication(){
      ipcRenderer.send('minimize-btn', true);
}