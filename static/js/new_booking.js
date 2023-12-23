$(document).ready(function () {
    $("#id_booked_artist, #id_date, #id_time, #submit-booking, label[for='id_booked_artist'], label[for='id_date'], label[for='id_time'], #booking-spinner").hide();
    $("#id_booked_style").change(function () {
        $("#booking-spinner").show();
        $("#id_date, #id_time, label[for='id_date'], label[for='id_time']").hide();
        let selectedValue = $(this).val();
        if (selectedValue == 0) {
            $("#id_booked_artist, #id_date, #id_time, #submit-booking, label[for='id_booked_artist'], label[for='id_date'], label[for='id_time'], #booking-spinner").hide();
        }
        $.ajax({
            url: '/bookings/booking-options/',
            method: 'GET',
            data: {
                field_name: "#id_booked_style",
                selected_value: selectedValue
            },
            success: function (data) {
                $("#id_booked_artist").empty();
                for (let i = 0; i < data.options.length; i++) {
                    $("#id_booked_artist").append(data.options[i]);
                    if (selectedValue != 0) {
                        $("#id_booked_artist, label[for='id_booked_artist']").show();
                        $("#booking-spinner").hide();
                    }
                }
            }
        });
    });
    $("#id_booked_artist").change(function () {
        $("#booking-spinner").show();
        $("#id_date").val('');
        $("#id_time, #submit-booking, label[for='id_time']").hide();
        let selectedValue = $(this).val();
        if (selectedValue == 0) {
            $("#id_date, #id_time, #submit-booking, label[for='id_date'], label[for='time'], #booking-spinner").hide();
        }
        $.ajax({
            url: '/bookings/booking-options/',
            method: 'GET',
            data: {
                field_name: "#id_booked_artist",
                selected_value: selectedValue
            },
            success: function (data) {
                if (selectedValue != 0) {
                    $("#id_date, label[for='id_date']").show();
                    $("#booking-spinner").hide();
                }
            }
        });
    });
    $("#id_date").change(function () {
        $("#booking-spinner").show();
        $("#id_time, #submit-booking, label[for='id_time']").hide();
        let selectedValue = $(this).val();
        $.ajax({
            url: '/bookings/booking-options/',
            method: 'GET',
            data: {
                field_name: "#id_date",
                selected_value: selectedValue
            },
            success: function (data) {
                $("#id_time").empty();
                for (let i = 0; i < data.options.length; i++) {
                    $("#id_time").append(data.options[i]);
                    $("#id_time, label[for='id_time']").show();
                    $("#booking-spinner").hide();
                }
            }
        });
    });
    $("#id_time").change(function () {
        $("#submit-booking").show();
    });
});