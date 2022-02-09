from modules.Aimbot import aimbot

# Screenshot de um local selecionado e retorna a coordenadas do getpixel
def findInScreenshot (coordinate, rgbTargets):
    # Declarando dados do pixel nas propriedades do aimbot
    # Tira print de uma area especificada nas propriedades do aimbot
    screenshot = aimbot.printTarget(coordinate) 
    # Retorna a localização do pixel q coincide com as propriedades do aimbot, se não for encontrado retorna None
    data = aimbot.findRgb(screenshot, coordinate, rgbTargets) 
    
    return data

# (Leitura de tela) Verifica se no camto superior esquerdo, há a indicação de um inimigo
def watcherTarget (): 
    # Dados do pixel
    coordinate = (1269, 39, 1, 1)
    # Rgb alvos
    rgbEnemyLife = (208,   208,   208)
    rgbEnemyDead = (255,   0,   0)
    
    rgbTargets = [rgbEnemyLife, rgbEnemyDead] 
    
    # Retorna a localização do pixel se coiciderem com os dados enviados, se não retorna None
    data = findInScreenshot(coordinate, rgbTargets)
    
    
    if (data !=  None):
        
        if (data['rgb'] == (255, 0, 0)):
            return 'isEnemy'
        else:
            return 'isLoot'
    else:
        return None
    
def isBagOpen ():
    # Dados do pixel
    coordinate = (932, 220, 1, 1)
    # Rgb alvos
    rgbOpen = [( 90, 239,  74)]
   
    # Retorna a localização do pixel se coiciderem com os dados enviados, se não retorna None
    data = findInScreenshot(coordinate, rgbOpen)
    print(data)

    if (data !=  None):
        return True
    else:
        return False
    
def watcherLoot ():
    # Dados do pixel
    coordinate = (990, 220, 10, 10)
    # Rgb alvos
    rgbGold = (255, 255,  57)
    rgbImundice = (198, 181,  82)
    
    rgbLoots = [rgbGold, rgbImundice] 
    
    # Retorna a localização do pixel se coiciderem com os dados enviados, se não retorna None
    data = findInScreenshot(coordinate, rgbLoots)
    print(data)
    
    return data
    
def myLocation ():
    # Coordenadas da area onde o user pode estar
    coordinate = (880, 30, 465, 564) 
    rgbTargets = [(255,  57, 255)]
    data = findInScreenshot(coordinate, rgbTargets)
    return data