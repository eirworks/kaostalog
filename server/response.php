<?php

function json_response(array $data, $status = 200)
{
    header("Access-Control-Allow-Origin: *");
    header("Content-Type: application/json");
    echo json_encode($data);
}

function error_response(string $error, $status = 400) 
{
    json_response([
        'error' => $error,
    ], $status);
}