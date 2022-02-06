from time import sleep 
from modules.Aimbot import aimbot

# Micro funções do aimbot, subdivididade para cada setor do aimbot.
from utils.useUser import startPositionArrow, scannerByArrow, startFight, openGetCloseLoot # Ações.
from utils.useReadScreen import watcherEnemyName, watcherLoot # Leitura de tela
from utils.useSkills import demage, healer, healerArea,  defense, summon # Habilidades

# Analisa e atualiza o que está acontecendo no arrow do aimbot
def updateAimbotToEnemy():
    isEnemy = watcherEnemyName() # (Leitura de tela) Verifica se no camto superior esquerdo, há a indicação de um inimigo
    isLoot = watcherLoot() # (leitura de tela) Verifica se no campo superior esquerdo, há a indicação de um inimigo morto
    
    # Atualizando as propriedades do aimbot
    if (isEnemy == True):
        aimbot.isEnemy = True
    else:
        aimbot.isEnemy = False
        aimbot.inFight = False
        
    if (isLoot == True):
        aimbot.isLoot = True
    else:
        aimbot.isLoot = False
        
    print(f'isEnemy: {aimbot.isEnemy}, isLoot: {aimbot.isLoot}')
        
def skillBuffs():
    healer() # Auto cura
    defense() # Auto proteção de def
    summon() # Summon lacaio
       
        
def findEnemy():
    area = 4 # Area q o spiral procurará o inimigo
    sleep(.5) # Essa espera de .5s, serve para quando acabar de lootear, o aimbot chegar até em cima do cadaver.
    startPositionArrow() 
    scannerByArrow(area, updateAimbotToEnemy, skillBuffs)
        
# Inicia luta e atualiza propriedade como 'inFight'
def fight ():
    startFight() 
    aimbot.inFight = True
    
    demage() # (Habilidade)
    
def getLoot (): 
    
    openGetCloseLoot()
    
    # Agora q ja está em cima do cadaver, procure um novo inimigo
    findEnemy()