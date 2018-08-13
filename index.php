<!DOCTYPE html>
<html>

<head>
	<title> :: 디그다 :: </title>
	<meta charset="utf-8" />
	<script type="text/javascript" src="//code.jquery.com/jquery-1.8.3.min.js"></script>
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
				<tr>
					<td>
						<label> Method </label>
						<td>
							<label>
								<input type="radio" name="method" value="get" required/> get </label>
						</td>
						<td>
							<label>
								<input type="radio" name="method" value="post" /> post </label>
						</td>
				</tr>
				<tr>
					<td>
						<label> Parameter
							<input type="text" name="param" required/> </label>
					</td>
				</tr>
			</table>
		</fieldset>

		<fieldset>
			<legend> 추가 정보 입력 </legend>
			<table>
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
</body>

</html>

<?php
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
			if(!empty($_POST['method']))
					if(!empty($_POST['param']))
							$isRightForm = TRUE;
	$cookie = '';
	$header = '';
	if(!empty($_POST['cookie']))
		$cookie = $_POST['cookie'];
	if(!empty($_POST['header']))
		$header = $_POST['header'];
	if($isRightForm) {
		$sheet = array(
				'atkType' => $atkArr,
				'url' => $_POST['url'],
				'method' => $_POST['method'],
				'param' => $_POST['param'],
				'cookie' => $cookie,
				'header' => $header,
		);
		$parsedSheet = json_encode((object)$sheet);
		file_put_contents("./queue/".time().".json", $parsedSheet);
		header("Location: ./");
		die();
	}
?>