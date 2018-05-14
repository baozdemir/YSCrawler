<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
    <head>
        <meta charset="UTF-8">
            <title>city-zone</title>
            <script src="js/jquery-2.1.1.js"></script>
            <script src="js/main.js"></script>
    </head>
    <body>
        <div class="select-area">
            <select id="cities" name="cities">
                <?php
                $string = file_get_contents("http://dentaltourism-turkey.com/yscrawler/cities.json");
                $json_a = json_decode($string, true);
                $city_length = count($json_a['cities']);
                for ($i = 0; $i < $city_length; $i++) {
                    echo "<option value='" . $i . "/" . $json_a['cities'][$i]['name'] . "'>" . $json_a['cities'][$i]['name'] . "</option>";
                }
                ?>
            </select>
            <!-- That select options will be populate after cities option change-->
            <select id="zones" name="zones"></select>
        </div>    
        <div class="companylist-area" name="companies">
            <ul id="companylist" name="companylist">
                
            </ul>

        </div>
    </body>
</html>