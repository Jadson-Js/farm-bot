from modules.Aimbot import Aimbot # Class com o celebro do aimbot, contem todas ações do pyautogui
from utils.Main import Main # Class com utilidades principal, Ações completas do aimbot.
from utils.User import User # Class com funções q agirão diretamente com o aimbot.  
from utils.ReadScreen import ReadScreen # Class com funções especificas para leitura de tela.

aimbot = Aimbot()
useReadScreen = ReadScreen(aimbot)
useUser = User(aimbot, useReadScreen)
useMain = Main(aimbot, useUser, useReadScreen)

while (True):
    print('Loop Restarted')
    useMain.updateAimbotToEnemy() # Atualiza as propriedades 'inFight' e 'isEnemy' do aimbot

    if (aimbot.inFight == True): 
        continue

    # Se a atualização indicou q existe um inimigo, e ainda não está lutando, então lute
    if(aimbot.isEnemy == True): 
        useMain.fight()
    else:
        useMain.findEnemy()
        
    # obs: Pode parecer q a existencia das duas variavéis são desnessesaria, porém a ordem q é manipulada cada uma, interfere se o aimbot vai iniciar um combate ou se ele ja está em combate e graças a isso, o aimbot se torná mais seguro
