# import pyautogui
from utils.utils import clickMe, findEnemy, scannerToAtack, atack

#pyautogui.displayMousePosition()

dataScanner = {'isEnemy': False, 'inFight': False}    

while (True):
    if (dataScanner['inFight'] == True): 
        continue
    
    if(dataScanner['isEnemy'] == True): 
        atack()
    else:
       findEnemy()