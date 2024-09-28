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

    $foundItem['description'] = nl2br($foundItem['description']);

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

    $products = array_map(function($product) {
        $product['description'] = nl2br($product['description']);
        return $product;
    }, $products);

    json_response([
        'products' => $products,
    ]);
}