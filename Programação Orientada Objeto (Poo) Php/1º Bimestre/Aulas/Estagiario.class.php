<?php

class Estagiario extends Funcionario {
    /*
    método getSalario sobreescrito
    retorna o $Salario com 12% de bônus
    */

    function GetSalario()
    {
        return $this->Salario *1.12;
    }
}