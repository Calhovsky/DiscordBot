import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import asyncio
from config import BOT_TOKEN
from config import user_audio_mapping
from gui import GUI

# Configuração do bot
#prefix = "!"  # Prefixo dos comandos do bot
ffmpeg_path = "C:/Users/pedro/ffmpeg/bin/ffmpeg.exe"
intents = discord.Intents.default()
intents.voice_states = True

# Inicialização do bot
bot = commands.Bot(command_prefix="", intents=intents)

@bot.event
async def on_ready():
    print("Bot pronto!")

@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None:
        # Verifica se algum user entrou num canal de voz
        voice_channel = after.channel
        if member.bot:  # Verifica se o user é um bot
            return
        if str(member.id) in user_audio_mapping:
            audio_file = user_audio_mapping[str(member.id)]
            audio_source = FFmpegPCMAudio(audio_file,executable=ffmpeg_path)
            voice_client = await voice_channel.connect()
            voice_client.play(audio_source)
            while voice_client.is_playing():
                await asyncio.sleep(1)
            await voice_client.disconnect()

bot.run(BOT_TOKEN)