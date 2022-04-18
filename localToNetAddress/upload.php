<?php

//upload post file->file
function curl_post($url,$post_data)
{
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_SAFE_UPLOAD, true);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $post_data);
    $output = curl_exec($ch);
    curl_close($ch);
    return  $output;
}

$fileUrl = !empty($_GET['url'])?$_GET['url']:0;//file absUrl
$url = $_SERVER["HTTP_HOST"] .'/file_save.php';
$post_data = ['name' => 'upload_file','file'=> new CURLFile($fileUrl)];

header('content-type:application/json');

echo (curl_post($url,$post_data));


?>