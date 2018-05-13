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
    echo "$zonelength";
    echo " <optgroup label='Kampüsler'>";
    for ($i = 0; $i < $zonelength; $i++) {
        echo "<option value='" . $jsonfile['allZones'][$index][$city][1]['Tüm Kampüsler'][$i]['url'] . "'>" . $jsonfile['allZones'][$index][$city][1]['Tüm Kampüsler'][$i]['name'] . "</option>";
    }
    echo "</optgroup>";

    //All uni campus zones parsing from zones.json
    $zonelength2 = count($jsonfile['allZones'][$index][$city][0]['Diğer Semtler']);
    echo " <optgroup label='Bölgeler'>";
    for ($j = 0; $j < $zonelength2; $j++) {
        echo "<option value='" . $jsonfile['allZones'][$index][$city][0]['Diğer Semtler'][$j]['name'] . "'>" . $jsonfile['allZones'][$index][$city][0]['Diğer Semtler'][$j]['name'] . "</option>";
    }
    echo "</optgroup>";

    function debug_to_console($data) {
        $output = $data;
        if (is_array($output))
            $output = implode(',', $output);

        echo "<script>console.log( 'Debug Objects: " . $output . "' );</script>";
    }

} else if (isset($_POST['country_id'])) {
    
} else if (isset($_POST['state_id'])) {
    
}
?>