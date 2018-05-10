<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
    <head>
        <meta charset="UTF-8">
            <title></title>
    </head>
    <body>
        <select>
        <?php
        $string = file_get_contents("http://dentaltourism-turkey.com/yscrawler/cities.json");
        $json_a = json_decode($string, true);
        $city_length = count($json_a['cities']);
        for ($i = 1; $i < $city_length ; $i++){
            echo "<option value='".$json_a['cities'][$i]['href']."'>".$json_a['cities'][$i]['name']."</option>";
        }
        
        #foreach ($json_a as $person_name => $person_a) {
            #echo $person_a['name'];
            #echo "<option value='".$json_a."'>".$json_a."</option>";
        #}
        ?>
        </select>
    </body>
</html>
