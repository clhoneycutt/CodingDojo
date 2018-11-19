// DOM? What's that?
// Document Object Model
console.dir(document);
document.title = "ZOINKS!!!"
// How does Javascript affect the DOM?
console.log(document.getElementsByTagName("h1"));
document.getElementsByTagName("h1")[0].innerText = "Hello Javascript";

// How does jQuery fit in?


$(document).ready(function(){

    $("button").click(function(){
        $("#first").fadeOut();
    })

})