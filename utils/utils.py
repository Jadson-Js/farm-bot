from modules.Aimbot import Aimbot 

aimbot = Aimbot() # Ligando o AIMBOT

# Tira uma screenshot no pixel no name do enemy   
def scannerToAtack ():
    aimbot.regionPrint = (1273, 42, 1, 1)
    aimbot.rgbWanted = [255, 0, 0]
    
    screenshot = aimbot.printTarget() # Printa um pixel onde estará o name do mob
    
    location = aimbot.findRgb(screenshot) # Lerá o print do printTarget
    
    if (location != None):
        print(location)
        aimbot.isEnemy = True
    else:
        aimbot.isEnemy = False
        aimbot.inFight = False
    
    return {'isEnemy': aimbot.isEnemy, 'inFight': aimbot.inFight}

def atack ():
    aimbot.atackEnemy()