import random
import discord
import profile_embeds
import events
import hall_of_fame
import help_embed
from reactionmenu import ReactionMenu, Button, ButtonType
from discord.ext import commands
import token_chyna
import youtube_dl
import os
from discord.ext import commands
import chyna_music
import nltk
from nltk.tokenize import word_tokenize
import operator

cogs = [chyna_music]
client = commands.Bot(command_prefix = "$")
client.remove_command("help")
history_messages = []
inv_index = {} 

#This function obtains messages from a certain text channel
@client.event
async def on_ready():
    history_channel = client.get_channel(406496729207406595) #ID corresponding to the #general chat we are getting messages from
    print("Processing messages from #general...")
    messages = await history_channel.history(limit=20000).flatten() #Obtains Message objects from the chosen channel and turns them into a list
    for m in messages:
        history_messages.append(m.content)  #Adds the content of Message objects (the message in text format) to a new list where all messages will be stored
    for i in range(len(history_messages)):
        words = word_tokenize(history_messages[i])  
        for w in words:
            if w not in inv_index.keys():
                inv_index[w] = []
            inv_index[w].append(i)  
    print(inv_index)

    print("CHYNA is ready!")

for i in range(len(cogs)):
    cogs[i].setup(client)

#This command prompts a menu that serves as a manual to help the users understand how CHYNA works
@client.command(name="manual", aliases=["m"])
async def help_menu(ctx):
    menu = ReactionMenu(ctx, back_button='⬅️', next_button='➡️', config=ReactionMenu.STATIC, style="$/&")
    #Each of the following functions creates an embed designed specifically for each command
    front_page_embed = help_embed.help_front_page()
    set_profile_embed = help_embed.create_profile_embed()
    set_thumbnail_embed = help_embed.thumbnail_page_embed()
    add_subs_embed, remove_subs_embed = help_embed.sub_chars_page_embed()
    set_max_rank_embed = help_embed.max_rank_page_embed()
    add_social_embed, remove_social_embed = help_embed.social_media_page_embed()
    add_user_description = help_embed.user_description_embed()
    add_esports_embed, remove_esports_embed = help_embed.esports_team_embed()
    name_change_page_embed = help_embed.name_change_embed()
    profile_page_embed = help_embed.profile_embed()
    add_results_embed, remove_results_embed, edit_results_embed, pick_results_embed = help_embed.tournament_results_page_embed()
    add_vods_embed = help_embed.set_vods_embed()
    delete_vods_embed = help_embed.remove_vods_embed()
    menu.add_page(front_page_embed)
    menu.add_page(set_profile_embed)
    menu.add_page(set_thumbnail_embed)
    menu.add_page(add_subs_embed)
    menu.add_page(remove_subs_embed)
    menu.add_page(set_max_rank_embed)
    menu.add_page(add_user_description)
    menu.add_page(add_social_embed)
    menu.add_page(remove_social_embed)
    menu.add_page(add_esports_embed)
    menu.add_page(remove_esports_embed)
    menu.add_page(name_change_page_embed)
    menu.add_page(profile_page_embed)
    menu.add_page(add_results_embed)
    menu.add_page(remove_results_embed)
    menu.add_page(edit_results_embed)
    menu.add_page(pick_results_embed)
    menu.add_page(add_vods_embed)
    menu.add_page(delete_vods_embed)
    await menu.start()

#Help Command
@client.command(name="helpcommands", aliases=["help"])
async def help_commands(ctx):
    msg = ctx.message.content.split(" ")
    if len(msg) > 1:
        command_embed = help_embed.call_command_help_embed(msg[1])  #This function returns the menu page for the desired section
        try:
            if command_embed == 0:  #If the menu page requested by the user doesn't exist, it returns 0
                await ctx.send("Command not found!")
            await ctx.send(embed=command_embed)
        except AttributeError:
            pass
    elif len(msg) == 1: #If the user only types "$help", a menu with every command is prompted for the user to choose
        menu = ReactionMenu(ctx, back_button='⬅️', next_button='➡️', config=ReactionMenu.STATIC, style="$/&")
        command_menu1, command_menu2 = help_embed.show_commands_embed()
        menu.add_page(command_menu1)
        menu.add_page(command_menu2)
        await menu.start()
        user_input = await client.wait_for('message', check=lambda message: message.author == ctx.author) #The menu will ask for user input in order to determine what help menu page will be shown
        command_number = int(user_input.content)
        chosen_command_embed = help_embed.call_command_help_embed(command_number)
        if chosen_command_embed == 1:   #If the prior function returns 1, the full help manual will be displayed
            menu = ReactionMenu(ctx, back_button='⬅️', next_button='➡️', config=ReactionMenu.STATIC, style="$/&")
            front_page_embed = help_embed.help_front_page()
            set_profile_embed = help_embed.create_profile_embed()
            set_thumbnail_embed = help_embed.thumbnail_page_embed()
            add_subs_embed, remove_subs_embed = help_embed.sub_chars_page_embed()
            set_max_rank_embed = help_embed.max_rank_page_embed()
            add_social_embed, remove_social_embed = help_embed.social_media_page_embed()
            add_user_description = help_embed.user_description_embed()
            add_esports_embed, remove_esports_embed = help_embed.esports_team_embed()
            name_change_page_embed = help_embed.name_change_embed()
            profile_page_embed = help_embed.profile_embed()
            add_results_embed, remove_results_embed, edit_results_embed, pick_results_embed = help_embed.tournament_results_page_embed()
            add_vods_embed = help_embed.set_vods_embed()
            delete_vods_embed = help_embed.remove_vods_embed()
            menu.add_page(front_page_embed)
            menu.add_page(set_profile_embed)
            menu.add_page(set_thumbnail_embed)
            menu.add_page(add_subs_embed)
            menu.add_page(remove_subs_embed)
            menu.add_page(set_max_rank_embed)
            menu.add_page(add_user_description)
            menu.add_page(add_social_embed)
            menu.add_page(remove_social_embed)
            menu.add_page(add_esports_embed)
            menu.add_page(remove_esports_embed)
            menu.add_page(name_change_page_embed)
            menu.add_page(profile_page_embed)
            menu.add_page(add_results_embed)
            menu.add_page(remove_results_embed)
            menu.add_page(edit_results_embed)
            menu.add_page(pick_results_embed)
            menu.add_page(add_vods_embed)
            menu.add_page(delete_vods_embed)
            await menu.start()
        await ctx.send(embed=chosen_command_embed)

#This command allows the user to create their own profile
@client.command(name="setprofile", aliases=["sp"])
async def setprofile(ctx):
    msg = ctx.message.content.split(" ", 1)[1]
    discord_user_id = ctx.message.author.id
    check_if_profile_exists = profile_embeds.create_profile(discord_user_id,msg)
    if check_if_profile_exists == 1:
        await ctx.send("Profile created successfully!")
    else:
        await ctx.send("A profile for this user already exists!")

#This command allows the user to view the profiles of other players
@client.command(name="profile", aliases=["p"])
async def profile(ctx):
    msg = ctx.message.content.split(" ", 1)[1]
    check_if_profile_exists = profile_embeds.find_profile(msg.lower())
    if check_if_profile_exists == 0:
        await ctx.send("This profile doesn't exist!")
    else:
        menu = ReactionMenu(ctx, back_button='⬅️', next_button='➡️', config=ReactionMenu.STATIC, style="$/&")
        searched_profile = profile_embeds.profile_embed(msg.lower())
        tournament_results = profile_embeds.tournament_results_embed(msg.lower())
        vods = profile_embeds.vods_page(msg.lower())
        menu.add_page(searched_profile)
        if tournament_results != 0:
            menu.add_page(tournament_results)
        if vods != 0:
            menu.add_page(vods)
        await menu.start()

#This command allows the user to add a thumbnail to their profile
@client.command(name="thumbnail", aliases=["t"])
async def set_thumbnail(ctx):
    msg = ctx.message.content.split(" ", 1)[1]
    discord_user_id = ctx.message.author.id
    check_if_char_exists = profile_embeds.add_thumbnail(msg, discord_user_id)
    if check_if_char_exists == 0:
        await ctx.send("The character was not identified! (HINT: Try inputting the character's first name. In some cases, you might have to type two names! See the following example!)\n**Characters with ONE name**: !st Marduk; !st Anna; !st Jin\n**Characters with MORE THAN ONE name**: !st Lucky Chloe; !st Master Raven")
    else:
        await ctx.send("Thumbnail added successfully!")

#This command allows the user to add their max rank in Online Mode to their profile
@client.command(name="maxrank", aliases=["mr"])
async def set_max_rank(ctx):
    msg = ctx.message.content.split(" ", 1)[1]
    discord_user_id = ctx.message.author.id
    check_if_rank_exists = profile_embeds.add_max_rank(msg, discord_user_id)
    if check_if_rank_exists == 0:
        await ctx.send("Rank not found! (HINT: If the rank has more than one name, type it the way it's written in the game. Acronyms will not work!)\n\nExample: !sr tgo ❌ !sr tekken god omega ✅")
    else:
        await ctx.send("Season 4 MAX RANK added successfully!")

#This command allows the user to add their secondary characters to their profile
@client.command(name="setsubs", aliases=["ss"])
async def set_sub_characters(ctx):
    msg = ctx.message.content.split(" ", 1)[1]
    discord_user_id = ctx.message.author.id
    check_if_sub_limit = profile_embeds.add_sub_characters(msg, discord_user_id)
    if check_if_sub_limit == 0:
        await ctx.send("SUB-CHARACTERS limit out of bounds! (MAX 3)\n\n**HINT:** If you wish to remove a SUB-CHARACTER, use the command !rs followed by the character's name. Example: !rs Heihachi")
    elif check_if_sub_limit == -1:
        await ctx.send("The MAIN CHARACTER can't be a SUB-CHARACTER! (HINT: In the case you wish to change your main character, use the command !st to set the new main character/thumbnail.)")
    elif check_if_sub_limit == 2:
        await ctx.send("The selected character doesn't exist!")
    elif check_if_sub_limit == 3:
        await ctx.send("The selected character is already a SUB-CHARACTER!")
    else:
        await ctx.send("SUB-CHARACTER(S) added successfully!\n\n **WARNING:**\nIf one of the SUB-CHARACTERS was not added as intended, use the help command '!h !ss'")

#This command allows the user to remove a sub-character
@client.command(name="removesubs", aliases=["rs"])
async def delete_sub_characters(ctx):
    msg = ctx.message.content.split(" ", 1)[1]
    discord_user_id = ctx.message.author.id
    check_removal_success = profile_embeds.remove_sub_characters(msg, discord_user_id)
    if check_removal_success == 0:
        await ctx.send("Character not found in the SUB-CHARACTERS list!")
    else:
        await ctx.send("SUB-CHARACTER removed successfully!")

#This command allows the user to add their social medias in their profile
@client.command(name="setsocial", aliases=["sm"])
async def set_social_media(ctx):
    msg = ctx.message.content.split(" ", 1)[1]
    discord_user_id = ctx.message.author.id
    check_if_link_works = profile_embeds.add_social_media(msg, discord_user_id)
    if check_if_link_works == 0:
        await ctx.send("Social Media added successfully!")
    elif check_if_link_works == -1:
        await ctx.send("This social media link is invalid!")

#This command allows the user to remove a social media from their profile
@client.command(name="removesocial", aliases=["rm"])
async def delete_social_media(ctx):
    msg = ctx.message.content.split(" ", 1)[1]
    discord_user_id = ctx.message.author.id
    check_if_social_exist = profile_embeds.remove_social_media(msg, discord_user_id)
    if check_if_social_exist == 1:
        await ctx.send("Social Media removed successfully!")
    elif check_if_social_exist == -1:
        await ctx.send("No social media was found.")
    elif check_if_social_exist == 0:
        await ctx.send(msg.capitalize() + " was not found in this user's profile.")

#This command allows the user to change their player name
@client.command(name="changename", aliases=["cn"])
async def change_name(ctx):
    msg = ctx.message.content.split(" ", 1)[1]
    discord_user_id = ctx.message.author.id
    profile_embeds.name_change(msg, discord_user_id)
    await ctx.send("Player name edited successfully!")

#This command allows the user to write a message or speak about themselves in a little section of their profile
@client.command(name="description", aliases=["d"])
async def player_description(ctx):
    limit = 250
    msg = ctx.message.content.split(" ", 1)[1]
    discord_user_id = ctx.message.author.id
    check_if_exceeds_limit = profile_embeds.description(msg, discord_user_id)
    if check_if_exceeds_limit == 0:
        await ctx.send("Character limit out of bounds! (" + str(limit) + ")")
    else:
        await ctx.send("Player description added/edited successfully!")

#This command allows the user to add their tournament results in their profile
@client.command(name="results", aliases=["tr"])
async def add_accolades(ctx):
    msg = ctx.message.content.split(" ", 1)[1]
    discord_user_id = ctx.message.author.id
    profile_embeds.tournament_results(msg, discord_user_id)
    await ctx.send("Tournament Results added successfully!")

#This command allows the user to edit their tournament results
@client.command(name="editresults", aliases=["er"])
async def edit_accolades(ctx):
    discord_user_id = ctx.message.author.id
    accolades_list = profile_embeds.tournament_results_list(discord_user_id)
    accolades_embed = profile_embeds.edit_tournament_results_interface(accolades_list)
    await ctx.send(embed=accolades_embed)

    msg = await client.wait_for('message', check=lambda message: message.author == ctx.author)  #The menu asks the user to choose the tournament result they wish to edit
    number = int(msg.content)
    await ctx.send("Type in the result you wish to save to your profile. This action will replace the tournament result you selected.")
    new_msg = await client.wait_for('message', check=lambda message: message.author == ctx.author)
    check_if_in_range = profile_embeds.edit_tournament_results_final(new_msg.content, number, discord_user_id)
    if check_if_in_range == 0:
        await ctx.send("Out of bounds! (The selected number doesn't exist in the list)")
    else:
        await ctx.send("Tournament Result edited successfully!")

#This command allows the user to remove a tournament result
@client.command(name="removeresults", aliases=["rr"])
async def delete_accolades(ctx):
    discord_user_id = ctx.message.author.id
    accolades_list = profile_embeds.tournament_results_list(discord_user_id)
    accolades_embed = profile_embeds.remove_tournament_results_interface(accolades_list)
    await ctx.send(embed=accolades_embed)

    msg = await client.wait_for('message', check=lambda message: message.author == ctx.author)  #The menu asks the user to choose the tournament result they wish to remove
    number = int(msg.content)
    check_if_in_range = profile_embeds.remove_tournament_results_final(number, discord_user_id)
    if check_if_in_range == 0:
        await ctx.send("Out of bounds! (The selected number doesn't exist in the list)")
    else:
        await ctx.send("Tournament Result removed successfully!")

#This command allows the user to chose their 3 favorite tournament results to be displayed in the user's profile front page
@client.command(name="pickresults", aliases=["pr"])
async def choose_accolades(ctx):
    discord_user_id = ctx.message.author.id
    accolades_list = profile_embeds.tournament_results_list(discord_user_id)
    accolades_embed = profile_embeds.pick_tournament_results_interface(accolades_list)
    await ctx.send(embed=accolades_embed)

    msg = await client.wait_for('message', check=lambda message: message.author == ctx.author)
    numbers = msg.content.split(",")
    check_if_valid = profile_embeds.pick_accolades_final(numbers, discord_user_id)
    if check_if_valid == 0:
        await ctx.send("Select a maximum of THREE tournament results. (Out of bounds)")
    elif check_if_valid == -1:
        await ctx.send("Invalid input. (Type in only NUMBERS separated by a comma AND a space. Example: 4, 2, 5)")
    elif check_if_valid == -2:
        await ctx.send("Out of bounds! (The selected number doesn't belong to the list)")
    elif check_if_valid == 1:
        await ctx.send("Results updated! See the new changes by typing '!p' followed by your profile name!")

#This command allows the user to add or edit their E-Sports team to their Player Name
@client.command(name="setesports", aliases=["se"])
async def add_esports_team(ctx):
    msg = ctx.message.content.split(" ", 1)[1]
    discord_user_id = ctx.message.author.id
    profile_embeds.set_esports_team(msg,discord_user_id)
    await ctx.send("E-Sports Team updated!")

#This command allows the user to remove their E-Sports team
@client.command(name="removeesports", aliases=["re"])
async def delete_esports_team(ctx):
    discord_user_id = ctx.message.author.id
    check_if_esports_team = profile_embeds.remove_esports_team(discord_user_id)
    if check_if_esports_team == 0:
        await ctx.send("No E-Sports Team assigned to this profile.")
    else:
        await ctx.send("E-Sports Team removed successfully!")

#This command allows the user to add their videos and clips to their profile
@client.command(name="setvods", aliases=["sv"])
async def set_vods(ctx):
    vod_link = ctx.message.content.split(" ", 1)[1]
    discord_user_id = ctx.message.author.id
    check_vod_success = profile_embeds.add_vods(vod_link, discord_user_id)
    if check_vod_success == 1:
        await ctx.send("Video(s) added successfully!")
    elif check_vod_success == 2:
        await ctx.send("ATTENTION: You can only type in THREE links at a time (MAX)!")
    elif check_vod_success == 3:
        await ctx.send("ATTENTION: Use commas in between links!")
    elif check_vod_success == 0:
        await ctx.send("Invalid link!")

#This command allows the user to remove videos/clips from their profile
@client.command(name="removevods", aliases=["rv"])
async def remove_vods(ctx):
    
    discord_user_id = ctx.message.author.id
    vods_embed = profile_embeds.remove_vods_interface(discord_user_id) 
    if vods_embed == 0:
        await ctx.send("There are no VODs assigned to this profile.")
        return
    else:
        await ctx.send(embed=vods_embed)

    msg = await client.wait_for('message', check=lambda message: message.author == ctx.author)  #The menu will ask the user which VOD they wish to remove
    number = int(msg.content)
    check_if_in_range = profile_embeds.remove_vods_final(number, discord_user_id)
    if check_if_in_range == 0:
        await ctx.send("Out of bounds! (The selected number doesn't belong to the list.)")
    elif check_if_in_range == 1:
        await ctx.send("VOD removed successfully!")

#This command allows the user to view a past offline event
@client.command(name="event")
async def view_event(ctx):
    msg = ctx.message.content.split(" ", 1)[1]
    evento = events.event_embeds(msg)
    if evento == 0:
        await ctx.send("Event not found!")
    else:
        await ctx.send(embed=evento)

#This command allows the user to view a past online event
@client.command(name="onevent")
async def view_online_event(ctx):
    msg = ctx.message.content.split(" ", 1)[1]
    evento = events.online_event_embed(msg)
    if evento == 0:
        await ctx.send("Online event not found!")
    else:
        await ctx.send(embed=evento)

#This command allows the user to see a menu with the past results of the online tournaments labeled as DISCÓRDIA LUSITANA/DISCÓRDIA IBÉRICA
@client.command(name="discordias")
async def hof_discordias(ctx):
    discordias = hall_of_fame.hall_of_fame_discordias_embed()
    menu = ReactionMenu(ctx, back_button='⬅️', next_button='➡️', config=ReactionMenu.STATIC, style="$/&")
    for item in discordias:
        menu.add_page(item)
    await menu.start()

#This command allows the user to see a menu with past results of other online tournaments
@client.command(name="onlines")
async def hof_online_tournaments(ctx):
    online_tours = hall_of_fame.hall_of_fame_onlines_embed()
    menu = ReactionMenu(ctx, back_button='⬅️', next_button='➡️', config=ReactionMenu.STATIC, style="$/&")
    for item in online_tours:
        menu.add_page(item)
    await menu.start()

#This command allows the user to see a menu with past results of offline tournaments
@client.command(name="offlines")
async def hof_offline_tournaments(ctx):
    offline_tours = hall_of_fame.hall_of_fame_offlines_embed()
    menu = ReactionMenu(ctx, back_button='⬅️', next_button='➡️', config=ReactionMenu.STATIC, style="$/&")
    for item in offline_tours:
        menu.add_page(item)
    await menu.start()

#Command para exhibitions embed -> !exhibitions WIP
@client.command(name="exhibitions", aliases = ["exh"])
async def exhibitions(ctx):
    check_if_players = ctx.message.content.split(" ", 1)
    if len(check_if_players) == 1:
        #lista todos os exhibitions
        menu = ReactionMenu(ctx, back_button='⬅️', next_button='➡️', config=ReactionMenu.STATIC, style="$/&")
        exh_list = events.all_exhibitions_embed()
        for item in exh_list:
            menu.add_page(item)
        await menu.start()
    else:
        menu = ReactionMenu(ctx, back_button='⬅️', next_button='➡️', config=ReactionMenu.STATIC, style="$/&")
        players = ctx.message.content.split(" ", 1)[1]
        player_exh_list = events.exhibitions_embed(players)
        for item in player_exh_list:
            menu.add_page(item)
        await menu.start()



#ADMINISTRATOR COMMANDS ----------//-------------//----------------//-------------//-------------//-------------//------------
#This command allows the administrator to create a new event
@client.command(name="addevent")
async def create_tournament(ctx):
    msg = ctx.message.content.split(" ", 1)[1]
    new_event = events.event(msg)
    events.event.add_event(new_event)
    await ctx.send("Insert the date of the event (Example: 18 de outubro de 2021)")
    new_date = await client.wait_for('message', check=lambda message: message.author == ctx.author)
    if new_date.content.lower() == "skip":
        pass
    else:
        events.event.add_event_date(new_event, new_date.content)
    await ctx.send("Insert acronyms or other names by which the event might be known for:\n(Example: For Lutinhas em Lisboa #5, the *aliases* would be: 'LEL5, Lutinhas #5, Lutinhas em Lisboa #5'")
    new_aliases = await client.wait_for('message', check=lambda message: message.author == ctx.author)
    if new_aliases.content.lower() == "skip":
        pass
    else:
        events.event.add_event_aliases(new_event, new_aliases.content)
    await ctx.send("Insert the link for the **brackets**")
    new_brackets = await client.wait_for('message', check=lambda message: message.author == ctx.author)
    if new_brackets.content.lower() == "skip":
        pass
    else:
        check_brackets = events.event.add_event_brackets(new_event, new_brackets.content)
        while check_brackets == 0:
            await ctx.send("ATTENTION: You should only insert ONE link for the brackets! Try again!")
            new_brackets = await client.wait_for('message', check=lambda message: message.author == ctx.author)
            check_brackets = events.event.add_event_brackets(new_event, new_brackets.content)
    await ctx.send("Insert the link of the **poster** for the event")
    new_poster = await client.wait_for('message', check=lambda message: message.author == ctx.author)
    if new_poster.content.lower() == "skip":
        pass
    else:
        events.event.add_event_poster(new_event, new_poster.content)
    await ctx.send("Insert the location for the event")
    new_location = await client.wait_for('message', check=lambda message: message.author == ctx.author)
    if new_location.content.lower() == "skip":
        pass
    else:
        events.event.add_event_location(new_event, new_location.content)   
    await ctx.send("Insert the tournament organizers")
    new_organizers = await client.wait_for('message', check=lambda message: message.author == ctx.author)
    if new_organizers.content.lower() == "skip":
        pass
    else:
        events.event.add_event_organizers(new_event, new_organizers.content)

    await ctx.send("Event added successfully! Use the command !event followed by the name of the event to view it!")

#This command allows the admin to edit an event that was created before (WIP)
@client.command(name="editevent")
async def edit_tournament(ctx):
    menu = ReactionMenu(ctx, back_button='⬅️', next_button='➡️', config=ReactionMenu.STATIC, style="$/&")
    tour_list = events.edit_event_embed()
    for item in tour_list:
        menu.add_page(item)
    await menu.start()
    selected = await client.wait_for('message', check=lambda message: message.author == ctx.author)
    selected_tour = int(selected.content)
    parametro_embed = events.edit_event_parameter_embed()
    await ctx.send(embed=parametro_embed)
    selected_parametro = await client.wait_for('message', check=lambda message: message.author == ctx.author)

'''WIP    
await ctx.send("Insere o vencedor do torneio")
new_winner = await client.wait_for('message', check=lambda message: message.author == ctx.author)
events.event.add_event_winner(new_event, new_winner.content)

await ctx.send("Insere o restante do top 3 por ordem de lugar")
new_top_3 = await client.wait_for('message', check=lambda message: message.author == ctx.author)
events.event.add_event_top_3(new_event, new_top_3.content)

await ctx.send("Insere o link dos VODs do torneio. Se for mais do que um link, deves separá-los por vírgula!")
new_vods = await client.wait_for('message', check=lambda message: message.author == ctx.author)
events.event.add_event_vods(new_event, new_vods.content)
'''

#This section is where CHYNA will perform the action of socializing with other users
@client.event
async def on_message(message):

    await client.process_commands(message)

    chyna_id = 808866968416813076
    target_channel = 798626019564322840 #Currently the channel ID for CHYNA's testing server
    index_count = {}
    msg_words = word_tokenize(message.content)
    if message.channel.id != target_channel:    #CHYNA will not reply to users on other channels
        return
    else:
        for w in msg_words:
            if w in inv_index.keys():
                word_indexes = inv_index[w]
                for i in word_indexes:
                    if i not in index_count.keys():
                        index_count[i] = 0
                    index_count[i] += 1
        highest_index = max(index_count.items(), key=operator.itemgetter(1))[0]
        final_message = history_messages[highest_index-1]   #This is the message sent by CHYNA

    if message.author.id == chyna_id:   #Guarantees CHYNA will not reply to its own messages
        return
    await message.channel.send(final_message)

client.run(token_chyna.token_chyna)
