$(document).ready(function() {
    $('#request-button').click(function(){
        $.get("https://api.github.com/users/clhoneycutt", function displayName(data) {
            const target = document.getElementById('github-name')
            target.innerHTML = data.name;
        })
    })
});
