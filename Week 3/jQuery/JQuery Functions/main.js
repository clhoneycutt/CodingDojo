$(document).ready(function() {
    // .click (all)
    // .addClass
    
    $("button#addClass").click(function() {
            $('p#addColor').addClass("red");
    });

    // $( "button#addClass" ).click(function() {
    //     $( 'p#addColor' ).toggleClass( "red" );
    // });

    // .slideToggle
    $('button#slideToggle').click(function() {
        $('img#slideImage').slideToggle("fast");
    });

    // .append
    $('button#append').click(function() {
        $('p#paraAppend').append(" THIS IS A NEW PARAGRAPH ");
    });

    // .toggle
    $('button#toggle').click(function() {
        $('p#hide_seek').toggle();
    });

    // .hide
    $('button#hide').click(function() {
        $('p#hideme').hide();
    });

    // .show
    $('button#show').click(function() {
        $('p#hideme').show();
    });

    // .slideUp
    $('button#slideUp').click(function() {
        $('p#slide').slideUp();
    });

    // .slideDown
    $('button#slideDown').click(function() {
        $('p#slide').slideDown();
    });

    // .fadeIn
    $('button#fadeIn').click(function() {
        $('p#fade').fadeIn();
    });

    // .fadeOut

    $('button#fadeOut').click(function() {
        $('p#fade').fadeOut();
    });

    // .before
    // .after
    // .html
    // .attr
    // .val
    // .text
});







