import difflib
import discord

def help_front_page():

    #Front Page Embed
    embed = discord.Embed(title="HELP MENU")
    embed.set_author(name="CHYNA", icon_url="https://cdn.discordapp.com/avatars/808866968416813076/cc650ce022895166abf57e35f4454bc0.webp?size=128")
    embed.add_field(name="INTRODUÇÃO", value="A CHYNA é um Discord Bot cujos objetivos são criar e gerir perfis de jogadores do Tekken Portugal assim como mostrar todo o histórico de eventos, sejam estes torneios ou exhibition matches.")
    embed.set_image(url="https://store-images.s-microsoft.com/image/apps.5743.14512833441604162.53bad18b-8048-4554-bc49-1c0b5643be5b.bc0f22dd-225c-4508-86d0-07ab666f6f5c?mode=scale&q=90&h=720&w=1280&format=jpg")
    return embed

def create_profile_embed():

    #Creating Profile Embed
    embed = discord.Embed(title="HELP MENU")
    embed.set_author(name="CHYNA", icon_url="https://cdn.discordapp.com/avatars/808866968416813076/cc650ce022895166abf57e35f4454bc0.webp?size=128")
    embed.add_field(name="Criar Profile -> Command !sp ou !setprofile", value="A criação do perfil será feita através do command !sp ou !setprofile. O único requisito deste command é o nome do jogador, utilizando o command da seguinte forma:\n\n✅ !sp CHYNA\n\nA CHYNA dará uma resposta de sucesso se este passo tiver sido concluido sem problemas.")
    embed.set_image(url="https://cdn.discordapp.com/attachments/859851768595087390/859855281889214484/unknown.png")
    return embed

def thumbnail_page_embed():

    #Thumbnail Page Embed
    embed = discord.Embed(title="Adicionar MAIN CHARACTER/Thumbnail")
    embed.set_author(name="CHYNA", icon_url="https://cdn.discordapp.com/avatars/808866968416813076/cc650ce022895166abf57e35f4454bc0.webp?size=128")
    embed.add_field(name="Command !t ou !thumbnail", value="O command !t vai permitir o jogador definir a sua MAIN CHARACTER, que irá aparecer no seu perfil. Para este command o jogador deverá inserir o nome da MAIN CHARACTER.\nExemplo do uso do command !t:\n\n✅ !t Anna\n✅ !t Anna Williams")
    embed.set_image(url="https://cdn.discordapp.com/attachments/854306255043428392/854306925645398016/C_ZAF.png")
    return embed

def sub_chars_page_embed():

    #Sub Characters Page Embed -> Adding
    embed1 = discord.Embed(title="Adicionar SUB-CHARACTERS")
    embed1.set_author(name="CHYNA", icon_url="https://cdn.discordapp.com/avatars/808866968416813076/cc650ce022895166abf57e35f4454bc0.webp?size=128")
    embed1.add_field(name="Command !ss ou !setsubs", value="Para os jogadores que gostariam de incluir os seus SUB-CHARACTERS no seu perfil, existe essa opção utilizando o command !ss ou !setsubs.\n\n-O limite de subs é de 3 SUB-CHARACTERS;\n-As characters devem ser separadas por VÍRGULAS;\n\nExemplo do uso do command !ss:\n\n✅ !ss Kunimitsu, Lei, Xiaoyu\n❌ !ss Kunimitsu Lei Xiaoyu")
    embed1.set_image(url="https://cdn.discordapp.com/attachments/854306255043428392/854306925645398016/C_ZAF.png")

    #Sub Characters Page Embed -> Removing
    embed2 = discord.Embed(title="Remover SUB-CHARACTERS")
    embed2.set_author(name="CHYNA", icon_url="https://cdn.discordapp.com/avatars/808866968416813076/cc650ce022895166abf57e35f4454bc0.webp?size=128")
    embed2.add_field(name="Command !rs ou !removesubs", value="O command !rs ou !removesubs irá permitir a remoção de um SUB-CHARACTER da lista do jogador. Este command apenas permite a remoção de um SUB-CHARACTER de cada vez.\n\nExemplo do uso do command !rs:\n\n✅ !rs Shaheen")
    embed2.set_image(url="https://cdn.discordapp.com/attachments/854306255043428392/854306925645398016/C_ZAF.png") 
    return embed1, embed2


def max_rank_page_embed():

    #MAX Rank Page Embed
    embed = discord.Embed(title="Adicionar Season 4 MAX RANK")
    embed.set_author(name="CHYNA", icon_url="https://cdn.discordapp.com/avatars/808866968416813076/cc650ce022895166abf57e35f4454bc0.webp?size=128")
    embed.add_field(name="Command !mr ou !maxrank", value="Gostam de dar show-off? É a vossa oportunidade! O command !mr ou !maxrank permite adicionar o max rank do jogador na season atual. O único requisito deste command é o nome do rank.\n\nExemplo do uso do command !mr:\n\n✅ !sr Tekken God Omega\n❌ !sr TGO")
    embed.set_image(url="https://cdn.discordapp.com/attachments/854306255043428392/854306925645398016/C_ZAF.png")
    return embed

def social_media_page_embed():

    #ADD Social Media Page Embed
    embed1 = discord.Embed(title="Adicionar Social Media")
    embed1.set_author(name="CHYNA", icon_url="https://cdn.discordapp.com/avatars/808866968416813076/cc650ce022895166abf57e35f4454bc0.webp?size=128")
    embed1.add_field(name="Command !sm ou !setsocial", value="Este será o espaço para o jogador partilhar as suas redes sociais. O command !sm ou !set social apenas usa um requisito: o link da social media.\nNOTA: Se o link não estiver em forma de hiperligação, não será válido.\n\nExemplo do uso do command !sr:\n\n✅ !sm https://twitter.com/tekkenportugal\n❌ !sm twitter.com/tekkenportugal")
    embed1.set_image(url="https://cdn.discordapp.com/attachments/854306255043428392/854306925645398016/C_ZAF.png")

    #REMOVE Social Media Page Embed
    embed2 = discord.Embed(title="Remover Social Media")
    embed2.set_author(name="CHYNA", icon_url="https://cdn.discordapp.com/avatars/808866968416813076/cc650ce022895166abf57e35f4454bc0.webp?size=128")
    embed2.add_field(name="Command !rm ou !removesocial", value="Para remover uma social media, o jogador pode utilizar o command !rm ou !removesocial. O único requisito deste command é o NOME da social media.\n\nExemplo do uso do command !rm:\n\n✅ !rm twitter\n❌ !rm https://twitter.com/tekkenportugal")
    embed2.set_image(url="https://cdn.discordapp.com/attachments/854306255043428392/854306925645398016/C_ZAF.png")

    return embed1, embed2

def user_description_embed():

    #Description Page Embed
    embed = discord.Embed(title="Descrição do Jogador")
    embed.set_author(name="CHYNA", icon_url="https://cdn.discordapp.com/avatars/808866968416813076/cc650ce022895166abf57e35f4454bc0.webp?size=128")
    embed.add_field(name="Command !d ou !description", value="Este command permite ao jogador falar-nos um pouco sobre ele (ou então fazer memes). O céu é o limite, então dêem asas à vossa imaginação!\nNOTA: A descrição tem um limite de 250 caracteres.\n\nExemplo do uso do command !d:\n\n✅ !d Sou melhor que o Knee.")
    embed.set_image(url="https://cdn.discordapp.com/attachments/854306255043428392/854306925645398016/C_ZAF.png")
    return embed

def esports_team_embed():

    #Add E-Sports Team Embed
    embed1 = discord.Embed(title="Adicionar E-Sports Team")
    embed1.set_author(name="CHYNA", icon_url="https://cdn.discordapp.com/avatars/808866968416813076/cc650ce022895166abf57e35f4454bc0.webp?size=128")
    embed1.add_field(name="Command !se ou !setesports", value="Juntaram-se a alguma team? Com o command !se ou !setesports podem partilhar com o mundo! O único requisito deste command é o nome/sigla da team!\n\nExemplo do uso do command !se:\n\n✅ !se FTW.")
    embed1.set_image(url="https://cdn.discordapp.com/attachments/854306255043428392/854306925645398016/C_ZAF.png")

    #Remove E-Sports Team Embed
    embed2 = discord.Embed(title="Remover E-Sports Team")
    embed2.set_author(name="CHYNA", icon_url="https://cdn.discordapp.com/avatars/808866968416813076/cc650ce022895166abf57e35f4454bc0.webp?size=128")
    embed2.add_field(name="Command !re ou !removeesports", value="O command !re ou !removeesports remove a team que o jogador tenha previamente adicionado ao seu perfil. NÃO É necessário nenhum texto para além do command\n\nExemplo do uso do command !re:\n\n✅ !re")
    embed2.set_image(url="https://cdn.discordapp.com/attachments/854306255043428392/854306925645398016/C_ZAF.png")
    return embed1, embed2

def name_change_embed():

    #name change page embed
    embed = discord.Embed(title="Alterar Nome de Jogador")
    embed.set_author(name="CHYNA", icon_url="https://cdn.discordapp.com/avatars/808866968416813076/cc650ce022895166abf57e35f4454bc0.webp?size=128")
    embed.add_field(name="Command !cn ou !changename", value="Se o jogador desejar alterar o seu nome de jogador, pode fazê-lo com o command !cn ou !changename. O único requisito deste command é o novo nome do jogador.\n\nExemplo do uso do command !cn:\n\n✅ !cn CHYNA 2000.")
    embed.set_image(url="https://cdn.discordapp.com/attachments/854306255043428392/854306925645398016/C_ZAF.png")
    return embed

def profile_embed():

    #profile page embed
    embed = discord.Embed(title="Visualizar Perfis")
    embed.set_author(name="CHYNA", icon_url="https://cdn.discordapp.com/avatars/808866968416813076/cc650ce022895166abf57e35f4454bc0.webp?size=128")
    embed.add_field(name="Command !p ou !profile", value="Os jogadores podem ver os seus próprios perfis e de outros jogadores utilizando o command !p ou !profile. O único requisito deste command é o nome do jogador cujo perfil o utilizador pretende visualizar.\n\nExemplo do uso do command !p:\n\n✅ !p CHYNA.")
    embed.set_image(url="https://cdn.discordapp.com/attachments/854306255043428392/854306925645398016/C_ZAF.png")
    return embed

def tournament_results_page_embed():

    #add tournament results page embed
    embed1 = discord.Embed(title="Adicionar Resultados de Torneios")
    embed1.set_author(name="CHYNA", icon_url="https://cdn.discordapp.com/avatars/808866968416813076/cc650ce022895166abf57e35f4454bc0.webp?size=128")
    embed1.add_field(name="Command !tr ou !results", value="O jogador pode manter registo dos seus resultados de torneios adicionando-os ao perfil com o command !tr ou !results.\n\n➡ Os resultados devem ser separados por um '/'\n\nExemplo do uso do command !tr:\n\n✅ !tr 2º lugar no Lutinhas em Lisboa #38 / 5º lugar no Braga Fight Fest #4 / Derrotei o Knee.\n❌ !tr 2º lugar no Lutinhas em Lisboa #38, 5º lugar no Braga Fight Fest #4, Derrotei o Knee. ")
    embed1.set_image(url="https://cdn.discordapp.com/attachments/854306255043428392/854306925645398016/C_ZAF.png")
    
    #remove tournament results page embed
    embed2 = discord.Embed(title="Remover Resultados de Torneios")
    embed2.set_author(name="CHYNA", icon_url="https://cdn.discordapp.com/avatars/808866968416813076/cc650ce022895166abf57e35f4454bc0.webp?size=128")
    embed2.add_field(name="Command !rr ou !removeresults", value="O jogador pode remover os seus resultados através do command !rr. Não há requisitos para este command.\n\nComo funciona:\n\n➡ A CHYNA vai apresentar a lista dos resultados do jogador;\n➡ O jogador vai escolher o número correspondente ao resultado que pretende remover.\n\nExemplo do uso do command !rr:")
    embed2.set_image(url="https://cdn.discordapp.com/attachments/854306255043428392/854306925645398016/C_ZAF.png")

    #edita tournament results page embed
    embed3 = discord.Embed(title="Editar Resultados de Torneios")
    embed3.set_author(name="CHYNA", icon_url="https://cdn.discordapp.com/avatars/808866968416813076/cc650ce022895166abf57e35f4454bc0.webp?size=128")
    embed3.add_field(name="Command !er ou !editresults", value="Existe a opção de editar resultados de torneios com o command !er ou !editresults. Não há requisitos para este command.\n\nComo funciona:\n\n➡ A CHYNA vai apresentar a lista dos resultados do jogador;\n➡ O jogador escolhe o número correspondente ao resultado que pretende editar;\n➡ Após este passo, o jogador deve introduzir o novo resultado que substituirá o selecionado.\n\nExemplo do uso do command !er:")
    embed3.set_image(url="https://cdn.discordapp.com/attachments/854306255043428392/854306925645398016/C_ZAF.png")

    #escolhe até 3 tournament results page embed
    embed4 = discord.Embed(title="Escolher Principais Resultados de Torneios")
    embed4.set_author(name="CHYNA", icon_url="https://cdn.discordapp.com/avatars/808866968416813076/cc650ce022895166abf57e35f4454bc0.webp?size=128")
    embed4.add_field(name="Command !pr ou !pickresults", value="O perfil do jogador irá apresentar apenas 3 resultados de torneios na sua página principal. Este command permite ao jogador escolher os seus resultados mais importantes/favoritos. Não há requisitos para este command.\n\nComo funciona:\n\n- A CHYNA vai apresentar a lista dos resultados do jogador;\n- O jogador escolhe os números correspondentes aos resultados que pretende mostrar na sua página principal.\n\n➡ Limite de resultados escolhidos é de 3.\n➡ Os números selecionados devem ser separados por VÍRGULAS.\n\nExemplo do uso do command !pr:")
    embed4.set_image(url="https://cdn.discordapp.com/attachments/854306255043428392/854306925645398016/C_ZAF.png")

    return embed1, embed2, embed3, embed4

#adicionar vods
def set_vods_embed():
    embed = discord.Embed(title="Adicionar Videos/Clipes do Jogador")
    embed.set_author(name="CHYNA", icon_url="https://cdn.discordapp.com/avatars/808866968416813076/cc650ce022895166abf57e35f4454bc0.webp?size=128")
    embed.add_field(name="Command !sv ou !setvods", value="Para adicionar videos, clipes e highlights ao perfil, o jogador deve utilizar o command !sv ou !setvods seguido dos links dos videos desejados, separando-os através de vírgulas.\n\nExemplo do uso do command !sv:\n\n✅ !sv https://www.youtube.com/watch?v=lGTRUN0tqVk, https://www.youtube.com/watch?v=XvBE4Op7boI\n❌ !sv https://www.youtube.com/watch?v=lGTRUN0tqVk https://www.youtube.com/watch?v=XvBE4Op7boI")
    embed.set_image(url="https://cdn.discordapp.com/attachments/854306255043428392/854306925645398016/C_ZAF.png")

    return embed

#remover vods
def remove_vods_embed():

    embed = discord.Embed(title="Remover Videos/Clipes do Jogador")
    embed.set_author(name="CHYNA", icon_url="https://cdn.discordapp.com/avatars/808866968416813076/cc650ce022895166abf57e35f4454bc0.webp?size=128")
    embed.add_field(name="Command !rv ou !removevods", value="Para remover vídeos do perfil, o jogador deve utilizar o command !rv ou !removevods. Este command não tem requisitos. Ao receber o command !rv, a CHYNA perguntará qual dos VODs o jogador pretende remover. O jogador deve enviar uma mensagem com o número respetivo\n\nExemplo do uso do command !rv")
    embed.set_image(url="https://cdn.discordapp.com/attachments/854306255043428392/854306925645398016/C_ZAF.png")
    
    return embed

def call_command_help_embed(message):

    if message == "!m" or message == "!manual" or message == 0:
        return 1
    elif message == "!sp" or message == "!setprofile" or message == 1:
        embed = create_profile_embed()
    elif message == "!t" or message == "!thumbnail" or message == 2:
        embed = thumbnail_page_embed()
    elif message == "!ss" or message == "!setsubs" or message == 3:
        embed, not_embed = sub_chars_page_embed()
    elif message == "!rs" or message == "!removesubs" or message == 4:
        not_embed, embed = sub_chars_page_embed()
    elif message == "!mr" or message == "!maxrank" or message == 5:
        embed = max_rank_page_embed()
    elif message == "!d" or message == "!description" or message == 6:
        embed = user_description_embed()
    elif message == "!sm" or message == "!setsocial" or message == 7:
        embed, not_embed = social_media_page_embed()
    elif message == "!rm" or message == "!removesocial" or message == 8:
        not_embed, embed = social_media_page_embed()
    elif message == "!se" or message == "!setesports" or message == 9:
        embed, not_embed = esports_team_embed()
    elif message == "!re" or message == "!removeesports" or message == 10:
        not_embed, embed = esports_team_embed()
    elif message == "!cn" or message == "!changename" or message == 11:
        embed = name_change_embed()
    elif message == "!p" or message == "!profile" or message == 12:
        embed = profile_embed()
    elif message == "!tr" or message == "!results" or message == 13:
        embed, not_embed, not_embed1, not_embed2 = tournament_results_page_embed()
    elif message == "!rr" or message == "!removeresults" or message == 14:
        not_embed, embed, not_embed1, not_embed2 = tournament_results_page_embed()
    elif message == "!er" or message == "!editresults" or message == 15:
        not_embed, not_embed1, embed, not_embed2 = tournament_results_page_embed
    elif message == "!pr" or message == "!pickresults" or message == 16:
        not_embed, not_embed1, not_embed2, embed = tournament_results_page_embed()
    elif message == "sv" or message == "!setvods" or message == 17:
        embed = set_vods_embed()
    elif message == "rv" or message == "!removevods" or message == 18:
        embed = remove_vods_embed()
    else:
        return 0
    
    return embed

def show_commands_embed():

    commands_string_1 = "0- !m ou !manual\n1- !sp ou !setprofile\n2- !t ou !thumbnail\n3- !ss ou !setsubs\n4- !rs ou !removesubs\n5- !mr ou !maxrank\n6- !d ou !description\n7- !sm ou !setsocial\n8- !rm ou!removesocial\n9- !se ou !setesports"
    commands_string_2 = "10- !re ou !removeesports\n11- !cn ou! changename\n12- !p ou !profile\n13- !tr ou !results\n14- !rr ou !removeresults\n15- !er ou !editresults\n16- !pr ou !pickresults\n17- !sv ou !setvods"
    embed1 = discord.Embed(title="LISTA DE COMANDOS")
    embed1.set_author(name="CHYNA", icon_url="https://cdn.discordapp.com/avatars/808866968416813076/cc650ce022895166abf57e35f4454bc0.webp?size=128")
    embed1.add_field(name="Escolhe o número do command para obter informação sobre ele:", value=commands_string_1)
    embed1.set_image(url="https://cdn.discordapp.com/attachments/854306255043428392/854306925645398016/C_ZAF.png")

    embed2 = discord.Embed(title="LISTA DE COMANDOS")
    embed2.set_author(name="CHYNA", icon_url="https://cdn.discordapp.com/avatars/808866968416813076/cc650ce022895166abf57e35f4454bc0.webp?size=128")
    embed2.add_field(name="Escolhe o número do command para obter informação sobre ele:", value=commands_string_2)
    embed2.set_image(url="https://cdn.discordapp.com/attachments/854306255043428392/854306925645398016/C_ZAF.png")
    return embed1, embed2