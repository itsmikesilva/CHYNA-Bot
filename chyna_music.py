import discord
from discord.ext import commands
import youtube_dl
from selenium import webdriver

class Music (commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def play(self, ctx, url):
        if ctx.author.voice == None:    #verifica se o utilizador se encontra em algum voice channel
            await ctx.send("You're not in a voice channel!")
        voice_channel = ctx.author.voice.channel    #nome do voice channel onde se encontra o utilizador para a CHYNA se conectar
        if ctx.voice_client == None:    
            await voice_channel.connect()   #se a CHYNA não estiver conectada em nenhum canal, conecta-se no voice channel respetivo 
        else:
            await ctx.send("CHYNA já se encontra num voice channel.")   #se a CHYNA estiver conectada num canal, transmite uma mensagem e cancela o command
            exit()
        if ctx.voice_client.is_playing():   #se a CHYNA estiver a transmitir áudio, interrompe-o
            ctx.voice_client.stop()

        #este segmento contem as configurações necessárias do FFMPEG e do YouTubeDL para conseguir obter um playable audio
        FFMPEG_OPTIONS = {'before_options' : '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options' : '-vn'}
        YDL_OPTIONS = {'format' : 'bestaudio'}
        vc = ctx.voice_client

        #faz o download da música e transforma-o num playable audio com base nas opções acima
        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            vc.play(source)     #inicio do playback do audio

    @commands.command()
    async def disconnect(self, ctx):
        await ctx.voice_client.disconnect()

    @commands.command()
    async def pause(self, ctx):
        await ctx.voice_client.pause()
        await ctx.send("Song paused!")
    
    @commands.command()
    async def resume(self, ctx):
        await ctx.voice_client.resume()
        await ctx.send("Song resumed!")

def setup(client):
    client.add_cog(Music(client))