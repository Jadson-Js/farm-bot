from utils.utils import clickMe, scannerToAtack, atack

while (True):
    dataScanner = scannerToAtack()
    
    if (dataScanner['inFight'] == True): 
        continue
    
    if(dataScanner['isEnemy'] == True): 
        atack()
    else:
        clickMe()