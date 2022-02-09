from time import sleep
from modules.Aimbot import aimbot # ERROR: CHAMA O useMain E O useMain também chama o useUser
from utils.useReadScreen import myLocation, watcherLoot, isBagOpen

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
        print('f1')
        aimbot.pressButton('f1', hold)
        
        aimbot.clickIn(1100, 340)
    
# Posiciona as arrow para que simplifique o loop do findEnemy
def startPositionArrow ():       
    clickMe() 
    aimbot.pressButton('up', False)
    aimbot.pressButton('right', False)
        
def scannerByArrow (area, updateAimbotToEnemy, skillBuffs):
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
    aimbot.pressButton('enter', hold) # Inicia confronto
    aimbot.pressButton('enter', hold) # Se tiver 2 em um mesmo bloco, ele atacará o primeiro
    
    
def openGetCloseLoot ():
    hold = False
    print('Inicio do looteamento')
    
    print('enter')
    aimbot.pressButton('enter', hold) # Vá até o loot e abrá
    
    sleep(2) # Espere chegar lá
    
    open = isBagOpen()
    print(open)
    
    if (open == True):
        aimbot.pressButton('right', hold)
        
        for presses in range(0, 2):
            coordinateItem = watcherLoot()
            
            if (coordinateItem != None):
                # Ajustes
                x = coordinateItem['x'] 
                y = coordinateItem['y']
                aimbot.clickIn(x, y)
            else:
                sleep(1)
                print('f1')
                aimbot.pressButton('f1', hold)

                print('1')
                aimbot.pressButton('1', hold)

                print('enter')
                aimbot.pressButton('enter', hold)
  
        
    print('fim do looteamento')
        
        
        

    
