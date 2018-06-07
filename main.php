<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
    <head>
        <meta charset="UTF-8">
            <title>city-zone</title>
            <script src="js/jquery-2.1.1.js"></script>
            <script src="js/main.js"></script>
            <script src="js/bootstrap.js"></script>
            <link rel="stylesheet" href="css/bootstrap.css"></link>
            <link rel="stylesheet" href="css/bootstrap-grid.css"></link>
            <link rel="stylesheet" href="css/bootstrap-reboot.css"></link>
            <link rel="stylesheet" href="css/main.css"></link>
            <link rel="stylesheet" href="css/ysapp.css"></link>

    </head>
    <body>
        <header class="main ys-header ">
            <div class="top"></div>
            <div class="inner ys-header-zone">
                <div class="container">
                    <div class="row">
                        <div class="col-md-3 logoSection">
                            <img src="img/yslogo.png" alt="logo"></img>
                        </div>
                        <div class="col-md-4 ">
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
                        </div>    
                        <div class="col-md-4">
                            <!-- That select options will be populate after cities option change-->
                            <select id="zones" name="zones"></select>
                        </div>
                    </div>
                </div>
            </div>
        </header>
        <div class="container">
            <div class="row">
                <ul id="companylist" name="companylist">

                </ul>
            </div>        
        </div>
        <div class="companylist-area" name="companies">


        </div>
        <div class="menu-table-container">
            <table id="menu-table" class="table-light">

            </table>

        </div>
        <div id="comments">

        </div>
    </body>
</html>