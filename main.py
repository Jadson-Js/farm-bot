# import pyautogui
from utils.UserFunction import UserFunctions
from modules.Aimbot import Aimbot 

aimbot = Aimbot()
UserFunctions = UserFunctions(aimbot)

while (True):
    if (aimbot.inFight == True): 
        continue
    
    if(aimbot.isEnemy == True): 
        UserFunctions.atack()
    else:
       UserFunctions.findEnemy()