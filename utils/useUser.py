from modules.Aimbot import aimbot # ERROR: CHAMA O useMain E O useMain também chama o useUser
from utils.useReadScreen import myLocation

# Clica no user
def clickMe ():
    coordinate = myLocation() # Coordenadas de sua localização atual
    if (coordinate != None):
        # Ajustes
        x = coordinate['x'] + 2
        y = coordinate['y'] + 7
        aimbot.clickIn(x, y)
    else:
        print('DANGER: User not found!')
        return
    
# Posiciona as arrow para que simplifique o loop do findEnemy
def startPositionArrow ():
    clickMe() 
    
    aimbot.moveArrow('up')
    aimbot.moveArrow('right')
    
    
def scannerByArrow (updateAimbotToEnemy):

    direction = ('down', 'left', 'up', 'right')
    
    places = 2
    
    for area in range(0, 10):
        
        
        for index in range(0, len(direction)):
            if (index % 2 != 0):
                places += 1
                
            for moves in range(0, places):
                aimbot.moveArrow(direction[index]) 

                updateAimbotToEnemy() 
                if (aimbot.isEnemy == True):
                    return
                else:
                    continue
                
                
                
"""
FIRST SPIRAL

index | direction | places 
0     | down      | 2
1     | left      | 2
2     | up        | 2
3     | right     | 3

OUTHERS SPIRAL

index | direction | places 
0     | down      | 3
1     | left      | 4 + 1
2     | up        | 4
3     | right     | 5 + 1
"""

"""
places += 1
print(f'{direction[index]} - {places}')
aimbot.moveArrow(direction[index], places) 
"""       
"""
updateAimbotToEnemy() 
if (aimbot.isEnemy == True):
    return
else:
    continue
"""
        
            
            
def startFight ():
    aimbot.atack()
