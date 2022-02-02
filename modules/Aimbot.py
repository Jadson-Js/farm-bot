import pyautogui

class Aimbot:
    def __init__(self):
        self.isEnemy = False # Propriedade que identifica se o screenshot é de um inimigo ou não
        self.inFight = False   
                    
    # Tira uma screenshot no pixel no name do enemy   
    def printTarget (self):
        screenshot = pyautogui.screenshot(region=(1273, 42, 1, 1)) # screenshot no local exato
        screenshot.save('images/pixels/enemy-name.png') # Salva img numa pasta
        return screenshot # Envia img para propriedade no constructor
        
     
    # Lerá o conteudo da screenshot     
    def readScreen(self, screenshot):        
        r, g, b = screenshot.getpixel((0, 0)) # Recebe o valores rgb da screenshot

        if (r == 255) and (g == 0) and (b == 0): # Se a screenshot for vermelhay
            self.isEnemy = True
        else: # Se não for vermelha
            self.isEnemy = False # evela na propriedade isEnemy q a screenshot não é de origem inimiga
            self.inFight = False
            
    def atackEnemy (self):
        pyautogui.press('enter') 
        self.inFight = True