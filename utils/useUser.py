from time import sleep
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
        print('DANGER: User not found!, click of emmergence!')
        aimbot.clickIn(1100, 340)
    
# Posiciona as arrow para que simplifique o loop do findEnemy
def startPositionArrow ():
    clickMe() 
    aimbot.moveArrow('up')
    aimbot.moveArrow('right')
        
def scannerByArrow (area, updateAimbotToEnemy, skillBuffs):
    direction = ('down', 'left', 'up', 'right') 
    places = 2 # Casas q a seta moverá


    for area in range(1, area): # Numero da area q o espiral vai percorrer
        skillBuffs() 
            
        for index in range(0, len(direction)):
            
            if (area != 1) and (index % 2 == 0):
                places += 1
            
                
            for moves in range(0, places): # Numero de movimentos da ceta
                aimbot.moveArrow(direction[index]) # Isso move a ceta um uma padrão spiral

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
    sleep(.5)
    aimbot.pressButton('enter', hold) # Se for um loot, ja pega o loot
    
    
def openGetCloseLoot ():
    hold = False
    print('Inicio do looteamento')
    
    aimbot.pressButton('enter', hold) # Vá até o loot e abrá
    
    sleep(1) # Espere chegar lá
    
    aimbot.pressButton('enter', hold) # Pegue todo o loot
    
  
    aimbot.pressButton('enter', hold)  # Se posicione em cima do cadaver
    
    sleep(.5) # Espere o aimbot chegar lá
    
    print('fim do looteamento')
        
        
        

    
