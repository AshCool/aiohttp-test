$(document).ready(function() {

    $('#logout').click(function() {
        $.post('/', {'action': 'logout'}, function() {
            window.location.href = '/login';
        })
    });

});