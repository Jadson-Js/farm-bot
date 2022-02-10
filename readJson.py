import json

with open('data/pixels.json') as f:
    entrada = json.load(f)
    
print(entrada['targetEnemy'])