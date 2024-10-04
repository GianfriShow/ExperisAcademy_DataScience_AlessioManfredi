import random
from dizionario_armi import armi,danni
from mostra_hp import display_hp_bar

def fighting_game():

    player_hp_current, player_hp_max, npc_hp_current, npc_hp_max = 100,100,100,100

    while player_hp_current > 0 and npc_hp_current > 0:
        print(f'You:\n{display_hp_bar(player_hp_current,player_hp_max)}\nNPC:\n{display_hp_bar(npc_hp_current,npc_hp_max)}')
        print(list(armi.keys()))
        choice = input("Choose your weapon:\n")
        player_dmg = danni(choice)
        npc_dmg = danni(list(armi.keys())[random.choice(range(len(list(armi.keys()))))])
        player_hp_current -= npc_dmg
        npc_hp_current -= player_dmg
    
    if player_hp_current < 0 and npc_hp_current < 0:
        print("Tie: you both died")
    elif player_hp_current < 0:
        print("You died")
    else:
        print("You won")