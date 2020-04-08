$(document).ready(function() {

    $('#logout').click(function() {
        $.post('/', {'action': 'logout'}, function() {
            window.location.href = '/login';
        })
    });

    $('#delete_account').click(function() {
        var q = confirm("Are you sure you want to delete your account? This action cannot be reverted");
        if (q == true) {
            $.post('/', {'action': 'delete'}, function() {
            window.location.href = '/login';
        });
        }
    });
});