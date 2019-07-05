$(document).ready(function(){
    $('img').click(function(){
        var currentImage = $(this).attr('src')
        var altImage = $(this).attr('data-alt-source');
        $(this).attr('src',altImage)
        $(this).attr('data-alt-source', currentImage)
    });
});