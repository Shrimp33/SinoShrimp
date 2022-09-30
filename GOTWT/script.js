// consts
const prefix = "GOTWTc";  // Name of the series / Prefix for the translation files
// General scripts for translation page
function loadTranslation(c_num) {
    // Read the translation file of the chapter
    let name = prefix + c_num + ".txt";
    // Read the file from disk
    let file = new File([""], name);
    // Open file and read text
    file.open("r");
    let text = file.read();
    // Print the text
    console.log(text);
}
loadTranslation(81);