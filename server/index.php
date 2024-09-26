<?php

require "response.php";

$products = require("db.php");

if ($_GET['product_id']) {
    $foundItem = null;

    foreach($products as $product) {
        if ($product['id'] === $_GET['product_id']) {
            $foundItem = $product;
            break;
        }
    }

    json_response([
        'product' => $foundItem,
        'product_id' => $_GET['product_id'],
    ]);

} else {
    json_response([
        'products' => $products,
    ]);
}