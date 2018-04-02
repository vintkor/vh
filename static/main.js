(function () {

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    function select2init(data) {
        $(".select2").select2({
            width: '100%'
        });
    }

    select2init();

    $('#add-parameter').click(function (e) {
        e.preventDefault();

        var container = $('#parameters');

        $.ajax({
            method: 'POST',
            data: {'action': 'add-parameter'},
            success: function (data) {
                container.append(data);
                select2init();
            },
            error: function (e) {
                console.log(e);
            }
        });
    });

    $(document).on('click', '.delete-parameter', function (e) {
        e.preventDefault();
        var row = $(this).parent('.row-parameter');
        swal({
            title: 'Вы уверены?',
            text: 'You will not be able to recover this imaginary file!',
            type: 'warning',
            showCancelButton: true,
            confirmButtonText: 'Да, удалить!',
            cancelButtonText: 'Нет, не удалять'
        }).then((result) => {
            if(result.value) {
                row.hide(800);
                setTimeout(function () {
                    row.remove();
                }, 800);
                swal(
                    'Удалено!',
                    'Your imaginary file has been deleted.',
                    'success'
                )
            } else if (result.dismiss === swal.DismissReason.cancel) {
                swal(
                    'Отменено',
                    'Your imaginary file is safe :)',
                    'error'
                )
            }
        })
    });

})();

function getParameters(select) {
    var parameterId = $(select)[0].value;
    var self = $(select);
    $.ajax({
        method: 'POST',
        data: {'action': 'get-parameter-value', 'parameter_id': parameterId},
        dataType: 'JSON',
        success: function (data) {
            var select2 = self.parents('.row-parameter').find('.set-parameter-value');
            select2.empty();
            if (data.length > 0) {
                data.forEach(function (index) {
                    var newOption = new Option(index.value, index.id, true, true);
                    select2.append(newOption).trigger('change');
                });
                select2.prop("disabled", false);
            } else {
                select2.prop("disabled", true);
            }
        },
        error: function (e) {
            console.log(e);
        }
    });
}

(function () {
    $('#example').dataTable();
})();

$('.addFormControl').find('input, select').addClass('form-control');