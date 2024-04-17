<?php
#captura valor variável
$umidade = readline('Insira o valor de umidade: ');
#Testa se é maior que 90. Retorna um booleano
$vai_chover = ($umidade>90);

#testa se $vai_chover é verdadeiro
if ($vai_chover){
    echo 'Está chovendo';
} else{
    echo 'Não está chovendo';
}
