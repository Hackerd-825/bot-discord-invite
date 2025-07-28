import discord
from discord.ext import commands
import asyncio
import json
import sys
import os

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# Charger config
with open('config.json') as f:
    config = json.load(f)

TOKEN = config['token']
INVITE_URL = config['invite_url']

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Connecté en tant que {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"✅ {len(synced)} commande(s) slash synchronisée(s).")
    except Exception as e:
        print(f"❌ Erreur de sync : {e}")

# Commande de test
@bot.tree.command(name="ping", description="Répond Pong !")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("🏓 Pong !")

# Commande pour envoyer une invitation en MP
@bot.tree.command(name="invite", description="Envoie un lien d'invitation en MP")
async def invite(interaction: discord.Interaction, member: discord.Member):
    try:
        await member.send(f"👉 Voici ton invitation : {INVITE_URL}")
        await interaction.response.send_message(f"✅ Invitation envoyée à {member.display_name} en MP !", ephemeral=True)
    except Exception as e:
        await interaction.response.send_message(f"❌ Erreur : {e}", ephemeral=True)

bot.run(TOKEN)
