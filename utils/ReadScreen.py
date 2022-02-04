class ReadScreen:
    def __init__ (self, aimbot):
        self.aimbot = aimbot

    # Screenshot de um local selecionado e retorna a coordenadas do getpixel
    def findInScreenshot (self, coordinate, rgb):
        # Declarando coordenadas e rgb
        self.aimbot.regionToPrint = coordinate
        self.aimbot.rgbWanted = rgb

        screenshot = self.aimbot.printTarget() 

        location = self.aimbot.findRgb(screenshot) 
        return location

    def myLocation (self):
        # Coordenadas da area onde o user pode estar
        coordinate = (800, 200, 400, 350)
        rgb = (255,  57, 255)

        location = self.findInScreenshot(coordinate, rgb)
        return location
    
    def scannerEnemyName (self):
        # Coordenadas do pixel no name enemy
        coordinate = (1273, 42, 100, 100)
        rgb = (255, 0, 0)

        location = self.findInScreenshot(coordinate, rgb)

        if (location != None):
            print('Is Enemy!!!')
            self.aimbot.isEnemy = True
        else:
            print('Is Not A Enemy')
            self.aimbot.isEnemy = False
            self.aimbot.inFight = False

        # ['isEnemy] == O scanner identificou algum inimigo & ['inFight'] == O aimbot ja está em um kombate
        # obs: Pode parecer q a existencia das duas variavéis são desnessesaria, porém a ordem q é manipulada cada uma, interfere se o aimbot vai iniciar um combate ou se ele ja está em combate e graças a isso, o aimbot se torná mais seguro