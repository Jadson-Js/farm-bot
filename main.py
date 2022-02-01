import pyautogui
from modules.StartFight import StartFight # importando modulos de utilidades

# pyautogui.PAUSE = .5 
# pyautogui.displayMousePosition()

aimbot = StartFight() # Ligando o AIMBOT

while (True):
    aimbot.printTarget() # Printa um pixel onde estará o name do mob
    aimbot.readData() # Lerá o print do printTarget
     
    if (aimbot.inFight == True): # Se estiver no modo fight, apenas resete o loop
        continue
    
    if(aimbot.isEnemy == True): # Se Não estiver em modo de luta, ataca o enemy e ativa modo luta
        aimbot.atackEnemy()