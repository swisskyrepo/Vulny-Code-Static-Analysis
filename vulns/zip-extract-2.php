<?php

    $dst_dir = $_FILE['dst']['name'];
    $zip = new ZipArchive(); 
    if($zip->open($upload_dir.$filename) === true)
    {
        $zip->extractTo($dst_dir);
        $zip->close();
    } 

?>