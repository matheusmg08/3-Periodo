<?php

#carrega as classes
include 'classes/Funcionario.class.php';
include 'classes/Estagiario.class.php';

//cria objeto Funcionario

$pedrinho = new Funcionario;
$pedrinho->Nome = 'Pedrinho';

//cria objeto Estagiário
$mariana = new Estagiario;
$mariana->Nome = 'Mariana';

//imprime propriedade nome
echo $pedrinho->Nome, "<br>";
echo $mariana->Nome;