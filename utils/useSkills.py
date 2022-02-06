from modules.Aimbot import aimbot

def demage ():
    hold = False
    aimbot.pressButton('1', hold) # Inicia habilidade de dmg
    aimbot.pressButton('1', hold) # Se n houver em batalha, finaliza ela

def demageArea ():
    pass

def healer ():
    hold = True
    aimbot.pressButton('2', hold) # Auto cura

def healerArea ():
    pass

def defense ():
    hold = True
    aimbot.pressButton('w', hold) # Auto proteção de def
    
def summon ():
    hold = False
    aimbot.pressButton('q', hold) # Summona lacaio