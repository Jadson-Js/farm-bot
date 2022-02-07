from modules.Aimbot import aimbot

# Screenshot de um local selecionado e retorna a coordenadas do getpixel
def findInScreenshot (coordinate, rgbTarget):
    # Declarando dados do pixel nas propriedades do aimbot
    aimbot.regionToPrint = coordinate
    aimbot.rgbWanteds = rgbTarget
    # Tira print de uma area especificada nas propriedades do aimbot
    screenshot = aimbot.printTarget() 
    # Retorna a localização do pixel q coincide com as propriedades do aimbot, se não for encontrado retorna None
    data = aimbot.findRgb(screenshot) 
    
    return data

def myLocation ():
    # Coordenadas da area onde o user pode estar
    coordinate = (800, 200, 400, 350)
    rgbTarget = [(255,  57, 255)]
    data = findInScreenshot(coordinate, rgbTarget)
    return data

# 1269, 39
# (Leitura de tela) Verifica se no camto superior esquerdo, há a indicação de um inimigo
def watcherTarget (): 
    # Dados do pixel onde fica o enemyName
    coordinate = (1269, 39, 1, 1)
    rgbEnemyLife = (208,   208,   208)
    rgbEnemyDead = (255,   0,   0)
    
    rgbTarget = [rgbEnemyLife, rgbEnemyDead]
    
    # Retorna a localização do pixel se coiciderem com os dados enviados, se não retorna None
    data = findInScreenshot(coordinate, rgbTarget)
    
    
    if (data !=  None):
        
        if (data['rgb'] == (255, 0, 0)):
            return 'isEnemy'
        else:
            return 'isLoot'
    else:
        return None
    
    return isEnemy