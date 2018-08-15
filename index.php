<!DOCTYPE html>
<html>

<head>
	<title> :: 디그다 :: </title>
	<meta charset="utf-8" />
	<script type="text/javascript" src="//code.jquery.com/jquery-1.8.3.min.js"></script>
	<link rel="stylesheet" href="style.css">
</head>

<body>

	<script type="text/javascript">
		$(document).ready(function () {
			$('#enqueue').click(function () {
				isCheck = $("input[type=checkbox]:checked").length;
				if (!isCheck) {
					alert("하나 이상의 퍼징대상을 선택해주세요.");
					return false;
				}
			});
		});
	</script>
	<div class = "box">
	<form method="POST">
		<fieldset>
			<legend> 퍼징 대상 선택 </legend>
			<table>
				<tr>
					<td>
						<label>
							<input type="checkbox" name="atkType[]" value="xss" /> XSS </label>
					</td>
					<td>
						<label>
							<input type="checkbox" name="atkType[]" value="sqli" /> SQLi </label>
					</td>
					<td>
						<label>
							<input type="checkbox" name="atkType[]" value="dirlist" /> DirListing </label>
					</td>
				</tr>
				<tr>
					<td>
						<label> URL
							<input type="url" name="url" required/> </label>
					</td>
				</tr>

			</table>
		</fieldset>

		<fieldset>
			<legend> 추가 정보 입력 </legend>
			<table>
				<tr>
					<td>
						<label> Method </label>
						<td>
							<label>
								<input type="radio" name="method" value="get"/> get </label>
						</td>
						<td>
							<label>
								<input type="radio" name="method" value="post" /> post </label>
						</td>
				</tr>
				<tr>
					<td>
						<label> Parameter
							<input type="text" name="param"/> </label>
					</td>
				</tr>
				<tr>
					<td>
						<label> Cookie
							<input type="text" name="cookie" /> </label>
					</td>
				</tr>
				<tr>
					<td>
						<label> Header
							<input type="text" name="header" /> </label>
					</td>
				</tr>
			</table>
		</fieldset>

		<input type="submit" id="enqueue" value="큐 등록" />

	</form>
	</div>
</body>

</html>

<?php
	function parseParam($paramStr) {
		$paramDict = array();
		$paramPair = explode(';', $paramStr);
		foreach($paramPair as $pp) {
			list($key, $value) = explode('=', $pp);
			if(strpos($value, 'Dig') !== FALSE) {
				$paramDict[$key] = $value;
			} else {
				throw new Exception("None Dig Point Found");
				return;
			}
		}
		return $paramDict;
	}
	session_start();
	$atkArr = array();
	if(!empty($_POST['atkType'])) {
		foreach($_POST['atkType'] as $atk) {
			$atkArr[] = $atk;
		}
	}
	$isRightForm = FALSE;
	if(count($atkArr)>0)
		if(!empty($_POST['url']))
			$isRightForm = TRUE;

	$method = '';
	$param = '';
	$cookie = '';
	$header = '';

	if(!empty($_POST['method']))
		$method = $_POST['method'];
	if(!empty($_POST['param']))
	{
		try {
			$param = parseParam($_POST['param']);
		} catch(Exception $e) {
			exit($e->getMessage());
		}
	}
		
	if(!empty($_POST['cookie']))
		$cookie = $_POST['cookie'];
	if(!empty($_POST['header']))
		$header = $_POST['header'];

	if($isRightForm) {
		$sheet = array(
				'atkType' => $atkArr,
				'url' => $_POST['url'],
				'method' => $method,
				'param' => $param,
				'cookie' => $cookie,
				'header' => $header,
		);
		$parsedSheet = json_encode((object)$sheet);
		if(!is_dir('queue'))
			mkdir('queue');
		file_put_contents("./queue/".time().".json", $parsedSheet);
		header("Location: ./");
		die();
	}
?>
