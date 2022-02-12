from time import sleep
from modules.Aimbot import aimbot # ERROR: CHAMA O useMain E O useMain também chama o useUser
from utils.useReadScreen import myLocation, watchValueItem, watchLootOpen, watchMenuOpen

# Clica no user
def clickMe ():
    print('clickMe()')
    
    data = myLocation() # Coordenadas de sua localização atual
    if (data != None):
        # Ajustes
        x = data['x'] + 2
        y = data['y'] + 7
        aimbot.clickIn(x, y)
    else:
        print('DANGER: User not found!, click of emmergence!')
        
        if (watchLootOpen() == True):
            getCloseLoot()
        
        aimbot.clickIn(1049, 359)
        
    print(';')
    
# Posiciona as arrow para que simplifique o loop do scannerByArrow
def startPositionArrow ():      
    print('startPositionArrow()')
    
    needEject()
    
    clickMe() 
    
    print("press('up')")
    aimbot.pressButton('up', False)
    
    print("press('right')")
    aimbot.pressButton('right', False)
    
    print(';')
        
# Movimenta as setas em um spiral (Filho do findEnemy)
def scannerByArrow (area, updateAimbotToEnemy, skillBuffs):
    print('scannerByArrow()')
    
    needEject()
    
    hold = False
    direction = ('down', 'left', 'up', 'right') 
    places = 2 # Casas q a seta moverá
    
    for area in range(1, area): # Numero da area q o espiral vai percorrer
            
        for index in range(0, len(direction)):
            
            if (area != 1) and (index % 2 == 0):
                places += 1
                skillBuffs() 
            
                
            for moves in range(0, places): # Numero de movimentos da ceta
                print(f'direction: {direction[index]}')
                aimbot.pressButton(direction[index], hold) # Isso move a ceta um uma padrão spiral

                # Atualizando o aimbot a cada movimento do espiral
                updateAimbotToEnemy() 
                
                if (aimbot.isEnemy == True) or (aimbot.isLoot == True):
                    return
                else:
                    continue
                
    print(';')
             
# Inicia o a luta, dando enter no inimigo   
def startFight ():
    print('startFight()')
    
    hold = False
    
    needEject()
    
    print(f"press('enter')")
    aimbot.pressButton('enter', hold) # Inicia confronto
    sleep(.5)
    
    needEject()
        
    print(f"press('enter')")
    aimbot.pressButton('enter', hold) # Se tiver 2 em um mesmo bloco, ele atacará o primeiro
    
    print(';')
         
# Abri o loot, apertando enter e esperando o user chegar no cadaver e abrir o loot 
def openLoot ():
    print('openLoot()')
    hold = False
    
    needEject()
    
    print(f"press('enter')")
    aimbot.pressButton('enter', hold) # Vá até o loot e abrá
    
    sleep(2) # Espere chegar lá
    
    print(';')
    
# Pega somente os itens valiosos, fecha o loot e se movimenta para cima do cadaver (para scannerByArrow não ser ativado novamente).
def getCloseLoot ():
    print('getCloseLoot()')
    
    hold = False
    
    print(f"press('right')")
    aimbot.pressButton('right', hold)
        
    for presses in range(0, 2):
        coordinateItem = watchValueItem()
        print(f'Is Value Item: {coordinateItem}')
        
        if (coordinateItem != None):
            # Ajustes
            x = coordinateItem['x'] 
            y = coordinateItem['y']
            print(f"aimbot.clickIn({x}, {y})")
            aimbot.clickIn(x, y)
        else:     
            print(f"press('f1')")
            aimbot.pressButton('f1', hold)
    else:
        
        needEject()
                
        print(f"press('5')")
        aimbot.pressButton('5', hold)
        
        print(f"press('enter')")
        aimbot.pressButton('enter', hold)
        
        needEject()
        
    print(';')
    
def needEject ():
    isLootOpen = watchLootOpen()
    
    if (isLootOpen == True):
        print('Ejected')
        getCloseLoot()
    
    hold = False
    isMenuOpen = watchMenuOpen()
    
    if (isMenuOpen == True):
        print('Ejected')
        print(f"press('f1')")
        aimbot.pressButton('f1', hold)
    

#print('fim do looteamento')
        
        
        

    
