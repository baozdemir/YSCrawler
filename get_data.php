<?php

if (isset($_POST['cities_id'])) {
    $string = file_get_contents("http://dentaltourism-turkey.com/yscrawler/zones.json");
    $jsonfile = json_decode($string, TRUE);

    // get posted select option value and manipulate
    $pair = explode("/", $_POST['cities_id']);
    $index = $pair[0];
    $city = $pair[1];

    //All normal zones parsing from zones.json 
    $zonelength = count($jsonfile['allZones'][$index][$city][1]['Tüm Kampüsler']);
    $zonelength2 = count($jsonfile['allZones'][$index][$city][0]['Diğer Semtler']);

    echo " <optgroup label='Kampüsler'>";
    for ($i = 0; $i < $zonelength; $i++) {
        $len = $i+$zonelength2 ;
        echo "<option value='" .$len . "/" . $jsonfile['allZones'][$index][$city][1]['Tüm Kampüsler'][$i]['name'] . "'>" . $jsonfile['allZones'][$index][$city][1]['Tüm Kampüsler'][$i]['name'] . "</option>";
    }
    echo "</optgroup>";

    //All uni campus zones parsing from zones.json
    echo " <optgroup label='Bölgeler'>";
    for ($j = 0; $j < $zonelength2; $j++) {
        echo "<option value='" . $j . "/" . $jsonfile['allZones'][$index][$city][0]['Diğer Semtler'][$j]['name'] . "'>" . $jsonfile['allZones'][$index][$city][0]['Diğer Semtler'][$j]['name'] . "</option>";
    }
    echo "</optgroup>";

    function debug_to_console($data) {
        $output = $data;
        if (is_array($output))
            $output = implode(',', $output);

        echo "<script>console.log( 'Debug Objects: " . $output . "' );</script>";
    }

} else if (isset($_POST['zone_id'])) {
    $pair = explode("/", $_POST['city_id']);
    $index = $pair[0];
    $city = $pair[1];
    
    $pair = explode("/", $_POST['zone_id']);
    $index_zone = $pair[0];
    $zone = $pair[1];
    
    $string = file_get_contents("http://dentaltourism-turkey.com/yscrawler/json/".$city."_companies.json");
    $jsonfile = json_decode($string, TRUE);
    
    $company_length = count($jsonfile[$city][$index_zone][$zone][0]['comps']);
    
    for ($i = 0; $i < $company_length; $i++) {
        $DisplayName = $jsonfile[$city][$index_zone][$zone][0]['comps'][$i]['DisplayName'];
        $href = $jsonfile[$city][$index_zone][$zone][0]['comps'][$i]['href'];
        echo "<li><a href=".$href.">".$DisplayName."</a></li>";
    }
        
}
?>