class ReadScreen:
    def __init__ (self, aimbot):
        self.aimbot = aimbot

    # Screenshot de um local selecionado e retorna a coordenadas do getpixel
    def findInScreenshot (self, coordinate, rgb):
        # Declarando dados do pixel nas propriedades do aimbot
        self.aimbot.regionToPrint = coordinate
        self.aimbot.rgbWanted = rgb

        # Tira print de uma area especificada nas propriedades do aimbot
        screenshot = self.aimbot.printTarget() 

        # Retorna a localização do pixel q coincide com as propriedades do aimbot, se não for encontrado retorna None
        location = self.aimbot.findRgb(screenshot) 
        return location

    def myLocation (self):
        # Coordenadas da area onde o user pode estar
        coordinate = (800, 200, 400, 350)
        rgb = (255,  57, 255)

        location = self.findInScreenshot(coordinate, rgb)
        return location
    
    def scannerEnemyName (self):
        # Dados do pixel onde fica o enemyName
        coordinate = (1273, 42, 100, 100)
        rgb = (255, 0, 0)

        # Retorna a localização do pixel se coiciderem com os dados enviados, se não retorna None
        enemyLocation = self.findInScreenshot(coordinate, rgb)

        return enemyLocation