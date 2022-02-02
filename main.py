from utils.utils import scannerToAtack, atack

while (True):
    mustAtack = scannerToAtack()
    print (mustAtack)
    
    if (mustAtack['inFight'] == True): # Se estiver no modo fight, apenas resete o loop
        continue
    
    if(mustAtack['isEnemy'] == True): # Se Não estiver em modo de luta, ataca o enemy e ativa modo luta
        atack()