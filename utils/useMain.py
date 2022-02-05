from modules.Aimbot import aimbot
from utils.useUser import startPositionArrow, scannerByArrow, startFight
from utils.useReadScreen import scannerEnemyName
#from main import aimbot, useUser, useReadScreen

# Atualiza as propriedades 'inFight' e 'isEnemy' do aimbot
def updateAimbotToEnemy():
    # Vai scannear o local onde fica o nome do inimigo
    enemyLocation = scannerEnemyName() # Se um enemy for identificado, retorna as coordenadas do pixel scanneado se não 'None'
    
    # Atualizando as propriedades
    if (enemyLocation != None):
       
        aimbot.isEnemy = True
    else:
        
        aimbot.isEnemy = False
        aimbot.inFight = False
        
def findEnemy():
    startPositionArrow()
    scannerByArrow(updateAimbotToEnemy)
        
# Inicia luta e atualiza propriedade como 'inFight'
def fight ():
    startFight() 
    aimbot.inFight = True
    
        