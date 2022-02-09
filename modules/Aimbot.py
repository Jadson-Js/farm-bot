import pyautogui

pyautogui.PAUSE = .2

class Aimbot:
    def __init__(self):
        self.isEnemy = False
        self.inFight = False 
        self.isLoot = False  


    # Screenshot de uma região selecionada        
    def printTarget (self, coordinate):
        screenshot = pyautogui.screenshot(region=coordinate) 
        screenshot.save('images/pixels/target.png') 
        return screenshot
    
   # Encontra um pixel com determido rgb e retorna as cordenadas
    def findRgb(self, screenshot, coordinate, rgbTargets):   
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

                        for rgbTarget in rgbTargets: # Percorre os rgb alvos
                            
                            if (r == rgbTarget[0]) and (g == rgbTarget[1]) and (b == rgbTarget[2]):
                                stop = True
                                return {'x': coordinate[0] + x, 'y': coordinate[1] + y, 'rgb': (r, g, b)}
                            else:
                                continue
        else:
            return None
    
    # Pressiona uma keyword
    def pressButton (self, button, hold):
        if (hold == True): # Deve pressiona o button indicado + 'alt'
            with pyautogui.hold('alt'):
                pyautogui.press(button) 
        else: # Se não so preciona mesmo
            pyautogui.press(button) 
        
    # Clicka em uma coordenada indicada
    def clickIn (self, x, y):
        pyautogui.click(x, y)
        
aimbot = Aimbot()