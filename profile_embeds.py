import json
import discord
import difflib
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

profileIndex_id = {}
profileIndex_name = {}
with open('profiles.json','r',encoding='utf8') as f:
    profiles = json.load(f)
    for p in profiles:
        profileIndex_name[profiles[p]["player_name"].lower()] = profiles[p]
        profileIndex_id[profiles[p]["user_id"]] = profiles[p]

all_ranks = ["1ST DAN", "2ND DAN", "3RD DAN", "INITIATE", "MENTOR", "EXPERT", "GRAND MASTER", "BRAWLER", "MARAUDER", "FIGHTER", "VANGUARD",
             "WARRIOR", "VINDICATOR", "JUGGERNAUT", "USURPER", "VANQUISHER", "DESTROYER", "SAVIOR", "OVERLORD", "GENBU", "BYAKKO", "SEIRYU",
             "SUZAKU", "MIGHTY RULER", "REVERED RULER", "DIVINE RULER", "ETERNAL RULER", "FUJIN", "RAIJIN", "YAKSA", "RYUJIN", "EMPEROR", 
             "TEKKEN KING", "TEKKEN GOD", "TRUE TEKKEN GOD", "TEKKEN GOD PRIME", "TEKKEN GOD OMEGA"]

all_characters = ["Anna", "Armor King", "Shaheen", "Alisa", "Asuka", "Bob", "Bryan", "Gigas", "Lucky Chloe", "Dragunov", "Devil Jin", "Eddy",
                  "Eliza", "Feng", "Master Raven", "Ganryu", "Heihachi", "Hwoarang", "Claudio", "Jack-7", "Jin", "Julia", "Kazuya", "King", 
                  "Kuma", "Kunimitsu", "Kazumi", "Lars", "Law", "Lee", "Violet", "Lei", "Leo", "Lidia", "Lili", "Katarina", "Marduk", "Miguel",
                  "Akuma", "Geese", "Noctis", "Josie", "Nina", "Negan", "Leroy", "Fahkumram", "Panda", "Paul", "Steve", "Xiaoyu", "Yoshimitsu", 
                  "Zafina"]

#Função que vai encontrar o profile desejado
def find_profile(message):
    if message in profileIndex_name.keys():
        return profileIndex_name[message]
    else:
        print("Unexistent profile!")
        return 0

#Função que vai criar um novo profile
def create_profile(user_id, message):
    # verificar se existe algum profile com o id do utilizador
    if user_id in profileIndex_id.keys():
        print("A profile for this user already exists!")
        return 0

    #cria o profile from scratch
    new_profile = {}
    new_profile["player_name"] = message
    new_profile["user_id"] = user_id
    profileIndex_id[new_profile["user_id"]] = new_profile
    profileIndex_name[new_profile["player_name"].lower()] = new_profile
    with open('profiles.json', 'w', encoding='utf8') as f:
        json.dump(profileIndex_id, f, indent=4)
    return 1

#adiciona thumbnail
def add_thumbnail(message, user_id):

    with open('tekken_icons.json', 'r', encoding='utf8') as f:
        tekken_icons = json.load(f)
        icons_list = list(tekken_icons.keys())
        check_thumb = difflib.get_close_matches(message, icons_list)
        #Verifica se existe thumbnail para a character, caso afirmativo adiciona a thumbnail ao perfil associado
        if len(check_thumb) > 0 :
            if check_thumb[0] in tekken_icons.keys():               
                profileIndex_id[user_id]["thumbnail"] = tekken_icons[check_thumb[0]]
                name = profileIndex_id[user_id]["player_name"].lower()
                profileIndex_name[name]["thumbnail"] = tekken_icons[check_thumb[0]]

                #Cria uma key para a main character
                main_character = difflib.get_close_matches(message.capitalize(), all_characters)
                if len(main_character) > 0:
                    profileIndex_id[user_id]["main_character"] = main_character[0]
                    profileIndex_name[name]["main_character"] = main_character[0]
                    
                    #Se a nova main character estiver anteriormente definida como sub, remove-a da lista de subs
                    if "sub_characters" in profileIndex_id[user_id].keys():
                        for sub_character in profileIndex_id[user_id]["sub_characters"]:
                            if main_character[0] == sub_character:
                                profileIndex_id[user_id]["sub_characters"].remove(sub_character)
                                #Apaga a key de subs na situação de a sub character removida deixar a lista vazia
                                if len(profileIndex_id[user_id]["sub_characters"]) == 0:
                                    del profileIndex_id[user_id]["sub_characters"]

                with open('profiles.json', 'w', encoding='utf8') as g:
                    json.dump(profileIndex_id, g, indent=4)
                return 1
            else:
                print("Character not found!")
                return 0

# Adiciona o max rank
def add_max_rank(message, user_id):

    final_rank = difflib.get_close_matches(message.upper(), all_ranks)

    if len(final_rank) > 0:
        profileIndex_id[user_id]["max_rank"] = final_rank[0]
        name = profileIndex_id[user_id]["player_name"].lower()
        profileIndex_name[name]["max_rank"] = final_rank[0]
        with open('profiles.json', 'w', encoding='utf8') as f:
            json.dump(profileIndex_id, f, indent=4)
        return 1
    else:
        print("Rank not found!")
        return 0

# Adiciona sub characters
def add_sub_characters (message, user_id):
    
    subs_array = message.split(",")
    final_sub_characters = []
    if len(subs_array) > 3:
        print("Sub characters limit exceeded")
        return 0
    else:
        if "sub_characters" in profileIndex_id[user_id].keys():
            final_sub_characters = profileIndex_id[user_id]["sub_characters"].copy()
        else:
            profileIndex_id[user_id]["sub_characters"] = []
        # Verifica se as characters introduzidas pelo utilizador existem na database (lista de characters do jogo)
        for x in range(len(subs_array)):
            if(len(final_sub_characters)) == 3:
                return 0
            check_char_existence = difflib.get_close_matches(subs_array[x].capitalize(), all_characters)
            if len(check_char_existence) > 0:
                if check_char_existence[0] in profileIndex_id[user_id]["sub_characters"]:
                    return 3
                else:
                    final_sub_characters.append(check_char_existence[0])
            else:
                return 2
        #Verifica se as characters introduzidas pelo utilizador são ou não a main character
        for y in final_sub_characters:
            if y == profileIndex_id[user_id]["main_character"]:
                final_sub_characters.remove(y)
                return -1

        profileIndex_id[user_id]["sub_characters"] = final_sub_characters
        name = profileIndex_id[user_id]["player_name"].lower()
        profileIndex_name[name]["sub_characters"] = final_sub_characters
    
        with open('profiles.json', 'w', encoding='utf8') as f:
            json.dump(profileIndex_id, f, indent=4)
        return 1

#Remove sub characters
def remove_sub_characters(message, user_id):

    subs_post_removal = []
    subs_post_removal = profileIndex_id[user_id]["sub_characters"]
    #Procura matches entre a mensagem e a lista de chars, e em seguida remove a char que tenha dado match da lista de subs
    sub_compare = difflib.get_close_matches(message.capitalize(), all_characters)
    if len(sub_compare) > 0:
        if sub_compare[0] in subs_post_removal:
            subs_post_removal.remove(sub_compare[0])
        else:
            print("Character not found in your SUB-CHARACTERS list!")
            return 0

    profileIndex_id[user_id]["sub_characters"] = subs_post_removal
    name = profileIndex_id[user_id]["player_name"].lower()
    profileIndex_name[name]["sub_characters"] = subs_post_removal
    #Apaga a key "sub_characters" caso deixem de existir subs após a remoção
    if len(profileIndex_id[user_id]["sub_characters"]) == 0:
        del profileIndex_id[user_id]["sub_characters"]
    
    with open('profiles.json', 'w', encoding='utf8') as f:
        json.dump(profileIndex_id, f, indent=4)
    return 1


#Adiciona social media do jogador
def add_social_media(message,user_id):

    #Este pattern dá match com os nomes do site -> Twitter, YouTube, Instagram, Twitch...
    pattern = "^(?:http)?s?(?:://)?(?:www\.)?([A-Za-z0-9]*)\.(?:[A-Za-z0-9]*)\/(?:.*)$"
    match = re.search(pattern, message)
    if not match:
        return -1

    social_list = []
    if "social_media" in profileIndex_id[user_id]:
        existing_social_list = profileIndex_id[user_id]["social_media"]
        existing_social_list.append(message)
        profileIndex_id[user_id]["social_media"] = existing_social_list
        name = profileIndex_id[user_id]["player_name"].lower()
        profileIndex_name[name]["social_media"] = existing_social_list
    else:
        profileIndex_id[user_id]["social_media"] = social_list
        name = profileIndex_id[user_id]["player_name"].lower()
        profileIndex_name[name]["social_media"] = social_list
        social_list.append(message)    
    
    with open('profiles.json', 'w', encoding='utf8') as f:
        json.dump(profileIndex_id, f, indent=4)
    return 0

#Remove a social media do jogador
def remove_social_media(msg, user_id):
    social_list =  []
    social_compare_list = []
    if "social_media" in profileIndex_id[user_id].keys():
        social_list = profileIndex_id[user_id]["social_media"]
        if len(social_list) > 0:
            for social_media_item in social_list:
                #Verifica se o item (link) da social media tem um nome reconhecivel através do pattern em regex (p.ex. twitter, twitch, youtube)
                pattern = "^(?:http)?s?(?:://)?(?:www\.)?([A-Za-z0-9]*)\.(?:[A-Za-z0-9]*)\/(?:.*)$"
                match = re.search(pattern, social_media_item)
                if match:
                    final_match = match.group(1)
                    social_compare_list.append(final_match)     #cria uma list das possiveis social medias para comparar com a mensagem
            all_socials = difflib.get_close_matches(msg, social_compare_list)
            if len(all_socials) > 0:
                new_msg = all_socials[0]
                social_list.pop(social_compare_list.index(new_msg))
            else:
                return 0        #este retorno serve para dizer à CHYNA que a social media a remover não existe no perfil do utilizador

            profileIndex_id[user_id]["social_media"] = social_list
            name = profileIndex_id[user_id]["player_name"].lower()
            profileIndex_name[name]["social_media"] = social_list

            if len(profileIndex_id[user_id]["social_media"]) == 0:
                del profileIndex_id[user_id]["social_media"]

            with open('profiles.json', 'w', encoding='utf8') as f:
                json.dump(profileIndex_id, f, indent=4)
            return 1        #este retorno serve para dizer à CHYNA que a remoção da social media indicada foi successful
        else:
            return -1       #este retorno serve para dizer à CHYNA que não foram encontradas social medias at all
    else:
        return -1       #este retorno serve para dizer à CHYNA que não foram encontradas social medias at all

#Função que altera o player name
def name_change(msg, user_id):

    profileIndex_id[user_id]["player_name"] = msg

    with open('profiles.json', 'w', encoding='utf8') as f:
        json.dump(profileIndex_id, f, indent=4)

#Função que adiciona uma brief description do player
def description(msg, user_id):

    max_characters = 250
    if len(msg) > max_characters:
        print("Exceeded message limit! (" + str(max_characters) + ")")
        return 0
    else:
        profileIndex_id[user_id]["description"] = msg
        name = profileIndex_id[user_id]["player_name"].lower()
        profileIndex_name[name]["description"] = msg
        with open('profiles.json', 'w', encoding='utf8') as f:
            json.dump(profileIndex_id, f, indent=4)
        return 1

#Função que adiciona tournament results
def tournament_results(msg, user_id):
    
    accolades_list = []
    new_accolades = msg.split("/")
    if "accolades" in profileIndex_id[user_id].keys():
        existing_accolades = profileIndex_id[user_id]["accolades"]
        for item in new_accolades:
            existing_accolades.append(item)
        print(existing_accolades)
    else:
        profileIndex_id[user_id]["accolades"] = accolades_list
        name = profileIndex_id[user_id]["player_name"].lower()
        profileIndex_name[name]["accolades"] = accolades_list
        for item in new_accolades:
            accolades_list.append(item)

    with open('profiles.json', 'w', encoding='utf8') as f:
        json.dump(profileIndex_id, f, indent=4)

#Função que adiciona uma E-Sports Team
def set_esports_team(message,user_id):

    final_esports_team = message.upper()
    profileIndex_id[user_id]["esports_team"] = final_esports_team
    name = profileIndex_id[user_id]["player_name"].lower()
    profileIndex_name[name]["esports_team"] = final_esports_team
    
    with open('profiles.json', 'w', encoding='utf8') as f:
        json.dump(profileIndex_id, f, indent=4)

#Função que remove uma E-Sports Team
def remove_esports_team(user_id):

    if "esports_team" in profileIndex_id[user_id].keys():
        del profileIndex_id[user_id]["esports_team"]
    else:
        print("There is no E-Sports Team assigned to this profile!")
        return 0
    
    with open('profiles.json', 'w', encoding='utf8') as f:
        json.dump(profileIndex_id, f, indent=4)
    return 1

#Remove o tournament result desejado
def remove_tournament_results_final(number, user_id):
    number = number - 1
    accolades_list = profileIndex_id[user_id]["accolades"]
    if number >= len(accolades_list):
        return 0
    else:
        for i in range(len(accolades_list)):
            if i == number:
                accolades_list.remove(accolades_list[i])

    with open('profiles.json', 'w', encoding='utf8') as f:
        json.dump(profileIndex_id, f, indent=4)
    return 1

#Pick top 3 tournament results
def pick_tournament_results_interface(accolades_list):

    accolades_menu = ""
    for item in accolades_list:
        accolades_menu += item + "\n"
    embed = discord.Embed(title="Tournament Results", description="Choose the numbers of the results you wish to set as the main results (MAX 3): ")
    embed.add_field(name="Choosing", value= accolades_menu)

    return embed

#Coloca as picks do user nos primeiros indices de uma nova lista, preenche os restantes
def pick_accolades_final(numbers, user_id):

    accolades_list = profileIndex_id[user_id]["accolades"]
    new_accolades = []

    if len(numbers) > 3:
        return 0
    #Dá-nos os indices das accolades no json que pretendemos colocar nos primeiros 1,2 ou 3 da nova lista (aka os top results)
    while True:
        try:
            for i in range(len(numbers)):
                numbers[i] = int(numbers[i])
                numbers[i] = numbers[i] - 1
            #Procura adicionar o conteudo da lista c/ os indexes desejados numa nova lista
            for j in numbers:
                new_accolades.append(accolades_list[j])
            #Adiciona os restantes elementos da lista de accolades na nova lista
            for k in range(len(accolades_list)):
                if k not in numbers:
                        new_accolades.append(accolades_list[k])
            
            profileIndex_id[user_id]["accolades"] = new_accolades.copy()
            name = profileIndex_id[user_id]["player_name"].lower()
            profileIndex_name[name]["accolades"] = new_accolades.copy()

            with open('profiles.json', 'w', encoding='utf8') as f:
                    json.dump(profileIndex_id, f, indent=4)
            return 1

        except ValueError:
            return -1

        except IndexError:
            return -2

#Cria um embed para uma nova página apenas de tournament results
def tournament_results_embed(message):

    final_profile = find_profile(message)

    if "accolades" in final_profile.keys():
        accolades_string = ""
        accolades_final_list = final_profile["accolades"]
        for item in accolades_final_list:
            accolades_string += "➡️ " + item + "\n"
        embed = discord.Embed(title=final_profile["player_name"] + "'s Tournament History")
        embed.add_field(name="Tournament Results & Other Accomplishments", value=accolades_string)
        if "thumbnail" in final_profile.keys():
            embed.set_thumbnail(url=final_profile["thumbnail"])

        return embed
    else:
        return 0

#Cria lista de accolades com números para a edição dos accolades existentes
def tournament_results_list(user_id):

    accolades_list = profileIndex_id[user_id]["accolades"]
    accolades_menu = ""
    count = 1
    for item in accolades_list:
        accolades_menu += str(count) + "- " + item + "\n"
        count += 1
    accolades_final = accolades_menu.split("\n")
    accolades_final.pop()

    return accolades_final

#Cria embed de interface ao utilizador (Editar Tournament Result)
def edit_tournament_results_interface(accolades_list):

    accolades_menu = ""
    for item in accolades_list:
        accolades_menu += item + "\n"
    embed = discord.Embed(title="Tournament Results", description="Choose the number of the result you wish to edit: ")
    embed.add_field(name="Editing", value= accolades_menu)

    return embed

#Faz a edição e update do json dos tournament results
def edit_tournament_results_final(new_msg, number, user_id):

    number = number - 1
    accolades_list = profileIndex_id[user_id]["accolades"]
    if number >= len(accolades_list):
        return 0
    else:
        for i in range(len(accolades_list)):
            if i == number:
                accolades_list[i] = new_msg

    with open('profiles.json', 'w', encoding='utf8') as f:
        json.dump(profileIndex_id, f, indent=4)
    return 1

#Cria interface ao utilizador (Remover Tournament Result)
def remove_tournament_results_interface(accolades_list):

    accolades_menu = ""
    for item in accolades_list:
        accolades_menu += item + "\n"
    embed = discord.Embed(title="Tournament Results", description="Choose the number of the result you wish to remove: ")
    embed.add_field(name="Removing", value= accolades_menu)

    return embed

#adiciona vods ao profile
def add_vods(vod_link, user_id):

    temp_vods = []
    vod_list = vod_link.split(", ")
    for vod in vod_list:
        if " " in vod.strip():
            return 3
    if len(vod_list) > 3:
        return 2
    pattern = "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    for vod in vod_list:
        match = re.search(pattern, vod)
        if match:
            pass
        else:
            return 0
    driver = webdriver.Chrome()
    cookies_clicked = False
    if "vods" in profileIndex_id[user_id].keys():
        temp_vods = profileIndex_id[user_id]["vods"]
    for vod in vod_list:
        driver.get(vod)
        try:
            if not cookies_clicked:
                cookies_button = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='yDmH0d']/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div[1]/div/button")))
                cookies_button.click()
                cookies_clicked = True
        except:
            print("vc demorou mt tempo a carregar")
        try:
            vod_name = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='container']/h1/yt-formatted-string")))
            vod_to_add = "[" + vod_name.text + "](" + vod + ")"
            temp_vods.append(vod_to_add)
        except:
            print("bo$$y")
        
        profileIndex_id[user_id]["vods"] = temp_vods
        name = profileIndex_id[user_id]["player_name"].lower()
        profileIndex_name[name]["vods"] = temp_vods
    print(temp_vods)

    with open('profiles.json', 'w', encoding='utf8') as f:
        json.dump(profileIndex_id, f, indent=4)
    return 1

def vods_page(message):

    final_profile = find_profile(message)

    if "vods" in final_profile.keys():
        vods_string = ""
        vods_list = final_profile["vods"]
        for vod in vods_list:
            vods_string += "➡️ " + vod + "\n"
        embed = discord.Embed(title="Videos, clips and highlights of " + final_profile["player_name"])
        embed.add_field(name="Clipada gostosa", value=vods_string)
        if "thumbnail" in final_profile.keys():
            embed.set_thumbnail(url=final_profile["thumbnail"])
        return embed
    else:
        return 0

#Recupera a lista de vods do player
def vods_list(user_id):

    if "vods" in profileIndex_id[user_id].keys():
        vods_list = profileIndex_id[user_id]["vods"]
        vods_menu = ""
        count = 1
        for item in vods_list:
            vods_menu += str(count) + "- " + item + "\n"
            count += 1
        vods_final = vods_menu.split("\n")
        vods_final.pop()

        return vods_final
    else:
        return 0

def remove_vods_interface(user_id):

    vods_menu = vods_list(user_id)
    print(vods_menu)
    if vods_menu == 0:
        return 0
    vods_final = ""
    for item in vods_menu:
        vods_final = vods_final + item + "\n"
    embed = discord.Embed(title="VODs list", description="Choose the number of the VOD you wish to remove: ")
    embed.add_field(name="Removing", value= vods_final)

    return embed

def remove_vods_final(number, user_id):

    number = number - 1
    vods_list = profileIndex_id[user_id]["vods"]
    if number >= len(vods_list):
        return 0
    else:
        for i in range(len(vods_list)):
            if i == number:
                vods_list.remove(vods_list[i])
                if len(vods_list) == 0:
                    del profileIndex_id[user_id]["vods"]

    with open('profiles.json', 'w', encoding='utf8') as f:
        json.dump(profileIndex_id, f, indent=4)
    return 1

#função que vai criar o embed do perfil encontrado
def profile_embed(message):
    final_profile = find_profile(message)

   #Cria o embed c/ player name
    if "esports_team" in final_profile.keys():
        embed = discord.Embed(title=final_profile["esports_team"] + " | " + final_profile["player_name"])
    else:
        embed = discord.Embed(title=final_profile["player_name"])

    #Adiciona a thumbnail caso exista
    if "thumbnail" in final_profile.keys():
        embed.set_thumbnail(url=final_profile["thumbnail"])
    
    #Adiciona max rank caso exista
    if "max_rank" in final_profile.keys():
        embed.add_field(name="SEASON 4 MAX RANK", value=final_profile["max_rank"],inline=True)
    
    #Adiciona sub characters caso existam
    if "sub_characters" in final_profile.keys():
        sub_char_embed = ""
        for sub_character in final_profile["sub_characters"]:
            sub_char_embed = sub_char_embed + "\n" + sub_character
        embed.add_field(name="SUB-CHARACTERS",value=sub_char_embed,inline=True)

    #Adiciona uma breve descrição do jogador
    if "description" in final_profile.keys():
        embed.add_field(name="ABOUT THE PLAYER", value=final_profile["description"], inline=False)
    
    #Adiciona social media caso exista
    if "social_media" in final_profile.keys():
        if len(final_profile["social_media"]) > 0:
            social_media_string = ""
            for s in final_profile["social_media"]:
                pattern = "^(?:http)?s?(?:://)?(?:www\.)?([A-Za-z0-9]*)\.(?:[A-Za-z0-9]*)\/(?:.*)$"
                match = re.search(pattern, s)
                if match:
                    final_match = match.group(1)
                social_media_string += "[" + final_match.capitalize() + "]" + "(" + s + ")" + "\n"
            embed.add_field(name=final_profile["player_name"] + "'s Social Media", value=(social_media_string), inline=False)

    #Adiciona tournament results e outros accomplishments caso existam
    if "accolades" in final_profile.keys():
        accolades_final_list = final_profile["accolades"]
        accolades_string = ""
        counter = 0
        for item in accolades_final_list:
            if counter > 2:
                break
            accolades_string += item + "\n"
            counter += 1
        embed.add_field(name="TOP TOURNAMENT RESULTS: ", value=accolades_string,inline=False)

    return embed
