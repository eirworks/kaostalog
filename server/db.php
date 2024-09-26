<?php

// require "deps/rb.php";

// $db_connection = "sqlite:database/data.sqlite";

// R::setup($db_connection);

return json_decode(file_get_contents(implode(DIRECTORY_SEPARATOR, [__DIR__, '..', 'data', 'data.json'])), true);