# Class cérebro do aimbot, contem todas ações do pyautogui
from modules.Aimbot import aimbot 

# Macro funções do aimbot
from utils.useMain import skillBuffs, updateAimbotToEnemy, findEnemy, fight, getLoot

while (True):
    print('Loop Restarted')
      
    skillBuffs() # (Habilidades) Auto buff o aimbot
    
    updateAimbotToEnemy() # Analisa e atualiza o que está acontecendo no arrow do aimbot

    # Se está em luta, continue
    if (aimbot.inFight == True): 
        fight()
        continue
    
    if (aimbot.isLoot == True):
        print('getLoot')
        getLoot()
        continue

    if(aimbot.isEnemy == True): 
        fight()
    else:
        findEnemy() 
        
    # obs: Pode parecer q a existencia das duas variavéis são desnessesaria, porém a ordem q é manipulada cada uma, interfere se o aimbot vai iniciar um combate ou se ele ja está em combate e graças a isso, o aimbot se torná mais seguro
