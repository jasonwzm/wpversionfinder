function get_wp_version() {
$versionFile = ABS_PATH.'/wp-includes/version.php'
// NO VERSION FILE //
if (($versionStr = @file_get_contents($versionFile))=='') return '';

$regex = "wp_version.*'(?<wpVersion>.*)'";
if (preg_match('/'.$regex.'/', $versionStr, $matches)) {
 return $matches['wpVersion'];
}
return '';
}
