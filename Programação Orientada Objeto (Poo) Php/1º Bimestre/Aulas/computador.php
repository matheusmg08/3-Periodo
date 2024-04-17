<?php
class Computador
{
    var $cpu;
    function ligar() #criando função
    {
        echo "Ligando computador a {$this->cpu}..."; #echo , printar na tela
    }
}

$obj = new Computador; #chamando a classe para criar objetos
$obj->cpu= "500Mhz\n"; #criando objetos
$obj->ligar();

$novoobj = new Computador;
$novoobj->cpu = readline("Insira velocidade CPU: "); #comando para digitar
$novoobj->ligar();  #chamando a função e alterando
