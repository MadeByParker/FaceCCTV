async function previewImage() {
    const form = document.getElementById('my-form');
    const formData = new FormData(form);
    const response = await fetch('http://127.0.0.1:8000/task/face-detection', {
        method: 'POST',
        body: formData,
    });
    const data = await response.json();
    const img = new Image();
    img.src = 'data:image/jpeg;base64,' + data.img_data;
        // Open a new window with the image
    const preview = document.getElementById('preview');
    preview.appendChild(img);
    const win = window.open("");
    win.document.write("<img src='" + img.src + "'/>");
}

previewImage();
