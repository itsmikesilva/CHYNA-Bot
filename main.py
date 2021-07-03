import discord
import profile_embeds
import wishlists
import hall_of_fame
import help_embed
from reactionmenu import ReactionMenu, Button, ButtonType
from discord.ext import commands
import token_chyna

client = commands.Bot(command_prefix = "!")
client.remove_command("help")

@client.event
async def on_ready():
    print("CHYNA is ready!")

#Command para o manual/guide
@client.command(name="manual", aliases=["m"])
async def help_menu(ctx):
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
    await menu.start()

@client.command(name="helpcommands", aliases=["help"])
async def help_commands(ctx):
    msg = ctx.message.content.split(" ")
    if len(msg) > 1:
        command_embed = help_embed.call_command_help_embed(msg[1])
        try:
            if command_embed == 0:
                await ctx.send("Command não foi encontrado!")
            await ctx.send(embed=command_embed)
        except AttributeError:
            pass
    elif len(msg) == 1:
        menu = ReactionMenu(ctx, back_button='⬅️', next_button='➡️', config=ReactionMenu.STATIC, style="$/&")
        command_menu1, command_menu2 = help_embed.show_commands_embed()
        menu.add_page(command_menu1)
        menu.add_page(command_menu2)
        await menu.start()
        user_input = await client.wait_for('message', check=lambda message: message.author == ctx.author)
        command_number = int(user_input.content)
        chosen_command_embed = help_embed.call_command_help_embed(command_number)
        await ctx.send(embed=chosen_command_embed)

#Command para criar o profile do jogador
@client.command(name="setprofile", aliases=["sp"])
async def setprofile(ctx):
    msg = ctx.message.content.split(" ", 1)[1]
    discord_user_id = ctx.message.author.id
    check_if_profile_exists = profile_embeds.create_profile(discord_user_id,msg)
    if check_if_profile_exists == 1:
        await ctx.send("Perfil criado com sucesso!")
    else:
        await ctx.send("Já existe um perfil para este utilizador!")

#Command para visualizar profiles de vários jogadores
@client.command(name="profile", aliases=["p"])
async def profile(ctx):
    msg = ctx.message.content.split(" ", 1)[1]
    check_if_profile_exists = profile_embeds.find_profile(msg.lower())
    if check_if_profile_exists == 0:
        await ctx.send("Perfil inexistente!")
    else:
        menu = ReactionMenu(ctx, back_button='⬅️', next_button='➡️', config=ReactionMenu.STATIC, style="$/&")
        searched_profile = profile_embeds.profile_embed(msg.lower())
        tournament_results = profile_embeds.tournament_results_embed(msg.lower())
        menu.add_page(searched_profile)
        if tournament_results != 0:
            menu.add_page(tournament_results)
        await menu.start()

#Command para adicionar/editar uma thumbnail
@client.command(name="thumbnail", aliases=["t"])
async def set_thumbnail(ctx):
    msg = ctx.message.content.split(" ", 1)[1]
    discord_user_id = ctx.message.author.id
    check_if_char_exists = profile_embeds.add_thumbnail(msg, discord_user_id)
    if check_if_char_exists == 0:
        await ctx.send("A personagem não foi identificada! (DICA: Em geral, deves utilizar o primeiro nome da personagem. Para os casos excecionais, segue conforme os exemplos)\n**Personagens com UM nome**: !st Marduk; !st Anna; !st Jin\n**Personagens com MAIS DO QUE UM nome**: !st Lucky Chloe; !st Master Raven")
    else:
        await ctx.send("Thumbnail adicionada com sucesso!")

#Command para adicionar o max rank
@client.command(name="maxrank", aliases=["mr"])
async def set_max_rank(ctx):
    msg = ctx.message.content.split(" ", 1)[1]
    discord_user_id = ctx.message.author.id
    check_if_rank_exists = profile_embeds.add_max_rank(msg, discord_user_id)
    if check_if_rank_exists == 0:
        await ctx.send("Rank não foi encontrado! (DICA: Se o rank tiver mais que uma palavra, escreve-o por extenso. Embora não seja case-sensitive, abreviações não vão resultar para esses casos.)\n\nExemplo: !sr tgo ❌ !sr tekken god omega ✅")
    else:
        await ctx.send("Season 4 MAX RANK adicionado com sucesso!")

#Command para adicionar sub characters
@client.command(name="setsubs", aliases=["ss"])
async def set_sub_characters(ctx):
    msg = ctx.message.content.split(" ", 1)[1]
    discord_user_id = ctx.message.author.id
    check_if_sub_limit = profile_embeds.add_sub_characters(msg, discord_user_id)
    if check_if_sub_limit == 0:
        await ctx.send("Limite de SUB-CHARACTERS excedido! (MAX 3)\n\n**DICA:** Se pretenderes remover uma SUB-CHARACTER, utiliza o command !rs junto do nome da personagem. Exemplo: !rs Heihachi")
    elif check_if_sub_limit == -1:
        await ctx.send("A MAIN CHARACTER não pode ser uma SUB-CHARACTER! (DICA: No caso em que pretendas alterar a tua main character, utiliza o comando !st para definires a nova main character/thumbnail.)")
    elif check_if_sub_limit == 2:
        await ctx.send("A personagem selecionada não existe!")
    elif check_if_sub_limit == 3:
        await ctx.send("A personagem selecionada já era previamente uma das SUB-CHARACTERS!")
    else:
        await ctx.send("SUB-CHARACTER(S) adicionada(s) com sucesso!\n\n **NOTA:**\nSe algum dos SUB-CHARACTERS não tiver sido inserido como esperado, utiliza o command de ajuda '!h !ss'")

#Command para remover sub characters
@client.command(name="removesubs", aliases=["rs"])
async def delete_sub_characters(ctx):
    msg = ctx.message.content.split(" ", 1)[1]
    discord_user_id = ctx.message.author.id
    check_removal_success = profile_embeds.remove_sub_characters(msg, discord_user_id)
    if check_removal_success == 0:
        await ctx.send("Personagem não encontrada na lista de SUB-CHARACTERS!")
    else:
        await ctx.send("SUB-CHARACTER removida com sucesso!")

#Command para adicionar social medias
@client.command(name="setsocial", aliases=["sm"])
async def set_social_media(ctx):
    msg = ctx.message.content.split(" ", 1)[1]
    discord_user_id = ctx.message.author.id
    check_if_link_works = profile_embeds.add_social_media(msg, discord_user_id)
    if check_if_link_works == 0:
        await ctx.send("Social Media adicionada com sucesso!")
    elif check_if_link_works == -1:
        await ctx.send("Link de Social Media inválido!")

#Command para remover social medias
@client.command(name="removesocial", aliases=["rm"])
async def delete_social_media(ctx):
    msg = ctx.message.content.split(" ", 1)[1]
    discord_user_id = ctx.message.author.id
    check_if_social_exist = profile_embeds.remove_social_media(msg, discord_user_id)
    if check_if_social_exist == 1:
        await ctx.send("Social Media removida com sucesso!")
    elif check_if_social_exist == -1:
        await ctx.send("Não foram encontradas Social Medias.")
    elif check_if_social_exist == 0:
        await ctx.send(msg.capitalize() + " não foi encontrado no perfil deste utilizador.")

#Command para alterar o player name
@client.command(name="changename", aliases=["cn"])
async def change_name(ctx):
    msg = ctx.message.content.split(" ", 1)[1]
    discord_user_id = ctx.message.author.id
    profile_embeds.name_change(msg, discord_user_id)
    await ctx.send("Nome de jogador alterado com sucesso!")

#Command para adicionar uma breve descrição
@client.command(name="description", aliases=["d"])
async def player_description(ctx):
    limit = 250
    msg = ctx.message.content.split(" ", 1)[1]
    discord_user_id = ctx.message.author.id
    check_if_exceeds_limit = profile_embeds.description(msg, discord_user_id)
    if check_if_exceeds_limit == 0:
        await ctx.send("Limite de mensagem excedido! (" + str(limit) + ")")
    else:
        await ctx.send("Descrição do jogador adicionada/alterada com sucesso!")

#Command para adicionar tournament results
@client.command(name="results", aliases=["tr"])
async def add_accolades(ctx):
    msg = ctx.message.content.split(" ", 1)[1]
    discord_user_id = ctx.message.author.id
    profile_embeds.tournament_results(msg, discord_user_id)
    await ctx.send("Tournament Results adicionados com sucesso!")

#Command para editar tournament results
@client.command(name="editresults", aliases=["er"])
async def edit_accolades(ctx):
    discord_user_id = ctx.message.author.id
    accolades_list = profile_embeds.tournament_results_list(discord_user_id)
    accolades_embed = profile_embeds.edit_tournament_results_interface(accolades_list)
    await ctx.send(embed=accolades_embed)

    msg = await client.wait_for('message', check=lambda message: message.author == ctx.author)
    number = int(msg.content)
    await ctx.send("Insere aqui o novo tournament result/accomplishment que irá substituir o escolhido anteriormente.")
    new_msg = await client.wait_for('message', check=lambda message: message.author == ctx.author)
    check_if_in_range = profile_embeds.edit_tournament_results_final(new_msg.content, number, discord_user_id)
    if check_if_in_range == 0:
        await ctx.send("Fora dos limites! (O número selecionado não pertence à lista)")
    else:
        await ctx.send("Tournament Result alterado com sucesso!")

#Command para remover tournament results
@client.command(name="removeresults", aliases=["rr"])
async def delete_accolades(ctx):
    discord_user_id = ctx.message.author.id
    accolades_list = profile_embeds.tournament_results_list(discord_user_id)
    accolades_embed = profile_embeds.remove_tournament_results_interface(accolades_list)
    await ctx.send(embed=accolades_embed)

    msg = await client.wait_for('message', check=lambda message: message.author == ctx.author)
    number = int(msg.content)
    check_if_in_range = profile_embeds.remove_tournament_results_final(number, discord_user_id)
    if check_if_in_range == 0:
        await ctx.send("Fora dos limites! (O número selecionado não pertence à lista.)")
    else:
        await ctx.send("Tournament Result removido com sucesso!")

#Command para pickar top 3 tournament results
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
        await ctx.send("Escolhe um máximo de TRÊS tournament results. (Limite excedido)")
    elif check_if_valid == -1:
        await ctx.send("Input inválido. (Digita apenas NÚMEROS separados por uma vírgula e um espaço. Exemplo: 4, 2, 5)")
    elif check_if_valid == -2:
        await ctx.send("Fora dos limites! (O número selecionado não faz parte da lista)")
    elif check_if_valid == 1:
        await ctx.send("Resultados atualizados! Verifica as mudanças digitando '!p Profile Name'")

#Command para adicionar E-Sports Team
@client.command(name="setesports", aliases=["se"])
async def add_esports_team(ctx):
    msg = ctx.message.content.split(" ", 1)[1]
    discord_user_id = ctx.message.author.id
    profile_embeds.set_esports_team(msg,discord_user_id)
    await ctx.send("E-Sports Team atualizada!")

#Command para adicionar E-Sports Team
@client.command(name="removeesports", aliases=["re"])
async def delete_esports_team(ctx):
    discord_user_id = ctx.message.author.id
    check_if_esports_team = profile_embeds.remove_esports_team(discord_user_id)
    if check_if_esports_team == 0:
        await ctx.send("Não existe uma E-Sports Team atríbuida a este perfil.")
    else:
        await ctx.send("E-Sports Team removida com sucesso!")

#Command para adicionar VODs
#BIIIIIIIG WIP
@client.command(name="setvods", aliases=["sv"])
async def set_vods(ctx):
    vod_link = ctx.message.content.split(" ", 1)[1]
    discord_user_id = ctx.message.author.id
    check_vod_success = profile_embeds.add_vods(vod_link, discord_user_id)

#ADMINISTRATOR COMMANDS ----------//-------------//----------------//-------------//-------------//-------------//------------
#Command para HOF Discórdias Embed
@client.command(name="hofdiscordias", aliases=["hd"])
async def hof_discordias(ctx):
    hof_discordias_embed1, hof_discordias_embed2 = hall_of_fame.hall_of_fame_discordias_embed()
    menu = ReactionMenu(ctx, back_button='⬅️', next_button='➡️', config=ReactionMenu.STATIC, style="$/&")
    menu.add_page(hof_discordias_embed1)
    menu.add_page(hof_discordias_embed2)
    await menu.start()


#VALENTINE'S DAY STUFF
@client.command()
async def valentine(ctx):
    if (ctx.message.channel.id != 809586931323109416):
        return
    
    f = discord.File('JAN.pdf')
    await ctx.send(file=f)


@client.command()
async def funsies(ctx):
    if (ctx.message.channel.id != 809586931323109416):
        return

    img = discord.File('joguinho.jpg')
    clues = discord.File('clues.jpg')
    await ctx.send(file=img)
    await ctx.send(file=clues)

#WISHLIST STUFF
@client.command()
async def wishlist(ctx):
    if (ctx.message.channel.id != 809586931323109416):
        return
    msg = ctx.message.content.split()[1]
    final_wishlist = wishlists.get_wishlist(msg)
    await ctx.send(final_wishlist)

@client.command(name="wishlistadd", aliases=["wa"])
async def wishlistadd(ctx):
    if (ctx.message.channel.id != 809586931323109416):
        return
    msg = ctx.message.content.split(" ", 1)[1]
    if ctx.message.author.id == 135895383686512640:
        wishlists.add_to_wishlist_jan(msg)
    elif (ctx.message.author.id == 220318176792150018):
        wishlists.add_to_wishlist_mike(msg)
    await ctx.send("Wishlist entry added successfully!")

@client.command(name="wishlistremove", aliases=["wr"])
async def wishlistremove(ctx):
    if (ctx.message.channel.id != 809586931323109416):
        return
    msg = ctx.message.content
    ix = int(msg.split()[1]) - 1
    if ctx.message.author.id == 135895383686512640:
        wishlists.remove_from_wishlist_jan(ix)
    elif (ctx.message.author.id == 220318176792150018):
        wishlists.remove_from_wishlist_mike(ix)

client.run(token_chyna.token_chyna)
