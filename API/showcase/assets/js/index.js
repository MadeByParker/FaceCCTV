// Converts HTML tags to avoid them being rendered. Prevents XSS attacks.
function stripHTMLCharacters(string) {
	string = replaceAll(string, "<", "&lt;");
	string = replaceAll(string, ">", "&gt;");
	return string;
}
