import json
import discord
import random

hall_of_fame_onlines = {}
hall_of_fame_offlines = {}
#hall_of_fame_exhibitions = {}

with open('HOF.json','r',encoding='utf8') as f: 
    hof = json.load(f)
    discordias_winners = hof["discordias"]["winners"]
    discordias = hof["discordias"]["tournaments"]
    onlines_winners = hof["onlines"]["winners"]
    onlines_tournaments = hof["onlines"]["tournaments"]
    offline_winners = hof["offlines"]["winners"]
    offline_tournaments = hof["offlines"]["tournaments"]
    #hall_of_fame_exhibitions = hof["exhibitions"]

def hall_of_fame_discordias_embed():

    with open('tekken_icons.json', 'r', encoding='utf8') as f:
        tekken_icons = json.load(f)
        icons_list = list(tekken_icons.keys())

        count = 0
        embed_array = []
        embed = discord.Embed(title="HALL OF FAME - DISCÓRDIA LUSITANA/IBÉRICA")
        embed_content_w = ""
        embed_content_t = ""
        for item in range(len(discordias)):
            winner = discordias_winners[item]
            tournament = discordias[item]
            embed_content_w = embed_content_w + winner + "\n"
            embed_content_t = embed_content_t + tournament + "\n"
            count += 1
            if count == 10:
                thumb = random.choice(icons_list)
                embed.set_thumbnail(url=tekken_icons[thumb])
                embed.add_field(name="Vencedores", value=embed_content_w)
                embed.add_field(name="Torneios", value=embed_content_t)
                embed_array.append(embed)
                embed_content_w = ""
                embed_content_t = ""
                embed = discord.Embed(title="HALL OF FAME - DISCÓRDIA LUSITANA/IBÉRICA")
                count = 0
        
        thumb = random.choice(icons_list)
        embed.set_thumbnail(url=tekken_icons[thumb])
        embed.add_field(name="Vencedores", value=embed_content_w)
        embed.add_field(name="Torneios", value=embed_content_t)
        embed_array.append(embed)
        

        return embed_array

def hall_of_fame_onlines_embed():

    with open('tekken_icons.json', 'r', encoding='utf8') as f:
        tekken_icons = json.load(f)
        icons_list = list(tekken_icons.keys())

        count = 0
        embed_array = []
        embed = discord.Embed(title="HALL OF FAME - OUTROS TORNEIOS ONLINE")
        embed_content_w = ""
        embed_content_t = ""
        for item in range(len(onlines_tournaments)):
            winner = onlines_winners[item]
            tournament = onlines_tournaments[item]
            embed_content_w = embed_content_w + winner + "\n"
            embed_content_t = embed_content_t + tournament + "\n"
            count += 1
            if count == 10:
                thumb = random.choice(icons_list)
                embed.set_thumbnail(url=tekken_icons[thumb])
                embed.add_field(name="Vencedores", value=embed_content_w)
                embed.add_field(name="Torneios", value=embed_content_t)
                embed_array.append(embed)
                embed_content_w = ""
                embed_content_t = ""
                embed = discord.Embed(title="HALL OF FAME - OUTROS TORNEIOS ONLINE")
                count = 0
        
        thumb = random.choice(icons_list)
        embed.set_thumbnail(url=tekken_icons[thumb])
        embed.add_field(name="Vencedores", value=embed_content_w)
        embed.add_field(name="Torneios", value=embed_content_t)
        embed_array.append(embed)
        

        return embed_array

def hall_of_fame_offlines_embed():

    with open('tekken_icons.json', 'r', encoding='utf8') as f:
        tekken_icons = json.load(f)
        icons_list = list(tekken_icons.keys())

        count = 0
        embed_array = []
        embed = discord.Embed(title="HALL OF FAME - TORNEIOS OFFLINE")
        embed_content_w = ""
        embed_content_t = ""
        for item in range(len(offline_tournaments)):
            winner = offline_winners[item]
            tournament = offline_tournaments[item]
            embed_content_w = embed_content_w + winner + "\n"
            embed_content_t = embed_content_t + tournament + "\n"
            count += 1
            if count == 10:
                thumb = random.choice(icons_list)
                embed.set_thumbnail(url=tekken_icons[thumb])
                embed.add_field(name="Vencedores", value=embed_content_w)
                embed.add_field(name="Torneios", value=embed_content_t)
                embed_array.append(embed)
                embed_content_w = ""
                embed_content_t = ""
                embed = discord.Embed(title="HALL OF FAME - TORNEIOS OFFLINE")
                count = 0
        
        thumb = random.choice(icons_list)
        embed.set_thumbnail(url=tekken_icons[thumb])
        embed.add_field(name="Vencedores", value=embed_content_w)
        embed.add_field(name="Torneios", value=embed_content_t)
        embed_array.append(embed)
        

        return embed_array

#def hall_of_fame_exhibitions():