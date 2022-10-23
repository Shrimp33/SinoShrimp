const MIN = 81;  // Change theese on update
const MAX = 82;

function indexcheck()
{
    let prevT = document.getElementById("prevT");
    let nextT = document.getElementById("nextT");
    let prevB = document.getElementById("prevB");
    let nextB = document.getElementById("nextB");

    if (index + 1 <= MAX)
    {
        nextT.hidden = false;
        nextB.hidden = false;
        // console.log("Next: " + (index + 1));
    }
    if (index - 1 >= MIN)
    {
        prevT.hidden = false;
        prevB.hidden = false;
        // console.log("Prev: " + (index - 1));
    }
}

function next()
{
    // Redirect to next page
    window.location.href = window.location.href.substring(0, "c" + index) + "c" + (index + 1) + ".html";
}
function prev()
{
    // Redirect to previous page
    window.location.href = window.location.href.substring(0, "c" + index) + "c" + (index - 1) + ".html";
}
function Home()
{
    // Exacly what it says
    window.location.href =  window.location.href.substring(0, window.location.href.indexOf("GOTWT")) + "index.html";
}