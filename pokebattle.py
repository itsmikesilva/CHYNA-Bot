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


    #def add_team(self, team_list):


class Pokemon:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.moves = []

        