#import pyautogui
from utils.utils import scannerToAtack, atack

# pyautogui.displayMousePosition()

while (True):
    dataScanner = scannerToAtack()
    print(dataScanner)
    
    if (dataScanner['inFight'] == True): 
        continue
    
    if(dataScanner['isEnemy'] == True): # Se Não estiver em modo de luta, ataca o enemy e ativa modo luta
        atack()