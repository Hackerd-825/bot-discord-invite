import discord
from discord.ext import commands
import json
import asyncio
import os
import sys
# crée par hackerd_825
# https://github.com/Hackerd-825/

# Pour Windows : fixer le bug avec aiodns
if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# Charger la config
with open('config.json') as f:
    config = json.load(f)

TOKEN = config['token']
INVITE_URL = config['invite_url']

# Activer TOUS les intents nécessaires
intents = discord.Intents.default()
intents.members = True
intents.message_content = True  # IMPORTANT : autorise la lecture du contenu des messages

bot = commands.Bot(command_prefix='!', intents=intents)

# Dossier et fichiers log attendus
LOG_FOLDER = 'log'
SENT_LOG = os.path.join(LOG_FOLDER, 'sent.txt')
ACCEPTED_LOG = os.path.join(LOG_FOLDER, 'accepted.txt')
NOT_ACCEPTED_LOG = os.path.join(LOG_FOLDER, 'not_accepted.txt')

# Vérifier que le dossier et les fichiers existent
required_files = [SENT_LOG, ACCEPTED_LOG, NOT_ACCEPTED_LOG]
if not os.path.exists(LOG_FOLDER):
    raise FileNotFoundError(f"❌ Le dossier '{LOG_FOLDER}' est manquant. Crée-le avant d'exécuter le bot.")

for file in required_files:
    if not os.path.isfile(file):
        raise FileNotFoundError(f"❌ Le fichier '{file}' est manquant. Crée-le manuellement dans le dossier log.")

# Liste pour suivre les utilisateurs invités
sent_users = []

@bot.event
async def on_ready():
    print(f'✅ Connecté en tant que {bot.user}')

@bot.command()
async def invite(ctx, member: discord.Member):
    """Commande : !invite @User ➜ Envoie l'invitation en MP"""
    try:
        await member.send(f"Salut {member.name} ! Voici une invitation : {INVITE_URL}")
        print(f'📤 Invitation envoyée à : {member} ({member.id})')

        sent_users.append((member.id, member.name))

        with open(SENT_LOG, 'a') as f:
            f.write(f"{member.id},{member.name}\n")

        await ctx.send(f"✅ Invitation envoyée à {member.mention}")

        # Attendre 60 secondes pour vérifier s'il a rejoint
        await asyncio.sleep(60)

        guild = ctx.guild
        if guild.get_member(member.id):
            print(f'✅ {member.name} est déjà dans le serveur !')
        else:
            with open(NOT_ACCEPTED_LOG, 'a') as f:
                f.write(f"{member.id},{member.name}\n")
            print(f'❌ {member.name} n\'a pas rejoint après 60s')

    except Exception as e:
        print(f"❌ Erreur pour {member} : {e}")
        await ctx.send(f"Erreur pour {member.mention} : {e}")

@bot.event
async def on_member_join(member):
    """Quand un membre rejoint ➜ On vérifie si c'est un invité"""
    for uid, uname in sent_users:
        if member.id == uid:
            with open(ACCEPTED_LOG, 'a') as f:
                f.write(f"{member.id},{member.name}\n")
            print(f'✅ {member.name} a accepté l\'invitation !')

bot.run(TOKEN)
