from modules.Aimbot import aimbot

# Screenshot de um local selecionado e retorna a coordenadas do getpixel
def findInScreenshot (coordinate, rgb):
    # Declarando dados do pixel nas propriedades do aimbot
    aimbot.regionToPrint = coordinate
    aimbot.rgbWanted = rgb
    # Tira print de uma area especificada nas propriedades do aimbot
    screenshot = aimbot.printTarget() 
    # Retorna a localização do pixel q coincide com as propriedades do aimbot, se não for encontrado retorna None
    location = aimbot.findRgb(screenshot) 
    return location

def myLocation ():
    # Coordenadas da area onde o user pode estar
    coordinate = (800, 200, 400, 350)
    rgb = (255,  57, 255)
    location = findInScreenshot(coordinate, rgb)
    return location

def scannerEnemyName ():
    # Dados do pixel onde fica o enemyName
    coordinate = (1273, 42, 100, 100)
    rgb = (255, 0, 0)
    # Retorna a localização do pixel se coiciderem com os dados enviados, se não retorna None
    enemyLocation = findInScreenshot(coordinate, rgb)
    return enemyLocation