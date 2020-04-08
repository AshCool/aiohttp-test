$(document).ready(function() {
       
    $('#submit').click(function() {
        var login = $('#login').val();
        var password = $('#password').val();
        $.post('/login', {'login': login, 'password': password}, function() {
            window.location.href = '/';
        });
    });

    // signin button is clicked, redirecting to signin page
    $('#signin').click(function(){
        window.location.href = "signin";
    });
});
