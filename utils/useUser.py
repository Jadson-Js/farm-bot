from time import sleep
from modules.Aimbot import aimbot # ERROR: CHAMA O useMain E O useMain também chama o useUser
from utils.useReadScreen import myLocation, counterValuesItems

# Clica no user
def clickMe ():
    data = myLocation() # Coordenadas de sua localização atual
    if (data != None):
        # Ajustes
        x = data['x'] + 2
        y = data['y'] + 7
        aimbot.clickIn(x, y)
    else: 
        print('DANGER: User not found!, click of emmergence!')
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
        skillBuffs() 
            
        for index in range(0, len(direction)):
            
            if (area != 1) and (index % 2 == 0):
                places += 1
            
                
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
    sleep(.5)
    aimbot.pressButton('enter', hold) # Se for um loot, ja pega o loot
    
    
def openGetCloseLoot ():
    hold = False
    print('Inicio do looteamento')
    
    print('enter')
    aimbot.pressButton('enter', hold) # Vá até o loot e abrá
    
    sleep(1) # Espere chegar lá
    
    # (Agora com a bag aberta)
   
    amount = counterValuesItems()
    print(amount)
    
    # (Sabendo a quantidade de itens)
    # moveArrow pra direira
    # click a quantidade de itens
    print('right')
    aimbot.pressButton('right', hold)
    
    for presses in range(0, amount):
        sleep(.5)
        print('enter')
        aimbot.pressButton('enter', hold)
    
    # (E para fechar a bag)
    # Aperte 'f1'
    sleep(.5)
    print('f1')
    aimbot.pressButton('f1', hold)
    
    print('fim do looteamento')
        
        
        

    
