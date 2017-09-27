var $form = '';

$(function() {
    init();
});

function init(){
    $form = $('#registration_form');
}

function clear_errors() {
    $form.find('li.error').remove()
}

function show_errors(errors) {
    for (var error_name in errors) {
        for (var error in errors[error_name]){
            $('[name=' + error_name + ']', $form).closest('div').append('<li class="error">'+ errors[error_name][error].message + '</li>');
        }
        $('[name=' + error_name + ']', $form).addClass('error');
    }
}

function getFormData(form) {
    var unindexed_array = form.serializeArray();
    var indexed_array = {};

    $.map(unindexed_array, function (n, i) {
        indexed_array[n['name']] = n['value'];
    });

    return indexed_array;
}

function fill_form(id){
    $.ajax({
        url: '/admin/get_user_form/' + id,
        type: 'GET',
        dataType: 'json',
        success: function (response) {
            if (response.errors) {
                console.log("errors = ", response.errors);
            } else {
                $('#registration_form_anchor').html(response.html);
            }
        },
        error: function (xhr, status, error) {
            console.log('error =', error)
        }
    });
}

function send_data() {
    var id = $('#user_id').val();
    var prefix =  (id != undefined) ? id : '';
    var user_data = getFormData($form);
    $.ajax({
        url: '/admin/user/create/' + prefix,
        type: 'POST',
        data: user_data,
        dataType: 'json',
        success: function (response) {
            if (response.errors) {
                var errors = JSON.parse(response.errors);
                clear_errors();
                show_errors(errors);
            } else {
                $('#users_list').html(response.html);
                reset_form();
            }
        },
        error: function (xhr, status, error) {
            console.log('error =', error)
        }
    });
    return false;
}

function delete_user(id) {
    var user_data = getFormData($form);
    $.ajax({
        url: '/admin/user/delete/' + id,
        type: 'POST',
        data: user_data,
        dataType: 'json',
        success: function (response) {
            $('#users_list').html(response.html);
        },
        error: function (xhr, status, error) {
            console.log('error =', error)
        }
    });
}

function reset_form(){
    clear_errors();
    $('input', $form).val('');
}