$(document).ready(function() {

    $('#submit').click(function() {
        var login = $('#new_login').val();
        var password = $('#new_password').val();

        $.post('/signin', {'login': login, 'password': password}, function(data) {
            if (data === 'error'){
                alert('User already exists. Try login in or choose different login');
            } else if (data === 'issue') {
                alert('Server issues, please try again later');
            } else {
                window.location.href = '/';
            }
        });
    });

    $('#login').click(function(){
        window.location.href = "/login";
    });
});