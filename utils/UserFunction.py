from utils.ReadScreen import ReadScreen

class UserFunctions:
    def __init__ (self, aimbot):
        self.aimbot = aimbot
        self.readScreen = ReadScreen(aimbot)

    # Clica no user.
    def clickMe (self):
        coordinate = self.readScreen.myLocation()
        if (coordinate != None):
            x = coordinate['x']
            y = coordinate['y'] + 7
            self.aimbot.clickIn(x, y)
        else:
            return

    def startPositionArrow (self):
        self.clickMe() 
        self.aimbot.moveArrow('up', 1)
        self.aimbot.moveArrow('right', 1)


    def findEnemy (self):
        self.startPositionArrow()

        direction = ('down', 'left', 'up', 'right')

        #FIRST CICLE
        for index in range(0, len(direction)):
            self.aimbot.moveArrow(direction[index], 2)

    def atack (self):
        self.aimbot.atackEnemy()
