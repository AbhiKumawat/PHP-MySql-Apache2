/*
Name:    Abhimanyu Kumawat
Class:   CS-288 (02)
Date:    May 4th 2018
Version: Final V2.
*/
<html>
<head>
    <title>Weather Table</title>
</head>
<body>
<table align="center" border="6">

<?php
	echo '<td>'.'State'.'</td><td>'.'City'.'</td><td>'.'Weather'
	.'</td><td>'.'Temperature'.'</td><td>'.'Humidity'.'</td><td>'.'Pressure'.'</td>';

	$connect = new mysqli('localhost','abhi','Demo_pw9','myDB');

	if ($connect->connect_error)
		die('Connection failed: ' . $connect->connect_error);

	$query = 'SELECT * FROM tableWeather';
	$cursor = $connect->query($query);

	while ($row = $cursor->fetch_assoc())
	{
	  echo '<tr>';
	  echo '<td>' . $row['state'] . '</td><td>' . $row['city'] . '</td><td align="right">' 
			  . $row['weather'] .'</td><td>' . $row['temperature'] .'</td><td>' . $row['humidity'] 
			  .'</td><td>' . $row['pressure'] .'</td>';
	  echo '</tr>';
	}

    $connect->close();
?>
</table>
</body>
</html>
