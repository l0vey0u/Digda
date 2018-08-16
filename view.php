<!DOCTYPE html>
<html>
<head>
	<title> Vue Page </title>
	<meta charset='utf-8'/>
</head>
<body>
	<form method='get'>
		<input type='text' name='key'/>
		<input type='submit'/>
	</form>
</body>
</html>
<?php
	session_start();
	function checkValidate($q)
	{
		if(!empty($_GET['key']))
		{
			foreach($q as $k)
			{
				if(str_replace('.json', '', $k)===$_GET['key'])
					return TRUE;		
			}
		}
		return FALSE;
	}

	$queue = array_diff(scandir('./queue'), array('..', '.'));
	
	if(!empty($_GET['key']))
	{
		if(checkValidate($queue))
		{
            if(!file_exists('./result/'.$_GET['key']))
            {
			    shell_exec('python controller.py '.$_GET['key']);		
            }
            $infoFile = file_get_contents('./result/'.$_GET['key'].'/queueInfo.txt');
            echo "<h1> URL : ".substr($infoFile,4)."</h1>";
            if(file_exists('./result/'.$_GET['key'].'/xss.json'))
            {
                $xss_json = file_get_contents('./result/'.$_GET['key'].'/xss.json');
                #echo htmlspecialchars($xss_json);
                $xss_data = json_decode($xss_json);
                foreach($xss_data as $xss)
                {
                        echo htmlentities($xss->payl).'&nbsp';
                        list($status, $isVuln) = $xss->resInfo;
                        echo $status.'&nbsp';
                        echo $isVuln ? 'Y':'N';
                        echo "<br/>";
                }
           }
		}
		else
		{
			print("ERROR : ".$_GET['key']." is Not in Queue.");
		}
	}
	else
	{
		foreach($queue as $q) 
		{
			echo $q." | ".date("F d Y H:i:s.", filemtime("./queue/".$q))."<br/>";
		}
	}
?>
