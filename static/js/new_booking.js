/*
This file ensures logic in users selection in combination of style, artist, date and time
*/
$(document).ready(function () {
    // Initial hiding of elements
    $("#id_booked_artist, #id_date, #id_time, #submit-booking, label[for='id_booked_artist'], label[for='id_date'], label[for='id_time'], #booking-spinner").hide();
    // Perform if style was changed
    $("#id_booked_style").change(function () {
        // show spinner
        $("#booking-spinner").show();
        // hide input elements
        $("#id_date, #id_time, label[for='id_date'], label[for='id_time']").hide();
        let selectedValue = $(this).val();
        // if selected value = 0 (default, hide all input elements)
        if (selectedValue == 0) {
            $("#id_booked_artist, #id_date, #id_time, #submit-booking, label[for='id_booked_artist'], label[for='id_date'], label[for='id_time'], #booking-spinner").hide();
        }
        // based on user selection, get options for artist input
        $.ajax({
            url: '/bookings/booking-options/',
            method: 'GET',
            data: {
                field_name: "#id_booked_style",
                selected_value: selectedValue
            },
            // if successful, append data to artists input field
            success: function (data) {
                $("#id_booked_artist").empty();
                for (let i = 0; i < data.options.length; i++) {
                    $("#id_booked_artist").append(data.options[i]);
                    if (selectedValue != 0) {
                        // show booked artist iput field
                        $("#id_booked_artist, label[for='id_booked_artist']").show();
                        // hide spinner
                        $("#booking-spinner").hide();
                    }
                }
            }
        });
    });
    // if artists changed
    $("#id_booked_artist").change(function () {
        // show spinner
        $("#booking-spinner").show();
        // reset date value
        $("#id_date").val('');
        // hide subsequent input fields
        $("#id_time, #submit-booking, label[for='id_time']").hide();
        let selectedValue = $(this).val();
        // if selected value == 0, hide all subsequent fields 
        if (selectedValue == 0) {
            $("#id_date, #id_time, #submit-booking, label[for='id_date'], label[for='time'], #booking-spinner").hide();
        }
        // based on user selection, artist communicated to backend
        $.ajax({
            url: '/bookings/booking-options/',
            method: 'GET',
            data: {
                field_name: "#id_booked_artist",
                selected_value: selectedValue
            },
            // if successful, show date field
            success: function (data) {
                if (selectedValue != 0) {
                    $("#id_date, label[for='id_date']").show();
                    // hide spinner
                    $("#booking-spinner").hide();
                }
            }
        });
    });
    // if date changed
    $("#id_date").change(function () {
        // show spinner
        $("#booking-spinner").show();
        // hide subsequent fields
        $("#id_time, #submit-booking, label[for='id_time']").hide();
        let selectedValue = $(this).val();
        // based on user selection, get options for time input
        $.ajax({
            url: '/bookings/booking-options/',
            method: 'GET',
            data: {
                field_name: "#id_date",
                selected_value: selectedValue
            },
            // if successful show time field and append options
            success: function (data) {
                $("#id_time").empty();
                for (let i = 0; i < data.options.length; i++) {
                    $("#id_time").append(data.options[i]);
                    $("#id_time, label[for='id_time']").show();
                    // hide spinner
                    $("#booking-spinner").hide();
                }
            }
        });
    });
    // if time changed, show submit button
    $("#id_time").change(function () {
        $("#submit-booking").show();
    });
});