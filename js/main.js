/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
/*function cityChanged(obj) {
    var city_value = obj.value;
    console.log(city_value);
    $.ajax({
        url: 'ajax.php',
        data: {city: city_value},
        type: 'post',
        success: function (resp) {
            $("#Y").html(resp);
        },
        error: function (xhr, textStatus, error) {
            console.log(xhr.statusText);
            console.log(textStatus);
            console.log(error);
        }
    });
}*/


$(document).ready(function () {
    //Change in continent dropdown list will trigger this function and
    //generate dropdown options for county dropdown
    $(document).on('change', '#cities', function () {
        var cities_id = $(this).val();
        if (cities_id != "") {
            $.ajax({
                url: "get_data.php",
                type: 'POST',
                data: {cities_id: cities_id},
                success: function (response) {
                    //var resp = $.trim(response);
                    if (response != '') {
                        $("#zones").removeAttr('disabled', 'disabled').html(response);
                    }
                }
            });
        }
    });
    $(document).on('change', '#zones', function () {
        var zone_id = $(this).val();
        var city_id = $('#cities').val();
        if (zone_id != "") {
            $.ajax({
                url: "get_data.php",
                type: 'POST',
                data: {zone_id: zone_id,city_id: city_id},
                success: function (response) {
                    //var resp = $.trim(response);
                    if (response != '') {
                        $("#companylist").removeAttr('disabled', 'disabled').html(response);
                    }
                }
            });
        }
    });
});