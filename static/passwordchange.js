$(document).ready(function() {

    $('#submit').click(function() {
        var new_password = $('#new_password').val();
        var repeat_password = $('#repeat_password').val();
        if (new_password === repeat_password) {
            $.post('/passwordchange', {'new_password': new_password}, function() {
                window.location.href = '/';
            });
        } else {
            alert("Passwords do not match");
        }
    });

    $('#cancel').click(function() {
        window.location.href = '/';
    });
});