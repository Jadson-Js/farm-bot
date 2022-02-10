import json
from modules.Aimbot import aimbot

with open('data/pixels.json') as f:
    dataPixel = json.load(f)

# Screenshot de um local selecionado e retorna a coordenadas do getpixel
def findInScreenshot (coordinate, rgbTargets):
    print(coordinate, rgbTargets)
    # Declarando dados do pixel nas propriedades do aimbot
    # Tira print de uma area especificada nas propriedades do aimbot
    screenshot = aimbot.printTarget(coordinate) 
    # Retorna a localização do pixel q coincide com as propriedades do aimbot, se não for encontrado retorna None
    data = aimbot.findRgb(screenshot, coordinate, rgbTargets) 
    
    return data

# (Leitura de tela) Verifica se no camto superior esquerdo, há a indicação de um inimigo
def watcherTarget (): 
    # Dados do pixel
    coordinate = tuple(dataPixel['target']['region']) # (1269, 39, 1, 1)
    # Rgb alvos
    rgbEnemyLife = tuple(dataPixel['target']['rgbEnemyLife']) # (208,   208,   208)
    rgbEnemyDead = tuple(dataPixel['target']['rgbEnemyDead']) # (255,   0,   0)
    
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
    
# Verifica se o loot está aberto
def watchLootOpen ():
    # Dados do pixel
    coordinate = tuple(dataPixel['isLootOpen']['region'])  # (932, 220, 1, 1)
    # Rgb alvos
    rgbOpen = [tuple(dataPixel['isLootOpen']['rgb'])] # [( 90, 239,  74)]
   
    # Retorna a localização do pixel se coiciderem com os dados enviados, se não retorna None
    data = findInScreenshot(coordinate, rgbOpen)

    if (data !=  None):
        print('Loot está aberto')
        return True
    else:
        print('Loot não está aberto.')
        return False
    
# Verifica se há itens valiosos no loot
def watchValueItem ():
    # Dados do pixel
    coordinate = tuple(dataPixel['isValueItem']['region']) # (990, 220, 1, 1)
    # Rgb alvos
    rgbGold = tuple(dataPixel['isValueItem']['rgbGold']) # (255, 255,  57)
    rgbImundice = tuple(dataPixel['isValueItem']['rgbImundice']) # (198, 181,  82)
    
    rgbLoots = [rgbGold, rgbImundice] 
    
    # Retorna a localização do pixel se coiciderem com os dados enviados, se não retorna None
    data = findInScreenshot(coordinate, rgbLoots)
    
    return data

# Verifica se o menu do game está aberto
def watchMenuOpen (): 
    # Dados do pixel
    coordinate = tuple(dataPixel['isMenuOpen']['region']) # (726, 470, 1, 1)
    # Rgb alvos
    rgbMenu = [tuple(dataPixel['isMenuOpen']['rgb'])] # [(238, 238, 187)] 
    
    # Retorna a localização do pixel se coiciderem com os dados enviados, se não retorna None
    data = findInScreenshot(coordinate, rgbMenu)
    
    if (data !=  None):
        print('Menu está aberto.')
        return True
    else:
        print('Menu não está aberto.')
        return False
    
# Retorna as coordenadas do user
def myLocation ():
    # Coordenadas da area onde o user pode estar
    coordinate = tuple(dataPixel['myLocation']['region']) # (880, 30, 465, 564) 
    rgbTargets = [tuple(dataPixel['myLocation']['rgb'])] # [(255,  57, 255)]
    data = findInScreenshot(coordinate, rgbTargets)
    return data