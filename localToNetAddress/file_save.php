<?php

	if ($_FILES["file"]["error"] > 0)
	{
		$ret = array("return" => 0);
	}
	else
	{
		//file message
		$final_file_name = time().".".end(explode(".",$_FILES["file"]["name"]));
		$ret = array("name"=>$_FILES["file"]["name"],
					 "type"=>$_FILES["file"]["type"],
					 "size"=>$_FILES["file"]["size"]/1024,
					 "return"=>$_SERVER["HTTP_HOST"] ."/upload/".$final_file_name);

		//file save
		if (file_exists("upload/" . $final_file_name))
		{
			$ret = array("return" => 1);
		}
		else
		{
			move_uploaded_file($_FILES["file"]["tmp_name"], "upload/" . $final_file_name);
		}
		echo json_encode($ret);
	}
	
?>


