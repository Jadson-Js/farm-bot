from utils.UserFunction import UserFunctions
from utils.ReadScreen import ReadScreen
from modules.Aimbot import Aimbot 

aimbot = Aimbot()
userFunctions = UserFunctions(aimbot)
readScreen = ReadScreen(aimbot)

while (True):
    print('Loop Restarted')
    readScreen.scannerEnemyName()

    if (aimbot.inFight == True): 
        continue

    if(aimbot.isEnemy == True): 
        userFunctions.atack()
    else:
        userFunctions.findEnemy()
