$(document).ready(function() {

    $('#add').click(function() {
        var link = $('#new_link').val();
        $.post('/', {'action': 'add_link', 'link': link}, function() {
            window.location.href = '/';
        })
    });

    $('#logout').click(function() {
        $.post('/', {'action': 'logout'}, function() {
            window.location.href = '/login';
        })
    });

    $('#change_password').click(function() {
        $.post('/', {'action': 'change'}, function() {
            window.location.href = '/passwordchange';
        })
    });

    $('#delete_account').click(function() {
        var q = confirm("Are you sure you want to delete your account? This action cannot be reverted");
        if (q == true) {
            $.post('/', {'action': 'delete_account'}, function() {
            window.location.href = '/login';
        });
        }
    });

    $(".download").click(function(event) {
        var element_id = event.target.parentNode.id;
        alert("Couldn't make Drive's API work");
    });

    $(".delete").click(function(event) {
        var q = confirm("Are you sure you want to delete this link?");
        if (q == true) {
            var element_id = event.target.parentNode.id;
            $.post('/', {'action': 'delete_link', 'item_id': element_id}, function() {
                alert("Link was successfully deleted");
                window.location.href = '/';
            })
        }

    });
});