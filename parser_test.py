from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://replay.pokemonshowdown.com/")
time.sleep(10)
element = driver.find_element_by_xpath("/html/body/div[2]/div/form[2]/p/label/input")
element.send_keys("gen8vgc2021series10")
time.sleep(3)
search_button = driver.find_element_by_xpath("/html/body/div[2]/div/form[2]/p/button")
search_button.click()
time.sleep(3)
replay = driver.find_element_by_xpath("/html/body/div[2]/div/ul[2]/li[1]/a")
replay.click()
time.sleep(1)

#Obter as teams
count = 0
webelement_teams_list = []
pokemon_teams_list = []
pokemon_team_1 = []
pokemon_team_2 = []
webelement_teams_list = driver.find_elements_by_xpath("//div[@class='chat battle-history']")
for i in webelement_teams_list:
    pokemon_teams_list.append(i.text)
for i in pokemon_teams_list:
    to_add = i.split("\n", 1)[1]
    pokemon_teams_list[count] = to_add
    count += 1
pokemon_team_1 = pokemon_teams_list[0].split(" / ")
pokemon_team_2 = pokemon_teams_list[1].split(" / ")
print(pokemon_team_1)
print(pokemon_team_2)

play_button = driver.find_element_by_xpath("/html/body/div[3]/div/div/div[1]/div[2]/button[1]")
play_button.click()

#xpath battle log: /html/body/div[3]/div/div/div[2]
#xpath dos active pokemon: /html/body/div[3]/div/div/div[1]/div[1]/div[6]