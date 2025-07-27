import discord
from discord.ext import commands
import json
import asyncio
import os

# Charger la config
with open('config.json') as f:
    config = json.load(f)

TOKEN = config['token']
INVITE_URL = config['invite_url']

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Dossier et fichiers log attendus
LOG_FOLDER = 'log'
SENT_LOG = os.path.join(LOG_FOLDER, 'sent.txt')
ACCEPTED_LOG = os.path.join(LOG_FOLDER, 'accepted.txt')
NOT_ACCEPTED_LOG = os.path.join(LOG_FOLDER, 'not_accepted.txt')

# 🔍 Vérifie que le dossier et les fichiers existent
required_files = [SENT_LOG, ACCEPTED_LOG, NOT_ACCEPTED_LOG]
if not os.path.exists(LOG_FOLDER):
    raise FileNotFoundError(f"❌ Le dossier '{LOG_FOLDER}' est manquant. Crée-le avant d'exécuter le bot.")

for file in required_files:
    if not os.path.isfile(file):
        raise FileNotFoundError(f"❌ Le fichier '{file}' est manquant. Crée-le manuellement dans le dossier log.")

# Liste pour suivre
sent_users = []

@bot.event
async def on_ready():
    print(f'✅ Connecté en tant que {bot.user}')

@bot.command()
async def send_invite(ctx, user: discord.User):
    try:
        await user.send(f"Invitation : {INVITE_URL}")
        print(f'📤 Invitation envoyée à : {user}')
        sent_users.append((user.id, user.name))

        with open(SENT_LOG, 'a') as f:
            f.write(f"{user.id},{user.name}\n")

        await ctx.send(f"Invitation envoyée à {user.name}")

        await asyncio.sleep(60)
        guild = ctx.guild
        member = guild.get_member(user.id)
        if member:
            print(f'✅ {user.name} est déjà dans le serveur')
        else:
            with open(NOT_ACCEPTED_LOG, 'a') as f:
                f.write(f"{user.id},{user.name}\n")
            print(f'❌ {user.name} n\'a pas rejoint (après délai)')

    except Exception as e:
        print(f"❌ Erreur pour {user} : {e}")
        await ctx.send(f"Erreur : {e}")

@bot.event
async def on_member_join(member):
    for uid, uname in sent_users:
        if member.id == uid:
            with open(ACCEPTED_LOG, 'a') as f:
                f.write(f"{member.id},{member.name}\n")
            print(f'✅ {member.name} a accepté l\'invitation')

bot.run(TOKEN)
