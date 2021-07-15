from pokebattle import Battle
from pokebattle import Pokemon
import pickle

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
                pokemon = action.split(" ")[-1]
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

for turn in replay[2]:
    for actions in turn:
        for action in actions:
            if "used" in action and "opposing" in action:
                action_result = action.split("The opposing ")[1].split(" used ") 
                pokemon_name = action_result[0]
                pokemon_move = action_result[1][:-1]
                battle.opposing_team[pokemon_name].name = pokemon_name
                print(actions)
                print(action)
                print(pokemon_name)
                print(pokemon_move)
                print()

            if "used" in action and "opposing" not in action:
                action_result = action.split(" used ") 
                pokemon_name = action_result[0]
                pokemon_move = action_result[1][:-1]
                print(actions)
                print(action)
                print(pokemon_name)
                print(pokemon_move)
                print()

            if "lost" in action and "opposing" not in action:
                action_result = action.split(" lost ")
                pokemon_name = action_result[0][1:]
                hp_lost = action_result[1].split("%")[0]
                print(action)
                print(pokemon_name)
                print(hp_lost)
                print()

            if "lost" in action and "opposing" in action:
                action_result = action.split(" lost ")
                pokemon_name = action_result[0].split("The opposing ")[1]
                hp_lost = action_result[1].split("%")[0]
                print(action)
                print(pokemon_name)
                print(hp_lost)
                print()

                
#print(replay[2][1])

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
