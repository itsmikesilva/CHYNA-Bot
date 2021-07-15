import copy

class Battle:
    
    def __init__(self):
        self.player_team = {}
        self.opposing_team = {}
        self.picked_player_team = []        #4 pokemons escolhidos dos 6, da team 1
        self.picked_opposing_team = []      #4 pokemons escolhidos dos 6, da team 2
        self.pokemon_field_1 = ""
        self.pokemon_field_2 = ""
        self.opposing_pokemon_field_1 = ""
        self.opposing_pokemon_field_2 = ""

    def getCopy(self):
        new_battle = Battle()
        new_battle.player_team = copy.deepcopy(self.player_team)
        new_battle.opposing_team = copy.deepcopy(self.opposing_team)
        new_battle.picked_player_team = copy.deepcopy(self.picked_player_team)
        new_battle.picked_opposing_team = copy.deepcopy(self.picked_opposing_team)
        new_battle.pokemon_field_1 = self.pokemon_field_1
        new_battle.pokemon_field_2 = self.pokemon_field_2
        new_battle.opposing_pokemon_field_1 = self.opposing_pokemon_field_1
        new_battle.opposing_pokemon_field_2 = self.opposing_pokemon_field_2
        return new_battle

    #def add_team(self, team_list):


class Pokemon:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.moves = []

        