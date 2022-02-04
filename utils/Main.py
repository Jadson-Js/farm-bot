from utils.User import User # Class com funções q agirão diretamente com o aimbot.  
from utils.ReadScreen import ReadScreen # Class com funções especificas para leitura de tela.

class Main:
    def __init__ (self, aimbot):
        self.aimbot = aimbot
        self.useUser = User(aimbot, self)
        self.useReadScreen = ReadScreen(aimbot)
        
    # Atualiza as propriedades 'inFight' e 'isEnemy' do aimbot
    def updateAimbotToEnemy(self):
        # Vai scannear o local onde fica o nome do inimigo
        enemyLocation = self.useReadScreen.scannerEnemyName() # Se um enemy for identificado, retorna as coordenadas do pixel scanneado se não 'None'
        
        # Atualizando as propriedades
        if (enemyLocation != None):
            print('Is An Enemy')
            self.aimbot.isEnemy = True
        else:
            print('Is Not A Enemy')
            self.aimbot.isEnemy = False
            self.aimbot.inFight = False
            
    def findEnemy(self):
        self.useUser.scannerByArrow()
            
    # Inicia luta e atualiza propriedade como 'inFight'
    def fight (self):
        self.useUser.startFight() 
        self.aimbot.inFight = True
    
        