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

# (Leitura de tela) Verifica se no camto superior esquerdo, há a indicação de um inimigo
def watcherEnemyName (): 
    # Dados do pixel onde fica o enemyName
    coordinate = (1298, 39, 1, 1)
    rgb = (221,   0,   0)
    
    # Retorna a localização do pixel se coiciderem com os dados enviados, se não retorna None
    isEnemy = findInScreenshot(coordinate, rgb)
    
    if (isEnemy !=  None):
        isEnemy = True
    else:
        isEnemy = False
    
    return isEnemy

# (leitura de tela) Verifica se no campo superior esquerdo, há a indicação de um inimigo morto
def watcherLoot (): 
    # Dados do pixel onde fica o enemyName
    coordinate = (1269, 43, 1, 1)
    rgb = (208,   208,   208)
    
    # Retorna a localização do pixel se coiciderem com os dados enviados, se não retorna None
    isLoot = findInScreenshot(coordinate, rgb)
    
    if (isLoot !=  None):
        isLoot = True
    else:
        isLoot = False
    
    return isLoot