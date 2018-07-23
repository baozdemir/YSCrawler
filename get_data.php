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
        $len = $i + $zonelength2;
        echo "<option value='" . $len . "/" . $jsonfile['allZones'][$index][$city][1]['Tüm Kampüsler'][$i]['name'] . "'>" . $jsonfile['allZones'][$index][$city][1]['Tüm Kampüsler'][$i]['name'] . "</option>";
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

    $string = file_get_contents("http://dentaltourism-turkey.com/yscrawler/json/" . $city . "_companies.json");
    $jsonfile = json_decode($string, TRUE);
    $company_length = count($jsonfile[$city][$index_zone][$zone][0]['comps']);
    for ($i = 0; $i < $company_length; $i++) {
        $DisplayName = $jsonfile[$city][$index_zone][$zone][0]['comps'][$i]['DisplayName'];
        $href = $jsonfile[$city][$index_zone][$zone][0]['comps'][$i]['href'];
        echo "<li><a href='#' onclick='getList(\"" . $href . "\");return false;' id='" . $href . "'>" . $DisplayName . "</a></li>";
    }
} else if (isset($_POST['zone_id2'])) {
    $pair = explode("/", $_POST['city_id2']);
    $index = $pair[0];
    $city = $pair[1];

    $pair = explode("/", $_POST['zone_id2']);
    $index_zone = $pair[0];
    $zone = $pair[1];

    $string = file_get_contents("http://dentaltourism-turkey.com/yscrawler/json/" . $city . "_companies.json");
    $jsonfile = json_decode($string, TRUE);
    $company_length = count($jsonfile[$city][$index_zone][$zone][0]['comps']);
    echo '<h6>Bölgedeki toplam restoran sayısı:</h6>';
    echo $company_length . "<br/>";
    $max = 0;
    $max_comp = "";

    $max_comment = 0;
    $max_comment_comp = "";
    
    $max_avg=0;
    $max_avg_comp="";
    
    for ($i = 0; $i < $company_length; $i++) {
        $DisplayName = $jsonfile[$city][$index_zone][$zone][0]['comps'][$i]['DisplayName'];
        $href = $jsonfile[$city][$index_zone][$zone][0]['comps'][$i]['href'];
        $stringMenu = file_get_contents("http://dentaltourism-turkey.com/yscrawler/menusjson/" . $href . ".json");
        $jsonfileMenu = json_decode($stringMenu, TRUE);
        $comp_comment = 0;
        $comment_length = count($jsonfileMenu['comment']);
        //firmaya yapılan yorumunların ayılması
        if ($comment_length > $max) {
            $max_comp = $DisplayName;
            $max = $comment_length;
        }
        //firma yorularının sayılması 
        for ($j = 0; $j < $menu_length; $j++) {
            $flavour = $jsonfileMenu['comment'][$j]['Flavour'];
            $speed = $jsonfileMenu['comment'][$j]['Speed'];
            $serving = $jsonfileMenu['comment'][$j]['Serving'];
            if ($flavour == "" || $speed == "" || $serving == "") {
                $comp_comment++;
            }
        }
        if ($comp_comment > $max) {
            $max_comment_comp = $DisplayName;
            $max_comment = $comp_comment;
        }
        //yorumlarda
        
    }
    echo '<h6>En fazla yorum yapılan restoran:<h6>' . $max_comp . ' ' . $max . ' yorum';
    echo '<h6>En fazla yorum yapan restoran:<h6>' . $max_comment_comp . ' ' . $max_comment . ' yorum';

} else if (isset($_POST['href'])) {
    $stringMenu = file_get_contents("http://dentaltourism-turkey.com/yscrawler/menusjson/" . $_POST['href'] . ".json");
    $jsonfileMenu = json_decode($stringMenu, TRUE);
    $menu_length = count($jsonfileMenu['menu']);

    for ($i = 0; $i < $menu_length; $i++) {
        $ItemName = $jsonfileMenu['menu'][$i]['ItemName'];
        $ItemInfo = $jsonfileMenu['menu'][$i]['ItemInfo'];
        $ItemPrice = $jsonfileMenu['menu'][$i]['ItemPrice'];

        $href = $jsonfileMenu[$city][$index_zone][$zone][0]['comps'][$i]['href'];
        echo "<tr><td>" . $ItemName . "<br />" . $ItemInfo . "</td><tr>" . $ItemPrice . "</td></tr>";
    }
} else if (isset($_POST['href2'])) {


    $stringMenu = file_get_contents("http://dentaltourism-turkey.com/yscrawler/menusjson/" . $_POST['href2'] . ".json");
    $jsonfileMenu = json_decode($stringMenu, TRUE);

    $menu_length = count($jsonfileMenu['comment']);

    for ($i = 0; $i < $menu_length; $i++) {
        $comment = $jsonfileMenu['comment'][$i]['Comment'];
        $date = $jsonfileMenu['comment'][$i]['Date'];
        $flavour = $jsonfileMenu['comment'][$i]['Flavour'];
        $speed = $jsonfileMenu['comment'][$i]['Speed'];
        $serving = $jsonfileMenu['comment'][$i]['Serving'];

        $href = $jsonfileMenu[$city][$index_zone][$zone][0]['comps'][$i]['href'];
        #echo "<p>&#34;" . $comment . "&#34;<br /> Date:" . $date . "<br />Flavour:" . $flavour . "<br /> Speed:".$speed."<br />Serving:".$serving."</p>";
        echo "<div class='card card-inner'><div class='card-body'><div class='row'><div class='col-md-10'><p class='text-secondary '>Flavour:" . $flavour . "<br /> Speed:" . $speed . "<br />Serving:" . $serving . "</p><p>.$comment.</p>" . $date . "<br /></div></div></div></div>";
    }
} else if (isset($_POST['href3'])) {
    $stringAnalysis = file_get_contents("http://dentaltourism-turkey.com/yscrawler/analysis/" . $_POST['href3'] . ".json");
    $jsonfileAnalysis = json_decode($stringAnalysis, TRUE);

    $average_length = count($jsonfileMenu['averageScore']);
    echo 'Ortalama Ürün Puanları:';
    foreach ($jsonfileAnalysis['averageScore'] as $key => $value) {
        echo "<li>" . $key . " : " . $value . "</li>";
    }
    echo 'Yorumlarda geçen ürün sayıları:';
    foreach ($jsonfileAnalysis['commentCount'] as $key => $value) {
        echo "<li>" . $key . " : " . $value . "</li>";
    }
}
?>
