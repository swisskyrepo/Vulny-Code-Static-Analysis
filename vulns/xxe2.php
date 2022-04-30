<?php
if ( isset( $_GET['name'] ) ) {
libxml_use_internal_errors( true );
libxml_disable_entity_loader( false );
$xml = '<?xml version="1.0" encoding="UTF-8" standalone="no" ?>' . $_GET['name'];
$parsed = simplexml_load_string( $xml, 'SimpleXMLElement', LIBXML_NOENT );
if ( !$parsed ) {
foreach( libxml_get_errors() as $error )
echo $error->message . "\n";
} else {
echo 'Hello ' . $parsed . "\n";
}
 }
?>