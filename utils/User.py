class User:
    def __init__ (self, aimbot, useReadScreen):
        self.aimbot = aimbot
        self.useReadScreen = useReadScreen

    # Clica no user
    def clickMe (self):
        coordinate = self.useReadScreen.myLocation() # Coordenadas de sua localização atual
        if (coordinate != None):
            # Ajustes
            x = coordinate['x'] + 2
            y = coordinate['y'] + 7
            self.aimbot.clickIn(x, y)
        else:
            print('DANGER: User not found!')
            return

    # Posiciona as arrow para que simplifique o loop do findEnemy
    def startPositionArrow (self):
        self.clickMe() 
        self.aimbot.moveArrow('up')
        self.aimbot.moveArrow('right')

 
    # Vai procurar o inimigo envolta do user
    def scannerByArrow (self):
        # Posicionando a arrow
        self.startPositionArrow()

        direction = ('down', 'left', 'up', 'right')

        # Primeiro ele vai percorrer as direções da arrow. ex: baixo, esquerda...
        for index in range(0, len(direction)):   
            # E cada direção percorrida
            for x in range(0, 2): #  Realize essa operação por esse numero de vezes
                # Mova a ceta para direção seleciona ex: esquerda
                self.aimbot.moveArrow(direction[index]) 
                
                
                
                        
    def startFight (self):
        self.aimbot.atack()
