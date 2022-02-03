import pyautogui

pyautogui.PAUSE = 1

class Aimbot:
    def __init__(self):
        self.isEnemy = False
        self.inFight = False   
        self.regionToPrint = None
        self.rgbWanted = None
                    
    # Screenshot de uma região selecionada        
    def printTarget (self):
        screenshot = pyautogui.screenshot(region=self.regionToPrint) 
        screenshot.save('images/pixels/target.png') 
        return screenshot
    
   # Encontra um pixel com determido rgb e retorna as cordenadas
    def findRgb(self, screenshot):   
        width, height = screenshot.size
        stop = False # Quando for verdadeira, cancela os loopings
        
        # Percorrendo toda area do screenshot
        for x in range(0, width): 
            if (stop == True):
                break
            else:
                for y in range(0, height):    
                    if (stop == True):
                        break
                    else:    
                        
                        r, g, b = screenshot.getpixel((x, y)) # Pega o rgb do pixel onde o looping está passando.

                        if (r == self.rgbWanted[0]) and (g == self.rgbWanted[1]) and (b == self.rgbWanted[2]):
                            stop = True
                            return {'x': self.regionToPrint[0] + x, 'y': self.regionToPrint[1] + y}
                        else:
                            continue
        else:
            return None

    def atackEnemy (self):
        pyautogui.press('enter') 
        self.inFight = True
        
    def clickIn (self, x, y):
        pyautogui.click(x, y)
        
    def moveArrow (self, direction, places):
        for presses in range(0, places):
            pyautogui.press(direction)
        
    def startPositionArrow (self):
        self.moveArrow('left', 1)
        self.moveArrow('up', 1)
        