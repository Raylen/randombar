var $form = '',
    entry_to_delete_id = 0;

$(function() {
    init();
});

function init(){
    $form = $('#game_form');
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
        url: '/admin/get_game_form/' + id,
        type: 'GET',
        dataType: 'json',
        success: function (response) {
            if (response.errors) {
                console.log("errors = ", response.errors);
            } else {
                $('#form_anchor').html(response.html);
            }
        },
        error: function (xhr, status, error) {
            console.log('error =', error)
        }
    });
}

function send_data() {
    var id = $('#entry_id').val();
    var prefix =  (id != undefined) ? id : '';
    var object_data = getFormData($form);
    $.ajax({
        url: '/games/create/' + prefix,
        type: 'POST',
        data: object_data,
        dataType: 'json',
        success: function (response) {
            if (response.errors) {
                var errors = JSON.parse(response.errors);
                clear_errors();
                show_errors(errors);
            } else {
                $('#game_list').html(response.html);
                reset_form();
            }
        },
        error: function (xhr, status, error) {
            console.log('error =', error)
        }
    });
    return false;
}

function show_delete_modal(id){
    entry_to_delete_id = id;
    $("#admin_object_delete_modal").modal('show');
}

function delete_entry() {
    var object_data = getFormData($form);
    $.ajax({
        url: '/games/delete/' + entry_to_delete_id,
        type: 'POST',
        data: object_data,
        dataType: 'json',
        success: function (response) {
            $('#game_list').html(response.html);
            $("#admin_object_delete_modal").modal('hide');
        },
        error: function (xhr, status, error) {
            console.log('error =', error)
        }
    });
}

function reset_form(){
    clear_errors();
    $('input', $form).val('');
    $('textarea', $form).val('');
    $('input:checkbox', $form).prop('checked', false);
}