<html>
  <head>
    <meta charset="utf-8">
    <link rel="icon" href="./res/favicon.ico">
    <link href="./index.css" rel="stylesheet">
    <title>Much Series Very Analyse</title>
  </head>

  <body>
    <h1>Much Series Very Analyse</h1>
    <div id='console'>

    <a href='?lang=en.php'>English</a> | <a href='?lang=fr.php'>Francais</a><br><br><br>
    <img src='./doge.png' width='100px'>
    <?php

    if(isset($_GET['viewsource'])) {
        highlight_file('index.php');
        highlight_file($_GET['viewsource']);
        exit();
    }

    class Lang {

        private $lang;

        public function __construct($lang='') {
            $this->lang = !empty($lang) ? $lang : 'en.php';
        }
        public function __destruct() {
            include($this->lang);
            echo "

            </div>
            <p>© 2016 WowDoge Security . All Rights Reserved</p>
        </body>
    </html>";
        }
    }

    if (isset($_GET['lang']) && !empty($_GET['lang'])) {
        $allowed = ['fr.php', 'en.php'];
        if (in_array($_GET['lang'], $allowed)) {
            $lang = new Lang($_GET['lang']);
            setcookie("lang", serialize($lang));
        }
        else
            $lang = new Lang('en.php');
    }
    else if (isset($_COOKIE['lang']) && !empty($_COOKIE['lang'])) {
        $lang = unserialize($_COOKIE['lang']);
    }
    else {
        $lang = new Lang('en.php');
    }
    ?>
