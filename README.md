# autoTabClicker
Desenvolvido por Renan Lima em 15/02/2022
Feito como solução Amvian Automotive e Camaco
Brasil, Atibaia

------------------------------------------------------------------------------- 

-------- FUNCIONALIDADE E LÓGICA:

Foram utilizadas três bibliotecas:

- pyautogui
- keyboard
- time 

Onde respectivamente: controle do mouse e teclado; captação das teclas pressionadas;
Pausa da aplicação por um tempo determinado.
Foi desenvolvido para automatizar clique no campo de preenchimento, após a
coleta do código de barras, onde o operador perdia demasiado tempo
clicando ele mesmo nos campos.

A aplicação é iniciada após o pressionar do TAB, tecla essa, que envia as informações
do campo para o BD. O coletor fará o papel de pressionar o TAB após a leitura 
do código de barras.

-------- AJUSTES NECESSÁRIOS:

* É importante lembrar, que esse script funciona de acordo com as dimensões da
tela do usuário, onde o mouse será posicionado exatamente onde for determinado 
na função. Por isso é importante que rode a função que identifica a posição do 
mouse na tela.

* Cuidado ao utilizar dois monitores ou mais, já que o script pode ficar perdido
e não reconhecer a real coordernada indicada.

* Para funcionar da forma esperada, o coletor deve estar configurado para 
pressionar o TAB após a coleta (leitura). Veja no manual do fabricante como 
realizar isso.


