import pyautogui

class StartFight:
    def __init__(self):
        self.screenshot = None # Propriedade que conteim a img com o pixel no nome do enemy
        self.isEnemy = False # Propriedade que identifica se o screenshot é de um inimigo ou não
        self.inFight = False # Propriedade q indica se o aimbot está em combate
            
            
    # Tira uma screenshot no pixel no name do enemy   
    def printTarget (self):
        screenshot = pyautogui.screenshot(region=(1273, 42, 1, 1)) # screenshot no local exato
        screenshot.save('images/pixels/enemy-name.png') # Salva img numa pasta
        self.screenshot = screenshot # Envia img para propriedade no constructor
        
     
    # Lerá o conteudo da screenshot     
    def readData(self):        
        r, g, b = self.screenshot.getpixel((0, 0)) # Recebe o valores rgb da screenshot

        if (r == 255) and (g == 0) and (b == 0): # Se a screenshot for vermelha
            print('Enemy identify') 
            self.isEnemy = True # Revela na propriedade isEnemy q a screenshot é de origem inimiga
        else: # Se não for vermelha
            print('Is Not A Enemy')
            self.isEnemy = False # evela na propriedade isEnemy q a screenshot não é de origem inimiga
            # Ja que quando o aimbot está lutando, eh revelado o status do enemy 
            self.inFight = False # como n tem o status, a propriedade 'inFight' é dada como falsa
         
    # Inicia modo de fight
    def atackEnemy (self):
        pyautogui.press('enter') # Ataca o enemy
        self.inFight = True # Propriedade é dada como verdadeira