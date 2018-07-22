<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
    <head>
        <meta charset="UTF-8">
            <title>city-zone</title>
            <script src="js/jquery-2.1.1.js"></script>
            <script src="js/main.js"></script>
            <!-- Latest compiled and minified CSS -->
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous"/>

            <!-- Optional theme -->
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous"/>

            <!-- Latest compiled and minified JavaScript -->
            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
            <link rel="stylesheet" href="css/bootstrap-grid.css"></link>
            <link rel="stylesheet" href="css/bootstrap-reboot.css"></link>
            <link rel="stylesheet" href="css/main.css"></link>
            <link rel="stylesheet" href="css/ysapp.css"></link>

    </head>
    <body>
        <header class="main ys-header ">
            <div class="top">
                <div class="container">
                    <div class="row">
                        <div class="col-md-4 col-md-offset-4 banners">
                            <div class="banners-container">
                                <script type="text/javascript">
                                    document.write('<scr' + 'ipt src="//ad.yemeksepeti.com/servlet/view/banner/javascript/zone?zid=401&pid=0&random=' + Math.floor(89999999 * Math.random() + 10000000) + '&millis=' + new Date().getTime() + '&referrer=' + encodeURIComponent(document.location) + '" type="text/javascript"></scr' + 'ipt>');
                                </script>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="inner">
                <div class="container">
                    <div class="row">
                        <div class="col-md-4 logoSection">
                            <span class="shadow-container"><span class="shadow"><img src="img/yslogo.png" style="margin-top: 30%; margin-left: 20%" alt="logo"></img></span></span>
                        </div>
                        <div class="col-md-4 form">
                            <div class="col-md-4 ">
                                <select class="form-control" id="cities" name="cities" style="width:300px;">
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
                            <div id="ys-areaSelector-droparea"></div>
                        </div>
                        <div class="col-md-4 form searchBarArea">
                            <!--<span id="search-loading-wrapper"></span>
                            <input class="form-control search-box" placeholder="Yemek, mutfak veya restoran arayın." type="text" tabindex="2">-->
                            <div class="col-md-4">

                                <!-- That select options will be populate after cities option change-->
                                <select class="form-control" id="zones" name="zones" style="width:300px;"></select>
                            </div>
                        </div>                      
                    </div>
                </div>
            </div>
        </header>
        <div class="container">
            <div class="page-header">
                <h1><span class="pull-right label label-default"></span></h1>
            </div>
            <div class="row">
                <div class="col-md-6">
                    <div class="panel with-nav-tabs panel-default">
                        <div class="panel-heading">
                            <ul class="nav nav-tabs">
                                <li class="active"><a href="#tab1default" data-toggle="tab">Restorantlar</a></li>

                            </ul>
                        </div>
                        <div class="panel-body">
                            <div class="tab-content">
                                <div class="tab-pane fade in active" id="tab1default">
                                    <table border=0 class="circle-list">
                                        <tr>
                                            <td>
                                                <ol id="companylist" name="companylist">
                                                </ol>
                                            </td>
                                        </tr>
                                    </table>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-md-6">
                    <div class="panel with-nav-tabs panel-default">
                        <div class="panel-heading">
                            <ul class="nav nav-tabs">
                                <li class="active"><a href="#tab1default" data-toggle="tab">Menüler</a></li>
                                <li><a href="#tab2default" data-toggle="tab">Yorumlar</a></li>
                                <li><a href="#tab3default" data-toggle="tab">Analizler</a></li>
                                <!--<li class="dropdown">
                                    <a href="#" data-toggle="dropdown">Dropdown <span class="caret"></span></a>
                                    <ul class="dropdown-menu" role="menu">
                                        <li><a href="#tab4default" data-toggle="tab">Default 4</a></li>
                                        <li><a href="#tab5default" data-toggle="tab">Default 5</a></li>
                                    </ul>
                                </li>-->
                            </ul>
                        </div>
                        <div class="panel-body">
                            <div class="tab-content">
                                <div class="tab-pane fade in active" id="tab1default">
                                    <div class="menuitem">
                                        <table id="menu-table" class="table-light">
                                        </table>
                                    </div>
                                </div>
                                <div class="tab-pane fade" id="tab2default">
                                    <div id="comments">

                                    </div>
                                </div>
                                <div class="tab-pane fade" id="tab3default"></div>
                            </div>
                        </div>
                    </div>
                </div>

            </div>
        </div>
        <div class="companylist-area" name="companies">


        </div>


    </body>
</html>