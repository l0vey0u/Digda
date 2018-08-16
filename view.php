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
			echo "<pre>".shell_exec('python controller.py '.$_GET['key'])."</pre>";		
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
