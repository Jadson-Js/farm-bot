from time import sleep
from modules.Aimbot import aimbot # ERROR: CHAMA O useMain E O useMain também chama o useUser
from utils.useReadScreen import myLocation, watcherLoot, isLootOpen

# Clica no user
def clickMe ():
    hold = False
    
    data = myLocation() # Coordenadas de sua localização atual
    if (data != None):
        # Ajustes
        x = data['x'] + 2
        y = data['y'] + 7
        aimbot.clickIn(x, y)
    else:
        print('DANGER: User not found!, click of emmergence!')
        
        if (isLootOpen() == True):
            getCloseLoot()
        
        aimbot.clickIn(1049, 359)
    
# Posiciona as arrow para que simplifique o loop do findEnemy
def startPositionArrow ():      
    clickMe() 
    
    if (isLootOpen() == True):
        getCloseLoot()
    
    aimbot.pressButton('up', False)
    aimbot.pressButton('right', False)
        
def scannerByArrow (area, updateAimbotToEnemy, skillBuffs):
    if (isLootOpen() == True):
        getCloseLoot()
    
    hold = False
    direction = ('down', 'left', 'up', 'right') 
    places = 2 # Casas q a seta moverá
    
    for area in range(1, area): # Numero da area q o espiral vai percorrer
            
        for index in range(0, len(direction)):
            
            if (area != 1) and (index % 2 == 0):
                places += 1
                skillBuffs() 
            
                
            for moves in range(0, places): # Numero de movimentos da ceta
                aimbot.pressButton(direction[index], hold) # Isso move a ceta um uma padrão spiral

                # Atualizando o aimbot a cada movimento do espiral
                updateAimbotToEnemy() 
                
                if (aimbot.isEnemy == True) or (aimbot.isLoot == True):
                    return
                else:
                    continue
                
def startFight ():
    hold = False
    
    if (isLootOpen() == True):
        getCloseLoot()
    
    print('enter')
    aimbot.pressButton('enter', hold) # Inicia confronto
    
    if (isLootOpen() == True):
        getCloseLoot()
    
    print('enter')
    aimbot.pressButton('enter', hold) # Se tiver 2 em um mesmo bloco, ele atacará o primeiro

          
def openLoot ():
    hold = False
    print('Inicio do looteamento')
    
    if (isLootOpen() == True):
        getCloseLoot()

    print('enter')
    aimbot.pressButton('enter', hold) # Vá até o loot e abrá
    
    if (isLootOpen() == False):
        print('enter')
        aimbot.pressButton('enter', hold)
    
    sleep(2) # Espere chegar lá
    
def getCloseLoot ():
    hold = False
    
    print('right')
    aimbot.pressButton('right', hold)
        
    for presses in range(0, 2):
        coordinateItem = watcherLoot()
        print(f'Is Value Item: {coordinateItem}')
        
        if (coordinateItem != None):
            # Ajustes
            x = coordinateItem['x'] 
            y = coordinateItem['y']
            aimbot.clickIn(x, y)
        
    print('f1')
    aimbot.pressButton('f1', hold)
    
    
    
    print('1')
    aimbot.pressButton('1', hold)
    
    print('enter')
    aimbot.pressButton('enter', hold)
    
    if (isLootOpen() == True):
        getCloseLoot()
        

#print('fim do looteamento')
        
        
        

    
