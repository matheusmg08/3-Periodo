<?php
class Biblioteca
{
    const Nome = "GTK";
}
class Aplicado extends Biblioteca
{
    //declaração das constantes
    const Ambiente = "Gnome Desktop ";
    const Versao = "3.8 ";

    function __construct($Nome)

    {
        echo parent::Nome . self::Ambiente . self::Versao . $Nome . "<br>";
    }
}

echo Biblioteca::Nome . Aplicacao::Ambiente . Aplicacao::Versao . "<br>"