from selenium import webdriver
import time

#arranjar isto de forma a ser um ciclo e fazer para todos os replays do replaylinks.txt
driver = webdriver.Chrome()
with open('replaytest.txt', 'r', encoding='utf8') as f:
    replays_list = f.readlines()
    for item in replays_list:
        driver.get(item)
        time.sleep(5)
        play_button = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[1]/div[2]/button[1]")
        play_button.click()
        time.sleep(3)
        for i in range(200):
            next_turn_button = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[3]/button[4]")
            next_turn_button.click()
    
        #Obter as teams
        count = 0
        webelement_teams_list = []
        pokemon_teams_list = []
        pokemon_team_1 = []
        pokemon_team_2 = []
        webelement_teams_list = driver.find_elements_by_xpath("//div[@class='chat battle-history']")    #vai buscar o segmento que tem os 6 mons do preview de cada team
        for i in webelement_teams_list:
            pokemon_teams_list.append(i.text)   #adiciona numa lista as strings que contem ambas as teams;
        for i in pokemon_teams_list:
            to_add = i.split("\n", 1)[1]    #as newlines nestes exemplos separam o nome do jogador dos mons, e nós apenas queremos os mons
            pokemon_teams_list[count] = to_add  #os indices desta lista passam a ser APENAS os mons
            count += 1
        pokemon_team_1 = pokemon_teams_list[0].split(" / ") #lista com os mons da team 1
        pokemon_team_2 = pokemon_teams_list[1].split(" / ") #lista com os mons da team 2
        print(pokemon_team_1)
        print(pokemon_team_2)
        time.sleep(3)
        battle_log_full = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[2]")
        battle_log = battle_log_full.text.split("Turn ")
        battle_repr = []
        for i in range(len(battle_log)):
            turn_actions = [x for x in battle_log[i].split("\n") if x != ""]
            del turn_actions[0]
            battle_repr.append(turn_actions)
        print(battle_repr)