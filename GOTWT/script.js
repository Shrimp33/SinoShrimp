function Home() {
    let url = window.location.href;
    // Get root "SinoShrimp"
    let root = url.substring(0, url.lastIndexOf("SinoShrimp")) + "SinoShrimp";
    // Redirect to home page
    window.location.href = root + "/index.html";
}