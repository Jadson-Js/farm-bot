from modules.Aimbot import aimbot

# Micro funções do aimbot, subdivididade para cada setor do aimbot.
from utils.useUser import startPositionArrow, scannerByArrow, startFight, openLoot, getCloseLoot # Ações.
from utils.useReadScreen import watcherTarget, watchLootOpen # Leitura de tela
from utils.useSkills import demage, healer,  defense, summon # Habilidades

# Analisa e atualiza o que está acontecendo no arrow do aimbot
def updateAimbotToEnemy():
    target = watcherTarget() 

    if (target == 'isEnemy'):
        aimbot.isEnemy = True
    else:
        aimbot.isEnemy = False
        aimbot.inFight = False
        
    if (target == 'isLoot'):
        aimbot.isLoot = True
    else:
        aimbot.isLoot = False
        
    print(f'isEnemy: {aimbot.isEnemy}, isLoot: {aimbot.isLoot}')
    
    print(';')
        
# Vai procurar um inimigo usando as cetas
def findEnemy():
    print('findEnemy():')
    
    area = 4 
    startPositionArrow() 
    scannerByArrow(area, updateAimbotToEnemy, skillBuffs)
    
    print(';')
        
# Luta com o inimigo
def fight ():
    print('fight()')

    startFight() 
    aimbot.inFight = True
    
    demage() 
    
    print(';')
    
# Faz o looteamento do cadaver
def loot (): 
    print('loot()')

    openLoot()
    
    open = watchLootOpen()
    
    if (open == True):
        getCloseLoot()
        
    findEnemy()
    
    print(';')
    
# Usa habilidades de auto buff
def skillBuffs():
    print('skillBuffs():')
    
    healer() 
    defense() 
    summon() 
    
    print(';')