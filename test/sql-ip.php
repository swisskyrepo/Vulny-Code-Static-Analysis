<?php
function GetIP(){
    $cip = $_SERVER["HTTP_X_FORWARDED_FOR"];
    $cip = $_SERVER["REMOTE_ADDR"];
    mysql_query("SELECT * from toot where ip=$cip");
}
?>