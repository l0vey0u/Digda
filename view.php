<!DOCTYPE html>
<html>
<head>
	<title> Vue Page </title>
	<meta charset='utf-8'/>
	<style>
        table {
            width: 100%;
            border: 1px solid #444444;
        }
        th, td {
            border: 1px solid #444444;
        }
    </style>
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
                echo "<h3>&nbspXSS&nbsp</h3>";
                $xss_json = file_get_contents('./result/'.$_GET['key'].'/xss.json');
				$xss_data = json_decode($xss_json);
				echo "<table><tbody>";
                foreach($xss_data as $xss)
                {	
						echo "<tr><td>".$status.'</td>';
                        echo "<td>".htmlentities($xss->payl).'</td><td>';
                        list($status, $isVuln) = $xss->resInfo;
						echo $isVuln ? 'Y':'N';
                        echo "</td></tr>";
				}
				echo "</tbody></table>";
            }
            if(file_exists('./result/'.$_GET['key'].'/sqli.json'))
            {
                echo "<h3>&nbspSQLi&nbsp</h3>";
                $sqli_json = file_get_contents('./result/'.$_GET['key'].'/sqli.json');
                $sqli_data = json_decode($sqli_json);
                foreach($sqli_data as $sqli)
                {
                        echo htmlentities($sqli->payl).'&nbsp';
                        list($status, $isVuln) = $sqli->resInfo;
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
