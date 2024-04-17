<?php

//insere a classe
include_once 'classes/Produto.class.php';

$produto = new Produto;
$produto2 = new Produto;

$produto->Codigo = 4001;
$produto->Descricao = 'CD - The Best of Eric Clapton';
$produto2->Codigo = 4002;
$produto2->Descricao = 'CD - Xuxa';
$produto->ImprimeEtiqueta();
$produto2->ImprimeEtiqueta();

//var_dump($produto);