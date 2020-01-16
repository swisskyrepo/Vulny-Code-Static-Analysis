<?php
    $xml = simplexml_load_file('employees.xml');

    echo "<strong>Matching employees with name 'Laura Pollard'</strong><br />";
    $employees = $xml->xpath('/employees/employee[name="'.$_GET['name'].'"]');

    foreach($employees as $employee) {
        echo "Found {$employee->name}<br />";
    }

    echo "<br />";

    echo "<strong>Matching employees younger than 54</strong><br />";
    $employees = $xml->xpath('/employees/employee[age<54]');

    foreach($employees as $employee) {
        echo "Found {$employee->id}<br />";
    }

    echo "<br />";

    echo "<strong>Matching employees as old or older than 48</strong><br />";
		$age = $_POST['age'];
    $employees = $xml->xpath('//employee[age>='.$age.']');

    foreach($employees as $employee) {
        echo "Found {$employee->age}<br />";
    }

    echo "<br />";

?>


<?php

$result = '';
if(isset($_POST['submit'])){
$doc = new DOMDocument;
$doc->load('coffee.xml');
$xpath = new DOMXPath($doc);
$query = "/Coffees/Coffee[@ID='".$_POST['search']."']";
#$result = isset($xpath->query($query)) ? $xpath->query($query) : '';
$result = $xpath->query($query);
}

?>