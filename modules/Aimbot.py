import pyautogui

class Aimbot:
    def __init__(self):
        self.isEnemy = False
        self.inFight = False   
        self.regionPrint = None
        self.rgbWanted = None
                    
    # Screenshot de uma região selecionada        
    def printTarget (self):
        screenshot = pyautogui.screenshot(region=self.regionPrint) 
        screenshot.save('images/pixels/enemy-name.png') 
        return screenshot
    
   # Encontra um pixel com determido rgb e retorna as cordenadas
    def findRgb(self, screenshot):   
        width, height = screenshot.size
        stop = False # Quando for verdadeira, cancela os loopings
        
        for x in range(0, width):
            if (stop == True):
                break
            else:
                for y in range(0, height):    
                    if (stop == True):
                        break
                    else:    
                        
                        r, g, b = screenshot.getpixel((x, y)) 

                        if (r == self.rgbWanted[0]) and (g == self.rgbWanted[1]) and (b == self.rgbWanted[2]):
                            stop = True
                            return {'x': self.regionPrint[0] + x, 'y': self.regionPrint[1] + y}
                        else:
                            return None

    def atackEnemy (self):
        pyautogui.press('enter') 
        self.inFight = True