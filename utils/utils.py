from modules.Aimbot import Aimbot 

aimbot = Aimbot()

# Screenshot de um local selecionado e retorna a coordenadas do getpixel
def findInScreenshot (coordinate, rgb):
    # Declarando coordenadas e rgb
    aimbot.regionToPrint = coordinate
    aimbot.rgbWanted = rgb
    
    screenshot = aimbot.printTarget() 
    
    location = aimbot.findRgb(screenshot) 
    return location

def myLocation ():
    # Coordenadas da area onde o user pode estar
    coordinate = (800, 200, 400, 350)
    rgb = (255,  57, 255)
    
    location = findInScreenshot(coordinate, rgb)
    return location

# Clica no use.
def clickMe ():
    coordinate = myLocation()
    if (coordinate != None):
        x = coordinate['x']
        y = coordinate['y'] + 7
        aimbot.clickIn(x, y)
    else:
        return
    
def startPositionArrow ():
    clickMe() 
    aimbot.moveArrow('up', 1)
    aimbot.moveArrow('right', 1)


def scannerToAtack ():
    # Coordenadas do pixel no name enemy
    coordinate = (1273, 42, 1, 1)
    rgb = (255, 0, 0)
    
    location = findInScreenshot(coordinate, rgb)
    
    if (location != None):
        aimbot.isEnemy = True
    else:
        aimbot.isEnemy = False
        aimbot.inFight = False
    
    # ['isEnemy] == O scanner identificou algum inimigo & ['inFight'] == O aimbot ja está em um kombate
    return {'isEnemy': aimbot.isEnemy, 'inFight': aimbot.inFight}    
    # obs: Pode parecer q a existencia das duas variavéis são desnessesaria, porém a ordem q é manipulada cada uma, interfere se o aimbot vai iniciar um combate ou se ele ja está em combate e graças a isso, o aimbot se torná mais seguro

def findEnemy ():
    startPositionArrow()
    
    direction = ('down', 'left', 'up', 'right')
        
    #FIRST CICLE
    for index in range(0, len(direction)):
        aimbot.moveArrow(direction[index], 2)

def atack ():
    aimbot.atackEnemy()