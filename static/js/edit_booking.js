$(document).ready(function () {
    // Checkers
    let timeClickChecker = 0;
    let artistClickChecker = 0;
    // Initial
    $("#id_time").append(`<option>${initialTime}</option>`);
    $("#submit-booking").hide();
    $("#booking-spinner").hide();
    // CLICK
    $("#id_time").click(function () {
        if (timeClickChecker == 0) {
            $("#booking-spinner").show();
            $.ajax({
                url: '/bookings/booking-options/',
                method: 'GET',
                data: {
                    field_name: "#id_booked_artist",
                    selected_value: $("#id_booked_artist").val()
                },
                success: function (data) {
                    $.ajax({
                        url: '/bookings/booking-options/',
                        method: 'GET',
                        data: {
                            field_name: "#id_date",
                            selected_value: $("#id_date").val()
                        },
                        success: function (data) {
                            $("#id_time").empty();
                            for (let i = 0; i < data.options.length; i++) {
                                $("#id_time").append(data.options[i]);
                                $("#booking-spinner").hide();
                            }
                        }
                    });
                }
            });
            timeClickChecker = 1;
        }
    });
    $("#id_booked_artist").click(function () {
        if (artistClickChecker == 0) {
            $("#booking-spinner").show();
            $("#id_booked_artist").empty();
            $("#id_booked_artist").append('<option>Select Artist</option>');
            $.ajax({
                url: '/bookings/booking-options/',
                method: 'GET',
                data: {
                    field_name: "#id_booked_style",
                    selected_value: $("#id_booked_style").val()
                },
                success: function (data) {
                    console.log(data)
                    $("#id_booked_artist").empty();
                    for (let i = 0; i < data.options.length; i++) {
                        $("#id_booked_artist").append(data.options[i]);
                    }
                }
            });
            artistClickChecker = 1;
            $("#booking-spinner").hide();
        }
    });
    // CHANGE
    $("#id_booked_style").change(function () {
        $("#booking-spinner").show();
        timeClickChecker = 1;
        artistClickChecker = 1;
        $("#id_date, #id_time, label[for='id_date'], label[for='id_time'], #submit-booking").hide();
        let selectedValue = $(this).val();
        if (selectedValue == 0) {
            $("#id_booked_artist, #id_date, #id_time, #submit-booking, label[for='id_date'], label[for='id_time'], #booking-spinner").hide();
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
                        $("#id_booked_artist").show();
                        $("#booking-spinner").hide();
                    }
                }
            }
        });
    });
    $("#id_booked_artist").change(function () {
        $("#booking-spinner").show();
        timeClickChecker = 1;
        artistClickChecker = 1;
        $("#id_date").val('');
        $("#id_time, label[for='id_time'], #submit-booking").hide();
        let selectedValue = $(this).val();
        if (selectedValue == 0) {
            $("#id_date, #id_time, #submit-booking, label[for='id_date'], label[for='id_time'], #booking-spinner").hide();
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
        timeClickChecker = 1;
        artistClickChecker = 1;
        $("#submit-booking").hide();
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