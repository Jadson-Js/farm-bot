from modules.Aimbot import Aimbot 

aimbot = Aimbot()

# Lê o pixel onde fica o nome enemy e retorna os dados em um dicionario contendo: 
def scannerToAtack ():
    # Aqui é declarado a região que o scanner vai procurar o pixel alvo
    aimbot.regionPrint = (1273, 42, 1, 1)
    aimbot.rgbWanted = [255, 0, 0]
    
    screenshot = aimbot.printTarget() 
    
    location = aimbot.findRgb(screenshot) 
    
    if (location != None):
        print(f'coordinates: {location}')
        aimbot.isEnemy = True
    else:
        aimbot.isEnemy = False
        aimbot.inFight = False
    
    # ['isEnemy] == O scanner identificou algum inimigo & ['inFight'] == O aimbot ja está em um kombate
    return {'isEnemy': aimbot.isEnemy, 'inFight': aimbot.inFight}    
    # obs: Pode parecer q a existencia das duas variavéis são desnessesaria, porém a ordem q é manipulada cada uma, interfere se o aimbot vai iniciar um combate ou se ele ja está em combate e graças a isso, o aimbot se torná mais seguro

def atack ():
    aimbot.atackEnemy()