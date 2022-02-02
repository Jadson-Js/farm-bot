from modules.Aimbot import Aimbot 

aimbot = Aimbot() # Ligando o AIMBOT

# Tira uma screenshot no pixel no name do enemy   
def scannerToAtack ():
    screenshot = aimbot.printTarget() # Printa um pixel onde estará o name do mob
    
    aimbot.readScreen(screenshot) # Lerá o print do printTarget
    
    return {'isEnemy': aimbot.isEnemy, 'inFight': aimbot.inFight}

def atack ():
    aimbot.atackEnemy()
    