import json
import discord

hall_of_fame_onlines = {}
hall_of_fame_offlines = {}
#hall_of_fame_exhibitions = {}

with open('HOF.json','r',encoding='utf8') as f: 
    hof = json.load(f)
    discordias_winners = hof["discordias"]["winners"]
    discordias = hof["discordias"]["tournaments"]
    hall_of_fame_onlines = hof["onlines"]
    hall_of_fame_offlines = hof["offlines"]
    #hall_of_fame_exhibitions = hof["exhibitions"]

def hall_of_fame_discordias_embed():

    final_first_half_discordias = ""
    final_second_half_discordias = ""
    final_first_half_winners = ""
    final_second_half_winners = ""
    first_half_discordias = []
    first_half_winners = []
    second_half_discordias = []
    second_half_winners = []

    first_half_discordias = discordias[:len(discordias)//2]
    first_half_winners = discordias_winners[:len(discordias_winners)//2]
    second_half_discordias = discordias[len(discordias)//2:]
    second_half_winners = discordias_winners[len(discordias_winners)//2:]

    for item in first_half_discordias:
        final_first_half_discordias = final_first_half_discordias + item + "\n"

    for item in first_half_winners:
        final_first_half_winners = final_first_half_winners + item + "\n"

    for item in second_half_discordias:
        final_second_half_discordias = final_second_half_discordias + item + "\n"

    for item in second_half_winners:
        final_second_half_winners = final_second_half_winners + item + "\n"

    embed1 = discord.Embed(title="HALL OF FAME - DISCÓRDIA LUSITANA/IBÉRICA")
    embed1.set_thumbnail(url="https://cdn.discordapp.com/attachments/854306255043428392/854306375156498453/C_ASK.png")
    embed1.add_field(name="Winners:", value=final_first_half_winners)
    embed1.add_field(name="Tournaments", value=final_first_half_discordias)

    embed2 = discord.Embed(title="HALL OF FAME - DISCÓRDIA LUSITANA/IBÉRICA")
    embed2.set_thumbnail(url="https://cdn.discordapp.com/attachments/854306255043428392/854306376356462613/C_BOB.png")
    embed2.add_field(name="Winners:", value=final_second_half_winners)
    embed2.add_field(name="Tournaments", value=final_second_half_discordias)
    return embed1, embed2