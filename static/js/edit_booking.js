/* 
This script ensures correct user selection when editing booking
---
Logic is slightly different than new booking
*/ 
$(document).ready(function () {
    // Set click checkers 
    let timeClickChecker = 0;
    let artistClickChecker = 0;
    // Initially append the correct time to time field, hide submit button and spinner
    $("#id_time").append(`<option>${initialTime}</option>`);
    $("#submit-booking").hide();
    $("#booking-spinner").hide();
    // if time input field is clicked
    $("#id_time").click(function () {
        // and if checker is off, get avalable option for artist and date previously selected
        if (timeClickChecker == 0) {
            // show spinner
            $("#booking-spinner").show();
            // get avalable times based on artist
            $.ajax({
                url: '/bookings/booking-options/',
                method: 'GET',
                data: {
                    field_name: "#id_booked_artist",
                    selected_value: $("#id_booked_artist").val()
                },
                success: function (data) {
                    // get avalable times based on date
                    $.ajax({
                        url: '/bookings/booking-options/',
                        method: 'GET',
                        data: {
                            field_name: "#id_date",
                            selected_value: $("#id_date").val()
                        },
                        success: function (data) {
                            // empty initial time and append real options
                            $("#id_time").empty();
                            for (let i = 0; i < data.options.length; i++) {
                                $("#id_time").append(data.options[i]);
                                // hide spinner
                                $("#booking-spinner").hide();
                            }
                        }
                    });
                }
            });
            // set time clicker to used
            timeClickChecker = 1;
        }
    });
    // if artist input field is clicked
    $("#id_booked_artist").click(function () {
        // and the click checker == 0
        if (artistClickChecker == 0) {
            // show spinner
            $("#booking-spinner").show();
            $("#id_booked_artist").empty();
            $("#id_booked_artist").append('<option>Select Artist</option>');
            // get available artist based on style initial 
            $.ajax({
                url: '/bookings/booking-options/',
                method: 'GET',
                data: {
                    field_name: "#id_booked_style",
                    selected_value: $("#id_booked_style").val()
                },
                // append artists names to input field
                success: function (data) {
                    $("#id_booked_artist").empty();
                    for (let i = 0; i < data.options.length; i++) {
                        $("#id_booked_artist").append(data.options[i]);
                        // hide spinner
                        $("#booking-spinner").hide();
                    }
                }
            });
            // set artist click checker to used
            artistClickChecker = 1;
        }
    });
    // if booked style is changed anytime during the editing
    $("#id_booked_style").change(function () {
        // show spinner
        $("#booking-spinner").show();
        // srt both click checkers to used
        timeClickChecker = 1;
        artistClickChecker = 1;
        // hide subsequent input fields
        $("#id_date, #id_time, label[for='id_date'], label[for='id_time'], #submit-booking").hide();
        let selectedValue = $(this).val();
        // if selected value is the default value, hide all subsequent fields
        if (selectedValue == 0) {
            $("#id_booked_artist, #id_date, #id_time, #submit-booking, label[for='id_date'], label[for='id_time'], #booking-spinner").hide();
        }
        // get options based on user selection
        $.ajax({
            url: '/bookings/booking-options/',
            method: 'GET',
            data: {
                field_name: "#id_booked_style",
                selected_value: selectedValue
            },
            // append received data to booked artist
            success: function (data) {
                $("#id_booked_artist").empty();
                for (let i = 0; i < data.options.length; i++) {
                    $("#id_booked_artist").append(data.options[i]);
                    if (selectedValue != 0) {
                        $("#id_booked_artist").show();
                        // hide spinner
                        $("#booking-spinner").hide();
                    }
                }
            }
        });
    });
    // if booked artist input field has changed
    $("#id_booked_artist").change(function () {
        // show spinner
        $("#booking-spinner").show();
        // set click checkers to used
        timeClickChecker = 1;
        artistClickChecker = 1;
        // reset date value
        $("#id_date").val('');
        // hide subsequent fields
        $("#id_time, label[for='id_time'], #submit-booking").hide();
        let selectedValue = $(this).val();
        if (selectedValue == 0) {
            $("#id_date, #id_time, #submit-booking, label[for='id_date'], label[for='id_time'], #booking-spinner").hide();
        }
        // send selected artist to back end
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
        // changed checkers to used
        timeClickChecker = 1;
        artistClickChecker = 1;
        // hide subsequent fields
        $("#submit-booking").hide();
        let selectedValue = $(this).val();
        // get list of available times
        $.ajax({
            url: '/bookings/booking-options/',
            method: 'GET',
            data: {
                field_name: "#id_date",
                selected_value: selectedValue
            },
            success: function (data) {
                //append times to time input field
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
    // if time changed
    $("#id_time").change(function () {
        // show submit button
        $("#submit-booking").show();
    });
});