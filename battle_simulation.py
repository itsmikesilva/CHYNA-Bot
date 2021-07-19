from pokebattle import Battle
from pokebattle import Pokemon
import pickle
import difflib

def load_obj(name, foldername):
    with open(foldername + '\\' + name + '.pkl', 'rb') as f: 
        return pickle.load(f)

replay = load_obj("1376791337", "replays")
team1 = {}
team2 = {}
for p in replay[0]:
    if "-*" in p:
        p = p.split("-*")[0]
        team1[p] = Pokemon(p)
    else:
        team1[p] = Pokemon(p)
for p in replay[1]:
    if "-*" in p:
        p = p.split("-*")[0]
        team2[p] = Pokemon(p)
    else:
        team2[p] = Pokemon(p)

#TURN 0
count_player_team = 0
count_opposing_team = 0
picked_player_team = []
picked_opposing_team = []

for turn in replay[2]:
    for actions in turn:
        for action in actions:
            if "Go!" in action and count_player_team < 2:
                pokemon = action.split(" ", 1)[1]
                pokemon = pokemon[:-1]
                picked_player_team.append(pokemon)
                count_player_team += 1
            if "sent out" in action and count_opposing_team < 2:
                pokemon = action.split(" sent out ")[1]
                pokemon = pokemon[:-1]
                picked_opposing_team.append(pokemon)
                count_opposing_team += 1

battle = Battle()
battle.player_team = team1
battle.opposing_team = team2
battle.picked_player_team = picked_player_team
battle.picked_opposing_team = picked_opposing_team
battle.pokemon_field_1 = picked_player_team[0]
battle.pokemon_field_2 = picked_player_team[1]
battle.opposing_pokemon_field_1 = picked_opposing_team[0]
battle.opposing_pokemon_field_2 = picked_opposing_team[1]
print("Full player team: ", battle.player_team)
print("Full opposing team: ", battle.opposing_team)
print("Picked player team: ", battle.picked_player_team)
print("Picked opposing team: ", battle.picked_opposing_team)
print("Player Team Pokemon in Field 1: ", battle.pokemon_field_1)
print("Player Team Pokemon in Field 2: ", battle.pokemon_field_2)
print("Opposing Team Pokemon in Field 1: ", battle.opposing_pokemon_field_1)
print("Opposing Team Pokemon in Field 2: ", battle.opposing_pokemon_field_2)

turnos_list = []
temp_fainted_player = []
temp_fainted_opposing = []
fainted_player_mons = []
fainted_opposing_mons = []
count10 = 1
for turn in replay[2]:
    for actions in turn:
        if "withdrew" in actions[0]:
            switch_out_action_op = actions[0].split(" withdrew ")
            withdrawn_pokemon_op = switch_out_action_op[1][:-1]
            if "sent out" in actions[1]:
                switch_in_action_op = actions[1].split(" sent out ")
                entering_pokemon_op = switch_in_action_op[1][:-1]
                if withdrawn_pokemon_op == battle.opposing_pokemon_field_1: 
                    battle.opposing_pokemon_field_1 = entering_pokemon_op
                    if entering_pokemon_op not in battle.picked_opposing_team:
                        battle.picked_opposing_team.append(entering_pokemon_op)
                        alive_opposing_team.append(entering_pokemon_op)
                elif withdrawn_pokemon_op == battle.opposing_pokemon_field_2:
                    battle.opposing_pokemon_field_2 = entering_pokemon_op
                    if entering_pokemon_op not in battle.picked_opposing_team:
                        battle.picked_opposing_team.append(entering_pokemon_op)
                        alive_opposing_team.append(entering_pokemon_op)
                else:
                    continue
        if "come back" in actions[0]:
            switch_out_action_player = actions[0].split(", ")
            withdrawn_pokemon_player = switch_out_action_player[0]        
            if "Go!" in actions[1]:
                switch_in_action_player = actions[1].split("Go! ")
                entering_pokemon_player = switch_in_action_player[1][:-1]
                if withdrawn_pokemon_player == battle.pokemon_field_1: 
                    battle.pokemon_field_1 = entering_pokemon_player
                    if entering_pokemon_player not in battle.picked_player_team:
                        battle.picked_player_team.append(entering_pokemon_player)
                elif withdrawn_pokemon_player == battle.pokemon_field_2:
                    battle.pokemon_field_2 = entering_pokemon_player
                    if entering_pokemon_player not in battle.picked_player_team:
                        battle.picked_player_team.append(entering_pokemon_player)                        
                else:
                    continue
        if "opposing" in actions[0] and "fainted!" in actions[0]:
            fainted_op = actions[0].split(" opposing ")
            fainted_opposing_pokemon = fainted_op[1].split(" ")[0]
            temp_fainted_opposing.append(fainted_opposing_pokemon)
        if "sent out" in actions[0]:
            entering_pokemon_op = actions[0].split(" sent out ")[1][:-1] #meter o bicho q entra
            if(len(temp_fainted_opposing) > 0):     #se ele tiver algum fainted pokemon p substituir (à partida tem)
                cur_fainted_op = temp_fainted_opposing[0] #isto vai ter a string "Ho-oh"
                alive_opposing_team.remove(cur_fainted_op)
                if cur_fainted_op == battle.opposing_pokemon_field_1:
                    battle.opposing_pokemon_field_1 = entering_pokemon_op
                    if entering_pokemon_op not in battle.picked_opposing_team:
                        battle.picked_opposing_team.append(entering_pokemon_op)
                elif cur_fainted_op == battle.opposing_pokemon_field_2:
                    battle.opposing_pokemon_field_2 = entering_pokemon_op
                    if entering_pokemon_op not in battle.picked_opposing_team:
                        battle.picked_opposing_team.append(entering_pokemon_op)
                del temp_fainted_opposing[0]

        '''
        else:
            if len(temp_fainted_opposing) > 0:
                cur_fainted_op = temp_fainted_opposing[0]
                if cur_fainted_op == battle.opposing_pokemon_field_1:
                    battle.opposing_pokemon_field_1 = "EMPTY"
                elif cur_fainted_op == battle.opposing_pokemon_field_2:
                    battle.opposing_pokemon_field_2 = "EMPTY"
        '''
        if "opposing" not in actions[0] and "fainted!" in actions[0]:
            fainted_player = actions[0].split(" ")[0]
            temp_fainted_player.append(fainted_player)
        if "Go!" in actions[0]:
            entering_pokemon_player = actions[0].split(" ")[1][:-1]
            if len(temp_fainted_player) > 0:
                cur_fainted_player = temp_fainted_player[0]
                alive_player_team.remove(cur_fainted_op)
                if cur_fainted_player == battle.pokemon_field_1:
                    battle.pokemon_field_1 = entering_pokemon_player
                    if entering_pokemon_player not in battle.picked_player_team:
                        battle.picked_player_team.append(entering_pokemon_player)
                elif cur_fainted_player == battle.pokemon_field_2:
                    battle.pokemon_field_2 = entering_pokemon_player
                    if entering_pokemon_player not in battle.picked_player_team:
                        battle.picked_player_team.append(entering_pokemon_player)

        for action in actions:
            if "used" in action and "opposing" in action:
                action_result = action.split("The opposing ")[1].split(" used ") 
                pokemon_name = action_result[0]
                pokemon_move = action_result[1][:-1]
                if pokemon_move not in battle.opposing_team[pokemon_name].moves:
                    battle.opposing_team[pokemon_name].moves.append(pokemon_move)

            if "used" in action and "opposing" not in action:
                action_result = action.split(" used ") 
                pokemon_name = action_result[0]
                name_compare = difflib.get_close_matches(pokemon_name, battle.player_team.keys())
                if len(name_compare) > 0:
                    pokemon_move = action_result[1][:-1]
                    if pokemon_move not in battle.player_team[name_compare[0]].moves:
                        battle.player_team[name_compare[0]].moves.append(pokemon_move)

            if "lost" in action and "opposing" not in action:
                action_result = action.split(" lost ")
                pokemon_name = action_result[0][1:]
                name_compare = difflib.get_close_matches(pokemon_name, battle.player_team.keys())
                if len(name_compare) > 0:
                    hp_lost = action_result[1].split("%")[0]
                    hp_lost = int(hp_lost)
                    if battle.player_team[name_compare[0]].health > 0:
                        battle.player_team[name_compare[0]].health = battle.player_team[name_compare[0]].health - hp_lost
                    battle.player_team[name_compare[0]]

            if "lost" in action and "opposing" in action:
                action_result = action.split(" lost ")
                pokemon_name = action_result[0].split("The opposing ")[1]
                hp_lost = action_result[1].split("%")[0]
                hp_lost = int(hp_lost)
                if battle.opposing_team[pokemon_name].health > 0:
                    battle.opposing_team[pokemon_name].health = battle.opposing_team[pokemon_name].health - hp_lost

    print("Turn %d" % count10)
    count10 += 1          
    print()
    turnos_list.append(battle.getCopy())

count1 = 0
count2 = 0

for battle_item in turnos_list:
    for i in battle_item.opposing_team.keys():
        print("Turn %d" % count1)
        #print("OPPOSING TEAM")
        print(battle_item.opposing_team[i].name)
        #print(battle_item.opposing_team[i].name + "'s moves: ")
        print(battle_item.opposing_team[i].moves)
        #print(battle_item.opposing_team[i].name + "'s health: ")
        print(battle_item.opposing_team[i].health)
        print()
    for j in battle_item.player_team.keys():
        print("Turn %d" % count2)
        #print("PLAYER TEAM")
        print(battle_item.player_team[j].name)
        #print(battle_item.player_team[j].name + "'s moves: ")
        print(battle_item.player_team[j].moves)
        #print(battle_item.player_team[j].name + "'s health: ")
        print(battle_item.player_team[j].health)
        print()
    count1 += 1
    count2 += 1

count4 = 1
for battle_item in turnos_list:
    print("Beginning of Turn %d" % count4)
    print(battle_item.pokemon_field_1)
    print(battle_item.pokemon_field_2)
    print(battle_item.opposing_pokemon_field_1)
    print(battle_item.opposing_pokemon_field_2)
    print()
    count4 += 1

print("PLAYER TEAM: ")
print(battle_item.picked_player_team)
print("OPPOSING TEAM: ")
print(battle_item.picked_opposing_team)
'''
Go! x -> Beginning of Game, Player Team
p sent out x! -> Beginng of Game, Opposing Team
x, come back! Go! y! -> Switch-out for player team
Withdrew x! w sent out y! -> Switch-out for opposing team
(x lost n% of its health!)
(The opposing x lost n% of its health!)
x used y! (The opposing w lost n% of its health)
x used y! It's not very effective/It's super effective! (The opposing w lost n% of its health)
x used y! It's not very effective on the opposing w! -> Double target moves
x used y! It's super effective on the opposing w! -> Double target moves
x used y! The opposing w avoided the attack!
x used y! A critical hit on w! (The opposing w lost n% of its health!)
x used y! It's not very effective.../It's super effective! A critical hit! (The opposing w lost %n of its health)
The opposing x used y! (w lost n% of its health)
The opposing x used y! A critical hit on w! (w lost n% of its health!)
The opposing x used y! It's not very effective.../It's super effective! (w lost n% of its health!)
The opposing x used y! It's not very effective.../It's super effective! A critical hit on w! (w lost n% of its health!)
x's y -> Player team ability activating
The opposing x's y fell!
x's y fell!
x's y fell harshly!
x fainted!
The opposing x fainted!

If move = Follow Me or Rage Powder: x became the center of attention!
If move = Follow Me or Rage Powder: The opposing x became the center of attention!
If move = Protect or Detect: x protected itself! 
If move = Protect or Detect: The opposing x protected itself!
If move = Substitute: x put in a substitute! x lost n% of its health!
close combat/def fell/sp def fell
If Substitute killed: x's substitute faded!
If Substitute alive: The substitute took damage for x!
If move = Reflect: Reflect made the opposing team stronger against physical moves
If move = Reflect: Reflect made ??? team stronger against physical moves
If move = Light Screen: Reflect made the opposing team stronger against special moves
If move = Light Screen: Reflect made ??? team stronger against special moves
If move = Helping Hand: The opposing x is ready to help the opposing y!
If move = Helping Hand: 
If move = Taunt: x fell for the taunt!
If move = Taunt: The opposing x fell for the taunt!
If move = Tailwind: The Tailwind blew from behind the opposing team!
If move has recoil: x was damaged by the recoil!
If move has recoil: The opposing x was damaged by the recoil!

x was burned!
x was hurt by its burn!
The opposing x was burned!
The opposing x was hurt by its burn!
'''
