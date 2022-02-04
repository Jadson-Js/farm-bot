class Main:
    def __init__ (self, aimbot, useUser, useReadScreen):
        self.aimbot = aimbot
        self.useUser = useUser
        self.useReadScreen = useReadScreen
        
    # Atualiza as propriedades 'inFight' e 'isEnemy' do aimbot
    def updateAimbotToEnemy(self):
        # Vai scannear o local onde fica o nome do inimigo
        enemyLocation = self.useReadScreen.scannerEnemyName() # Se um enemy for identificado, retorna as coordenadas do pixel scanneado se não 'None'
        
        # Atualizando as propriedades
        if (enemyLocation != None):
            self.aimbot.isEnemy = True
        else:
            self.aimbot.isEnemy = False
            self.aimbot.inFight = False
            
    def findEnemy(self):
        self.useUser.scannerByArrow()
            
    # Inicia luta e atualiza propriedade como 'inFight'
    def fight (self):
        self.useUser.startFight() 
        self.aimbot.inFight = True
    
        