import pyautogui
import keyboard
import time

'''
ÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜ

±±°  Programa: autoTabClicker | Autor:  Renan Lima  | Data : 15/02/2022   °±±

±±ÌÍÍÍÍÍÍÍÍÍÍØÍÍÍÍÍÍÍÍÍÍÊÍÍÍÍÍÍÍÏÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÊÍÍÍÍÍÍÏÍÍÍÍÍÍÍÍÍÍÍÍÍ¹±±

±±°  Programa com intuito de automatizar cliques após leitura de barcode  °±±

±±ÌÍÍÍÍÍÍÍÍÍÍØÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ¹±±

±±°  Uso Amvian Industria e Comercio de Pecas Automotivas                 °±±

±±ÈÍÍÍÍÍÍÍÍÍÍÏÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ¼±±

ßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßß
'''
# ---- Funcao que identifica a posicao do mouse na tela

'''''
time.sleep(8)
posicao = pyautogui.position()
tamanho = pyautogui.size()
print(posicao)
print(tamanho)
'''''

# ---- Loop que identifica o pressionamento do tab

while True:
 
    keyboard.wait('tab')  
    print('Tab pressionado')  
    time.sleep(5)

    # ---- Função do clique
    pyautogui.click(x=971, y=493)      

  
  
                    

    
                                    
    
