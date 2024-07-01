import discord
import random
from discord import Intents, app_commands, Embed
from discord.ui import Button, View
import datetime
from discord.ext import commands

intents = discord.Intents.all()

bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)
guild_id = 1220178595683766322
test_guild_id = 1228208591786344548

record_channel_id = 1239267379679068180
log_channel_id = 1256756422495174668

joined_users = set()

@tree.command(name="lfg", description="Tells users where to go if they are looking for a game!", guild=discord.Object(id=1220178595683766322))
async def lfg(interaction):
    if interaction.user.guild_permissions.kick_members:
        lfge = discord.Embed(
            title="<:HQ_GamerMode:1226036630868066365> Looking for a game?",
            description="Try posting or finding a game in this channel: <#1246841334665445407>\nDiscuss games here: <#1246841530929643570>\nFind the server's ban list: <#1236851970506100746>",
            color=0xff0000
        )
        await interaction.response.send_message("Sent!" , ephemeral=True)
        await interaction.channel.send(embed=lfge)
    else:
        await interaction.response.send_message("This command can only be used by moderators.", ephemeral=True)
                
@tree.command(
    name="admire",
    description="Admire someone anonymously!",
    guild=discord.Object(id=1220178595683766322)
)
async def admire(interaction, member: discord.Member, message: str):
    await interaction.response.send_message("Admired someone! Check out <#1256753957838262373>.", ephemeral=True)
    admired = discord.Embed(
        title=f"Someone admired {member.display_name}! Here's what they said about them.", 
        description=f"{message}", 
        color=0xff0000
    )
    admired.set_thumbnail(
        url="https://cdn.discordapp.com/icons/1220178595683766322/486b8dddba9c69b01571032c00de4f0a.webp?size=1024&format=webp&width=0&height=256"
    )
    admired.set_author(
        name=f"{member.display_name}",
        icon_url=f"{member.avatar.url}"
    )
    admire_channel = bot.get_channel(1256753957838262373)
    await admire_channel.send(f'{member.mention}', embed=admired)
    log_channel = bot.get_channel(log_channel_id)
    await log_channel.send(f"{interaction.user.mention} admired {member.mention}.")

@tree.command(
    name="bt",
    description="Guesses a member as a role",
    guild=discord.Object(id=1220178595683766322)
)
async def bt(interaction, member: discord.Member, role: str):
    await interaction.response.send_message(f"<:HQ_Guesser:1251358890600431686> {member.display_name} was guessed as {role}")

@tree.command(
    name="enter",
    description="Enters the chat.",
    guild=discord.Object(id=1220178595683766322)
)
async def enter(interaction):
    await interaction.response.send_message("Entered!", ephemeral=True)
    entere = discord.Embed(description=f"{interaction.user.mention} entered the chat.", color=0xff0000)
    await interaction.channel.send(embed=entere)

@tree.command(
    name="exit",
    description="Exits the chat.",
    guild=discord.Object(id=1220178595683766322)
)
async def exit(interaction):
    await interaction.response.send_message("Exited!", ephemeral=True)
    exite = discord.Embed(description=f"{interaction.user.mention} exited the chat.", color=0xff0000)
    await interaction.channel.send(embed=exite)

@tree.command(
    name="ping",
    description="Shows the bot's latency",
    guild=discord.Object(id=1220178595683766322)
)
async def ping(interaction):
    ping = round(bot.latency * 1000)
    await interaction.response.send_message(f'Pong! My ping is {ping}ms')


@bot.event
async def on_member_join(member):
    general = bot.get_channel(1220178597940297841)
    
    if general:
        welcome = discord.Embed(description="Make sure to read the rules in <#1220178597008900208>!\nYou can find Among Us game codes in <#1246841334665445407>, and chat about them in <#1246841530929643570>.\nYou can change your name color in <#1226037678105952326>.\nWhen you are ready, begin chatting!", color=0xff0000)
        await general.send(f'Welcome to the server, {member.mention}!', embed=welcome)

@bot.event 
async def on_member_remove(member):
    # Fetch the channel where member leaves will be recorded
    record_channel = bot.get_channel(record_channel_id)

    if record_channel:
        # Send a message to the record channel
        await record_channel.send(f'{member.display_name} has left the server.')

@tree.command(
    name="report",
    description="Makes a report to the staff",
    guild=discord.Object(id=1220178595683766322)
)
async def report(interaction, issue: str):
    await interaction.response.send_message("The staff is on their way!", ephemeral=True)
    report_channel = bot.get_channel(1257024265153282072)
    reporte = discord.Embed(description=f"{issue}", color=0xff0000)
    channel_url = f"https://discord.com/channels/{interaction.guild.id}/{interaction.channel.id}"
    reporte.set_author(
        name=f"{interaction.user.display_name} ({interaction.user.id})",
        icon_url=f"{interaction.user.avatar.url}",
        url=channel_url
    )
    reporte.set_footer(
        text=f"{interaction.channel.name} ({interaction.channel.id})"
    )
    await report_channel.send("<@&1226643701582008391>", embed=reporte)
    await log_channel.send(f"{interaction.user.mention} pinged the staff in {interaction.channel.mention}!")

@tree.command(
    name="hi",
    description="Says hi!",
    guild=discord.Object(id=1220178595683766322)
)
async def hi(interaction):
    log_channel = bot.get_channel(log_channel_id)
    await interaction.response.send_message("Hi!")
    await log_channel.send(f"{interaction.user.mention} used the `/hi` command in {interaction.channel.mention}!")

cooldowns = {}

@tree.command(
    name="tl",
    description="Judges a member",
    guild=discord.Object(id=1220178595683766322)
)
async def bt(interaction, member: discord.Member):
    await interaction.response.send_message(f"{member.display_name} was judged")

@bot.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=1220178595683766322))
    await tree.sync(guild=discord.Object(id=1228208591786344548))
    print("Ready!")
import os
import dotenv
dotenv.load_dotenv()
bot.run(os.getenv('BOT_TOKEN'))
    await tree.sync(guild=discord.Object(id=1228208591786344548))
    print("Ready!")
import os
import dotenv
dotenv.load_dotenv()
bot.run(os.getenv('TOKEN'))
