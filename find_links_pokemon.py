import selenium
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://replay.pokemonshowdown.com/")
time.sleep(5)
element = driver.find_element_by_xpath("/html/body/div[2]/div/form[2]/p/label/input")
element.send_keys("gen8vgc2021series10")
time.sleep(3)
search_button = driver.find_element_by_xpath("/html/body/div[2]/div/form[2]/p/button")
search_button.click()
time.sleep(3)
more_button = driver.find_element_by_xpath("/html/body/div[2]/div/p/button")
while True:
    try:
        more_button.click()
    except selenium.common.exceptions.StaleElementReferenceException:
        break
time.sleep(5)
link_final = driver.find_elements_by_xpath("/html/body/div[2]/div/ul[2]/li/a")
time.sleep(2)
battle_links_list = []
battle_link = ""
for i in link_final:
    battle_link = i.get_attribute("href")   #vai buscar o atributo "href" que contém o link do replay
    battle_links_list.append(battle_link)
print(battle_links_list)
with open('replaylinks.txt', 'w', encoding='utf8') as f:
    for i in battle_links_list:
        f.write(i + "\n")
driver.close()