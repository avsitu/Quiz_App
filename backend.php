<?php
	//connect to database
	$db = pg_connect("dbname=quiz_bot");
	if (!$db) {
		die("Error in connection: " . pg_last_error());
	}

	//execute test query
	$query = "SELECT * FROM category";
	$result = pg_query($db, $query);
	if(!$result) {
		die("Error");
	}

	echo $result;
	
	pg_free_result($result);
	pg_close($db);
?>