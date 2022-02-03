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