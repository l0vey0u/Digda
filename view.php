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
			$infoLine = explode("\n", $infoFile);
			echo "<h1> URL : ".substr($infoLine[0],4)."</h1>";
			if($infoLine[1] !== '')
			{
				echo "<h1>".$infoLine[1]."</h1>";
			}
			if(file_exists('./result/'.$_GET['key'].'/xss.json'))
            {
                echo "<h3>&nbspXSS&nbsp</h3>";
                $xss_json = file_get_contents('./result/'.$_GET['key'].'/xss.json');
				$xss_data = json_decode($xss_json);
				echo "<table><tbody>";
                foreach($xss_data as $xss)
                {	
						list($status, $duration, $isVuln, $resp_text) = $xss->resInfo;
						echo "<tr><td>".$status.'</td>';
						echo "<td>".$duration."</td>";
                        echo "<td>".htmlentities($xss->payl).'</td><td>';
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
				echo "<table><tbody>";
                foreach($sqli_data as $sqli)
                {
						list($status, $duration, $isVuln, $resp_text) = $xss->resInfo;
						echo "<tr><td>".$status.'</td>';
						echo "<td>".$duration."</td>";
                        echo "<td>".htmlentities($sqli->payl).'</td><td>';
                        echo $isVuln ? 'Y':'N';
                        echo "</td></tr>";
				}
				echo "</tbody></table>";
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
