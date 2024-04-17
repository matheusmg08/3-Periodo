<?php

include 'classes/Funcionario.class.php';
include 'classes/Estagiario.class.php';

$pedrinho = new Estagiario;
$pedrinho->SetSalario(248);

echo 'O Salário do Pedrnho é R$: ' . $pedrinho->GetSalario() . '<br>';