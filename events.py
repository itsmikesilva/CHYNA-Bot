import discord
import json
import difflib
import re

aliases = []
eventIndex_name = {}
online_eventIndex_name = {}
with open ("events.json",'r',encoding='utf8') as f:
    events_dict = json.load(f)
    for item in events_dict:
        eventIndex_name[events_dict[item]["name"]] = events_dict[item]
    
with open("online_events.json", 'r', encoding='utf8') as g:
    online_events_dict = json.load(g)
    for item in online_events_dict:
        online_eventIndex_name[online_events_dict[item]["name"]] = online_events_dict[item]
    
def event_embeds(message):
    with open('aliases_list.json', 'r', encoding='utf8') as f:
        events_list = json.load(f)

    selected_event = difflib.get_close_matches(message.upper(), events_list["aliases_list"]) #retorna a lista de aliases com que deu match
    tour = {}
    if len(selected_event) > 0:
        for item in events_dict:
            if selected_event[0] in events_dict[item]["aliases"]:
                tour = events_dict[item]    #este "tour" é o evento selecionado pelo user, após verificações
                break
        embed = discord.Embed(title=tour["name"], description=tour["location"])
        embed.set_image(url=tour["poster"])
        embed.add_field(name="Data", value=tour["date"])
        embed.add_field(name="VODs", value=tour["vod"], inline=True)
        embed.add_field(name="Vencedor(a)", value="🥇 " + tour["winner"], inline=False)
        embed.add_field(name="Runner-Ups", value="🥈 " + tour["top_3"][0] + "\n" + "🥉 " + tour["top_3"][1], inline=True)
        embed.add_field(name="Brackets", value=tour["brackets"], inline=True)
        embed.set_footer(text="Organizadores: " + tour["organizers"])
        return embed

    else:
        print("Event not found!")
        return 0

def online_event_embed(message):
    with open('aliases_list.json', 'r', encoding='utf8') as f:
        online_events_list = json.load(f)
        selected_event = difflib.get_close_matches(message.upper(), online_events_list["online_aliases_list"])
        tour = {}
        top_8_string = ""
        if len(selected_event) > 0:
            for item in online_events_dict:
                if selected_event[0] in online_events_dict[item]["aliases"]:
                    tour = online_events_dict[item]    #este "tour" é o evento selecionado pelo user, após verificações
                    break
            embed = discord.Embed(title=tour["name"])
            embed.add_field(name="Data", value=tour["date"])
            embed.add_field(name="VODs", value=tour["vod"], inline=True)
            embed.add_field(name="Vencedor(a)", value="🥇 " + tour["winner"], inline=False)
            for player in tour["top_8"]:
                top_8_string = top_8_string + player + "\n"
            #embed.add_field(name="Top 8", value="🥈 " + tour["top_3"][0] + "\n" + "🥉 " + tour["top_3"][1], inline=True)
            embed.add_field(name="Top 8", value=top_8_string, inline=True)
            embed.add_field(name="Brackets", value=tour["brackets"], inline=True)
            embed.set_footer(text="Organizadores: " + tour["organizers"])
            if "poster" in tour.keys():
                embed.set_image(url=tour["poster"])
            return embed
    
def edit_event_embed():

    count = 0
    num = 1
    tourneys_array = []
    embed_array = []
    embed = discord.Embed(title="LISTA DE TORNEIOS OFFLINE")
    embed_content_name = ""
    with open("events.json", 'r',encoding='utf8') as f:
        tourneys_dict = json.load(f)
        for item in tourneys_dict:
            tourneys_array.append(tourneys_dict[item]["name"])
        for item in range(len(tourneys_array)):
            embed_content_name = embed_content_name + str(num) + "- " + tourneys_array[item] + "\n"
            count += 1
            num += 1
            if count == 10:
                embed.add_field(name="Escolhe o torneio que desejas editar:", value=embed_content_name)
                embed.set_image(url="https://tekkenportugal.com/wp-content/uploads/2018/12/liga-ptfighters-finais-2018-banner.jpg")
                embed_array.append(embed)
                embed_content_name = ""
                embed = discord.Embed(title="LISTA DE TORNEIOS OFFLINE")
                count = 0
        embed.add_field(name="Escolhe o torneio que desejas editar:", value=embed_content_name)
        embed.set_image(url="https://tekkenportugal.com/wp-content/uploads/2018/12/liga-ptfighters-finais-2018-banner.jpg")
        embed_array.append(embed)
    return embed_array

def edit_event_parameter_embed():

    embed = discord.Embed(title="SELEÇÃO DE PARÂMETRO A EDITAR")
    embed_content = "1- Nome do Evento\n2- Data do Evento\n3- Siglas/Aliases\n4- Bracket Link\n5- VODs\n6- Poster do Evento\n7- Localização do eventon\n8- Vencedor do Evento\n9- Top 3\n10- Organizadores"
    embed.add_field(name="Escolhe o número do parâmetro que desejas editar", value=embed_content)
    return embed

class event:
    
    def __init__(self, name):
        self.name = name
        self.date = ""
        self.aliases = []
        self.brackets = ""
        self.vod = ""
        self.poster = ""
        self.location = ""
        self.winner = ""
        self.top_3 = []
        self.organizers = ""

    def add_event(self):
        eventIndex_name[self.name] = {}
        eventIndex_name[self.name]["name"] = self.name
        eventIndex_name[self.name]["date"] = self.date
        eventIndex_name[self.name]["aliases"] = self.aliases
        eventIndex_name[self.name]["brackets"] = self.brackets
        eventIndex_name[self.name]["vod"] = self.vod
        eventIndex_name[self.name]["poster"] = self.poster
        eventIndex_name[self.name]["location"] = self.location
        eventIndex_name[self.name]["winner"] = self.winner
        eventIndex_name[self.name]["top_3"] = self.top_3
        eventIndex_name[self.name]["organizers"] = self.organizers
        
        
        with open('aliases_list.json', 'r', encoding='utf8') as g:
            events_list = json.load(g)
        with open('aliases_list.json', 'w', encoding='utf8') as h:
            events_list["aliases_list"].append(self.name.upper())
            json.dump(events_list,h, indent=4)
        with open('events.json', 'w', encoding='utf8') as f:
            json.dump(eventIndex_name, f, indent=4)
        return self

    def add_event_date(self, new_date):

        self.date = new_date
        eventIndex_name[self.name]["date"] = self.date
        with open('events.json', 'w', encoding='utf8') as f:
            json.dump(eventIndex_name, f, indent=4)
        return self

    def add_event_aliases(self, new_aliases):
        
        final_aliases = []
        final_aliases = new_aliases.split(", ")
        for item in final_aliases:
            self.aliases.append(item.upper())
        eventIndex_name[self.name]["aliases"] = self.aliases

        with open('aliases_list.json', 'r', encoding='utf8') as g:
            events_list = json.load(g)
        with open('aliases_list.json', 'w', encoding='utf8') as h:
            for item in self.aliases:
                events_list["aliases_list"].append(item.upper())
            json.dump(events_list,h, indent=4)

        with open('events.json', 'w', encoding='utf8') as f:
            json.dump(eventIndex_name, f, indent=4)
        return self

    def add_event_brackets(self, brackets_link):

        brackets_check = brackets_link.split()
        if len(brackets_check) > 1:
            return 0
        else:
            final_brackets = ""
            pattern = "^(?:http)?s?(?:://)?(?:www\.)?([A-Za-z0-9]*)\.(?:[A-Za-z0-9]*)\/(?:.*)$"
            match = re.search(pattern, brackets_link)
            if match:
                final_match = match.group(1)
            final_brackets = "[" + final_match.capitalize() + "](" + brackets_link + ")"
            self.brackets = final_brackets
            eventIndex_name[self.name]["brackets"] = self.brackets
            with open('events.json', 'w', encoding='utf8') as f:
                json.dump(eventIndex_name, f, indent=4)
            return 1, self

    def add_event_vods(self, new_vods):

        final_vods = []
        vods_string = ""
        count = 1
        final_vods = new_vods.split(",")
        if len(final_vods) > 3:
            return 0
        else:
            for item in final_vods:
                if len(final_vods) == 1:
                    vods_string = vods_string + "[VOD de " + eventIndex_name[self.name]["name"] + "](" + item + ")"
                else:
                    vods_string = vods_string + "[VOD de " + eventIndex_name[self.name]["name"] + " Part %s" % count + "](" + item + ")\n"
                    count += 1
            self.vod = vods_string
            eventIndex_name[self.name]["vod"] = self.vod
            with open('events.json', 'w', encoding='utf8') as f:
                json.dump(eventIndex_name, f, indent=4)
            return self

    def add_event_poster(self, new_poster):

        self.poster = new_poster
        eventIndex_name[self.name]["poster"] = self.poster
        with open('events.json', 'w', encoding='utf8') as f:
                json.dump(eventIndex_name, f, indent=4)
        return self

    def add_event_location(self, new_location):

        self.location = new_location
        eventIndex_name[self.name]["location"] = self.location
        with open('events.json', 'w', encoding='utf8') as f:
                json.dump(eventIndex_name, f, indent=4)
        return self

    def add_event_winner(self, new_winner):

        self.winner = new_winner
        eventIndex_name[self.name]["winner"] = self.winner
        with open('events.json', 'w', encoding='utf8') as f:
                json.dump(eventIndex_name, f, indent=4)
        return self

    def add_event_top_3(self, new_top_3):

        final_top_3 = []
        final_top_3 = new_top_3.split(", ")
        if len(final_top_3) > 2 or len(final_top_3) < 2:
            return 0
        else:
            self.top_3 = final_top_3
            eventIndex_name[self.name]["top_3"] = self.top_3
            with open('events.json', 'w', encoding='utf8') as f:
                json.dump(eventIndex_name, f, indent=4)
            return self

    def add_event_organizers(self, new_organizers):

        self.organizers = new_organizers
        eventIndex_name[self.name]["organizers"] = self.organizers
        with open('events.json', 'w', encoding='utf8') as f:
                json.dump(eventIndex_name, f, indent=4)
        return self
