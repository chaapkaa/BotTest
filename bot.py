import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()

print("Lancement du bot...")
bot = commands.Bot(command_prefix= '!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot allumé")
    # synchroniser les commandes avec Discord
    try:
        # sync
        synced = await bot.tree.sync()
        print(f"COmmandes slash synchronisées : {len(synced)}")
    except Exception as e:
        print(e)

@bot.event
async def on_message(message: discord.Message):
    # empêcher le bot de répondre à lui-même
    if message.author.bot:
        return
    if message.content == 'Bonjour':
        channel = message.channel
        author = message.author
        await author.send("Comment ça va ?")
    if message.content == 'Bienvenue':
        welcome_channel = bot.get_channel (1421942767281770546)
        await welcome_channel.send(f"Bienvenue {message.author.mention} !")
@bot.tree.command(name="test", description="Tester les embeds")
async def test(interaction: discord.Interaction):
    embed = discord.Embed(title="Test", description="https://www.youtube.com/watch?v=A6d4We0cbX0&t=1562s", color=discord.Color.blue()
    )
    embed.add_field(name="Python", value="Apprendre le python")
    embed.add_field(name="WEB", value="Apprendre le web")

    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="warnguy", description="Alerter une personne")
async def warnguy(interaction: discord.Interaction, member: discord.Member):
    await interaction.response.send_message(f"{member.mention} a été alerté par un modérateur.")
    await member.send("Tu as été alerté par un modérateur.")

@bot.tree.command(name="banguy", description="Bannir une personne")
async def banguy(interaction: discord.Interaction, member: discord.Member):
    await interaction.response.send_message(f"{member.mention} a été banni par un modérateur.")
    await member.ban(reason="Banni par un modérateur")
    try:
        await member.send("Tu as été banni par un modérateur.")
    except Exception as e:
        print(f"Erreur lors de l'envoi du message à {member}: {e}")


@bot.tree.command(name="ping", description="Renvoie Pong!")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong!")

bot.run(os.getenv('DISCORD_TOKEN'))
