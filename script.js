// Code For A Silder for the home page
// var pos = 0;
// var imglen = 1016;
// function slide(){
//     $('#blogSlider').animate({backgroundPosition : '-=2px'}, 20, 'linear', slide);
//     pos += 2;
//     if (pos >= imglen) {
//         pos = 0;
//     }
// }
// setTimeout(slide, 1000);  // I DON'T KNOW WHY, BUT IF THERE'S NO TIMEOUT, IT DOESN'T WORK

// function imgtoidb(posx) {
//     var truex = posx % 1016
//     if (truex < 180) return 1;
//     if (truex < 565) return 2;
//     if (truex < 1016) return 3;
// }

// $(document).ready(function(event) {
//     $("#blogSlider").click(function(event) {
//         var redirect = window.confirm("Do You Want to Access At Blog #" + imgtoidb(pos + event.pageX - 25));
//         if (redirect) {
//             load(imgtoidb(pos + event.pageX - 25));
//         }
//     });
//     $("#search").keydown(function(event) {
//         if (event.keyCode == 13){
//             load($("#search").val());
//         }
//     });
// });
function GOTWT() {
    const min = 81;
    const max = 81;
    // Prompt for chapters
    var chapter = prompt("Enter Chapter Number, 81 - 81 are available");
    // Redirect to chapter
    if (chapter < min || chapter > max) {
        alert("Chapter " + chapter + " is not available");
        return;
    }
    // Redirect to GOTWT
    let url = window.location.href;
    // Get root "SinoShrimp"
    let root = url.substring(0, url.lastIndexOf("SinoShrimp")) + "SinoShrimp" + "/GOTWT";
    // Redirect to home page
    window.location.href = root + "/chapter" + chapter + ".html";
}