// Converts HTML tags to avoid them being rendered. Prevents XSS attacks.
function stripHTMLCharacters(string) {
	string = replaceAll(string, "<", "&lt;");
	string = replaceAll(string, ">", "&gt;");
	return string;
}

(function() {
	const dropzone = document.getElementById("dropzone");
	const uploads = document.getElementById("uploads");
	var fileInput = document.getElementById("drag-drop");
	var text, i, dropped = false;

	var generateNames = function(files) {
		for (i = 0; i < files.length; i++) {
			if (
				files[i].type === "image/jpeg" ||
				files[i].type === "image/png" ||
				files[i].type === "image/gif"
			) {
				text = document.createTextNode(files[i].name + " | ");
				uploads.appendChild(text);
			} else {
				text = document.createTextNode("Error! One or more files is not an image.");
				uploads.appendChild(text);
			}
		}
	};
	dropzone.ondragover = function() {
		this.className = "dropzone dragover";
		return false;
	};
	dropzone.ondragleave = function() {
		this.className = "dropzone";
		return false;
	};
	dropzone.ondrop = function(e) {
		e.preventDefault();
		dropped = true;
		uploads.innerHTML = "";
        fileInput.files = e.dataTransfer.files;
        generateNames(e.dataTransfer.files);
        this.className = "dropzone";
	};
	dropzone.onclick = function(e) {
		e.preventDefault();
		fileInput.click();
	};
	fileInput.onchange = function() {
		uploads.innerHTML = "";
		if(!dropped)
            generateNames(this.files);
        dropped = false;
	};
})();

const hamburger = document.querySelector(".hamburger");
const navLinks = document.querySelector(".nav-links");
const links = document.querySelectorAll(".nav-links li");

hamburger.addEventListener('click', ()=>{
   //Animate Links
    navLinks.classList.toggle("open");
    links.forEach(link => {
        link.classList.toggle("fade");
    });

    //Hamburger Animation
    hamburger.classList.toggle("toggle");
});
