from time import sleep 
from modules.Aimbot import aimbot

# Micro funções do aimbot, subdivididade para cada setor do aimbot.
from utils.useUser import startPositionArrow, scannerByArrow, startFight, openGetCloseLoot # Ações.
from utils.useReadScreen import watcherTarget # Leitura de tela
from utils.useSkills import demage, healer, healerArea,  defense, summon # Habilidades

# Analisa e atualiza o que está acontecendo no arrow do aimbot
def updateAimbotToEnemy():
    target = watcherTarget() # (Leitura de tela) Verifica se no canto superior esquerdo, e retorna 'isEnemy', 'isLoot' ou None

    # Atualizando as propriedades do aimbot
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
        
        
def findEnemy():
    area = 4 # Area q o spiral procurará o inimigo
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
    
def skillBuffs():
    healer() # Auto cura
    defense() # Auto proteção de def
    summon() # Summon lacaio