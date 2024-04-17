<?php
final class ContaPoupanca extends Conta {
    public $Aniversario;
    #Método construtor (sobrescrito), agora também inicia a variável $Limite
    function __construct($agencia, $codigo, $dataDeCriacao, $titular, $senha, $saldo, $aniversario){

  

    #chamada do método construtor da classe pai
    parent::__construct($agencia, $codigo, $dataDeCriacao, $titular, $senha, $saldo);
    $this->Aniversario = $aniversario;

    }

    function Retirar($quantia) {
        if ($this->Saldo >= $quantia){
            #executa método da classe pai
            parent::Retirar($quantia);
        }
        else {
            echo "Retirada não permitida...<br>";
            return false;
        }

        return true;
    }

    function Transferir($Conta, $Valor)
    {
        if ($this->Retirar($Valor))
        {
            $Conta->Depositar($Valor);
        }
    }

}