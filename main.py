import discord
import random
from discord import Intents, app_commands, Embed
from discord.ui import Button, View
from discord.ext import commands

intents = discord.Intents.all()

bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)
guild_id = 1220178595683766322
test_guild_id = 1228208591786344548

random_messages = ["Lime", "Taya", "Capybara", "Sarha", "Kazi", "Nai", "Captian Orange", "Zanyfee", "Gamer", "Retrodawn", "Firewall", "Laik", "Sky"]

record_channel_id = 1239267379679068180
log_channel_id = 1239314532896084100

joined_users = set()

@tree.command(
    name="join",
    description="Joins the 200 member nitro giveaway event!",
    guild=discord.Object(id=1228208591786344548)
)
async def join(interaction):
    if interaction.user.name in joined_users:
        await interaction.response.send_message(f'{interaction.user.mention}, you have already joined the event!', ephemeral=True)
    else:
        joined_users.add(interaction.user.name)
        await interaction.response.send_message(f'{interaction.user.mention} has joined the event!', ephemeral=True)

        special_channel = bot.get_channel(1232184214024359936)
        if special_channel:
            await special_channel.send(f'{interaction.user.name} has joined the event.')

@tree.command(
    name="ping",
    description="Shows the bot's latency",
    guild=discord.Object(id=1220178595683766322)
)
async def ping(interaction):
    ping = round(bot.latency * 1000)
    await interaction.response.send_message(f'<:goodping:1239662717133000706> Pong! My ping is {ping}ms')

@bot.event 
async def on_member_remove(member):
    # Fetch the channel where member leaves will be recorded
    record_channel = bot.get_channel(record_channel_id)

    if record_channel:
        # Send a message to the record channel
        await record_channel.send(f'{member.display_name} has left the server.')

@tree.command(name="close", description="Closes a post", guild=discord.Object(id=1220178595683766322))
async def close(interaction):
    if interaction.user == interaction.channel.owner or interaction.user.guild_permissions.manage_threads:
        try:
            if isinstance(interaction.channel, discord.Thread):
                log_channel = bot.get_channel(log_channel_id)
                thread_id = interaction.channel.id
                thread = bot.get_channel(thread_id)
                await interaction.response.send_message("Closed!" , ephemeral=True)
                await thread.edit(archived=True, locked=True, name="CLOSED")
                await log_channel.send(f"{interaction.user.mention} used the `/close` command in {interaction.channel.mention}!")
            else:
                await interaction.response.send_message("This command can only be used in a thread.")
        except discord.Forbidden:
            await interaction.channel.send("I don't have permission to close the thread.")
    else:
        await interaction.response.send_message("You can't close this thread.")

@tree.command(name="toh", description="Pings the TOH lobby role", guild=discord.Object(id=1220178595683766322))
async def toh(interaction):
            if isinstance(interaction.channel, discord.Thread):
                log_channel = bot.get_channel(log_channel_id)
                thread_id = interaction.channel.id
                thread_link = f'https://discord.com/channels/{interaction.guild.id}/{thread_id}'
                await interaction.channel.send(f"{thread_link} <@&1220178595704733789>")
                await interaction.response.send_message("Pinged!" , ephemeral=True)
                await log_channel.send(f"{interaction.user.mention} pinged the TOH lobby role in {interaction.channel.mention}!")
            else:
                await interaction.response.send_message("This command can only be used in a thread.")

@tree.command(name="tohe", description="Pings the TOHE lobby role", guild=discord.Object(id=1220178595683766322))
async def tohe(interaction):
        if isinstance(interaction.channel, discord.Thread):
            log_channel = bot.get_channel(log_channel_id)
            thread_id = interaction.channel.id
            thread_link = f'https://discord.com/channels/{interaction.guild.id}/{thread_id}'
            await interaction.channel.send(f"{thread_link} <@&1220178595704733788>")
            await interaction.response.send_message("Pinged!" , ephemeral=True)
            await log_channel.send(f"{interaction.user.mention} pinged the TOHE lobby role in {interaction.channel.mention}!")
        else:
            await interaction.response.send_message("This command can only be used in a thread.")

@tree.command(name="tohy", description="Pings the TOH-Y lobby role", guild=discord.Object(id=1220178595683766322))
async def tohy(interaction):
        if isinstance(interaction.channel, discord.Thread):
            log_channel = bot.get_channel(log_channel_id)
            thread_id = interaction.channel.id
            thread_link = f'https://discord.com/channels/{interaction.guild.id}/{thread_id}'
            await interaction.channel.send(f"{thread_link} <@&1226031538437886002>")
            await interaction.response.send_message("Pinged!" , ephemeral=True)
            await log_channel.send(f"{interaction.user.mention} pinged the TOH-Y lobby role in {interaction.channel.mention}!")
        else:
            await interaction.response.send_message("This command can only be used in a thread.")
@tree.command(name="tor", description="Pings the TOR lobby role", guild=discord.Object(id=1220178595683766322))
async def tor(interaction):
        if isinstance(interaction.channel, discord.Thread):
            log_channel = bot.get_channel(log_channel_id)
            thread_id = interaction.channel.id
            thread_link = f'https://discord.com/channels/{interaction.guild.id}/{thread_id}'
            await interaction.channel.send(f"{thread_link} <@&1220178595704733790>")
            await interaction.response.send_message("Pinged!" , ephemeral=True)
            await log_channel.send(f"{interaction.user.mention} pinged the TOR lobby role in {interaction.channel.mention}!")
        else:
            await interaction.response.send_message("This command can only be used in a thread.")

@tree.command(name="tour", description="Pings the TOU-R lobby role", guild=discord.Object(id=1220178595683766322))
async def tour(interaction):
        # Send a message to the target channel
        if isinstance(interaction.channel, discord.Thread):
            log_channel = bot.get_channel(log_channel_id)
            thread_id = interaction.channel.id
            thread_link = f'https://discord.com/channels/{interaction.guild.id}/{thread_id}'
            await interaction.channel.send(f"{thread_link} <@&1220178595704733792>")
            await interaction.response.send_message("Pinged!" , ephemeral=True)
            await log_channel.send(f"{interaction.user.mention} pinged the TOU-R lobby role in {interaction.channel.mention}!")
        else:
            await interaction.response.send_message("This command can only be used in a thread.")

@tree.command(name="tob", description="Pings the TOB lobby role", guild=discord.Object(id=1220178595683766322))
async def tob(interaction):
        if isinstance(interaction.channel, discord.Thread):
            log_channel = bot.get_channel(log_channel_id)
            thread_id = interaction.channel.id
            thread_link = f'https://discord.com/channels/{interaction.guild.id}/{thread_id}'
            await interaction.channel.send(f"{thread_link} <@&1226031456510545930>")
            await interaction.response.send_message("Pinged!" , ephemeral=True)
            await log_channel.send(f"{interaction.user.mention} pinged the TOB lobby role in {interaction.channel.mention}!")
        else:
            await interaction.response.send_message("This command can only be used in a thread.")

@tree.command(name="vanilla", description="Pings the vanilla lobby role", guild=discord.Object(id=1220178595683766322))
async def vanilla(interaction):
        if isinstance(interaction.channel, discord.Thread):
            log_channel = bot.get_channel(log_channel_id)
            thread_id = interaction.channel.id
            thread_link = f'https://discord.com/channels/{interaction.guild.id}/{thread_id}'
            await interaction.channel.send(f"{thread_link} <@&1220178595683766331>")
            await interaction.response.send_message("Pinged!" , ephemeral=True)
            await log_channel.send(f"{interaction.user.mention} pinged the vanilla lobby role in {interaction.channel.mention}!")
        else:
            await interaction.response.send_message("This command can only be used in a thread.")

@tree.command(name="0cd", description="Pings the 0cd lobby role", guild=discord.Object(id=1220178595683766322))
async def ocd(interaction):
        if isinstance(interaction.channel, discord.Thread):
            log_channel = bot.get_channel(log_channel_id)
            thread_id = interaction.channel.id
            thread_link = f'https://discord.com/channels/{interaction.guild.id}/{thread_id}'
            await interaction.channel.send(f"{thread_link} <@&1220178595704733786>")
            await interaction.response.send_message("Pinged!" , ephemeral=True)
            await log_channel.send(f"{interaction.user.mention} pinged the 0cd lobby role in {interaction.channel.mention}!")
        else:
            await interaction.response.send_message("This command can only be used in a thread.")

@tree.command(name="other", description="Pings the other mod lobby role", guild=discord.Object(id=1220178595683766322))
async def other(interaction):
        if isinstance(interaction.channel, discord.Thread):
            log_channel = bot.get_channel(log_channel_id)
            thread_id = interaction.channel.id
            thread_link = f'https://discord.com/channels/{interaction.guild.id}/{thread_id}'
            await interaction.channel.send(f"{thread_link} <@&1220178595704733787>")
            await interaction.response.send_message("Pinged!" , ephemeral=True)
            await log_channel.send(f"{interaction.user.mention} pinged the other mod lobby role in {interaction.channel.mention}!")
        else:
            await interaction.response.send_message("This command can only be used in a thread.")

@tree.command(
    name="emergency",
    description="Pings the staff",
    guild=discord.Object(id=1220178595683766322)
)
async def emergency(interaction):
    log_channel = bot.get_channel(log_channel_id)
    await interaction.response.send_message("The staff is on their way!", ephemeral=True)
    await interaction.channel.send("<@&1226643701582008391>")
    await log_channel.send(f"{interaction.user.mention} pinged the staff in {interaction.channel.mention}!")

@tree.command(
    name="who",
    description="Random active member in the server",
    guild=discord.Object(id=1220178595683766322)
)
async def who(interaction):
    log_channel = bot.get_channel(log_channel_id)
    random_message = random.choice(random_messages)
    await interaction.response.send_message(random_message)
    await log_channel.send(f"{interaction.user.mention} used the `/who` command in {interaction.channel.mention}!")
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
    name="mafia",
    description="Pings the mafia patrty!",
    guild=discord.Object(id=1220178595683766322)
)
async def mafia(interaction):
    log_channel = bot.get_channel(log_channel_id)
    await interaction.response.send_message("Pinged!", ephemeral=True)
    await interaction.channel.send("<@&1220178595683766328> come join us in the Mafia party!")
    await log_channel.send(f"{interaction.user.mention} pinged the mafia party in {interaction.channel.mention}!")
  

@bot.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=1220178595683766322))
    await tree.sync(guild=discord.Object(id=1228208591786344548))
    print("Ready!")
import os
import dotenv
dotenv.load_dotenv()
bot.run(os.getenv('TOKEN'))