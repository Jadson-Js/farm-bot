from modules.Aimbot import aimbot # Class com o celebro do aimbot, contem todas ações do pyautogui
from utils.useMain import updateAimbotToEnemy, findEnemy, fight

while (True):
    print('Loop Restarted')
    updateAimbotToEnemy() # Atualiza as propriedades 'inFight' e 'isEnemy' do aimbot

    if (aimbot.inFight == True): 
        continue

    # Se a atualização indicou q existe um inimigo, e ainda não está lutando, então lute
    if(aimbot.isEnemy == True): 
        fight()
    else:
        findEnemy()
        
    # obs: Pode parecer q a existencia das duas variavéis são desnessesaria, porém a ordem q é manipulada cada uma, interfere se o aimbot vai iniciar um combate ou se ele ja está em combate e graças a isso, o aimbot se torná mais seguro
