// Converts HTML tags to avoid them being rendered. Prevents XSS attacks.
function stripHTMLCharacters(string) {
	string = replaceAll(string, "<", "&lt;");
	string = replaceAll(string, ">", "&gt;");
	return string;
}


function Menu(e){
    let list = document.querySelector('ul');
    e.name === 'menu' ? (e.name = "close",list.classList.add('top-[80px]') , list.classList.add('opacity-100')) :( e.name = "menu" ,list.classList.remove('top-[80px]'),list.classList.remove('opacity-100'))
}
