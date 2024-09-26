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
    $query = strtolower($_GET['q']);
    if ($query) {
        $products = array_filter($products, function($product) use($query) {
            return str_contains(strtolower($product['name']), $query);
        });
    }

    json_response([
        'products' => $products,
    ]);
}