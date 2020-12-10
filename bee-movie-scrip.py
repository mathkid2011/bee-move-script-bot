import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound
import time

client = commands.Bot(command_prefix = ".")
client.remove_command('help')

file = open('acc-bee-scrip.txt', 'r')
lines = file.readlines()
file.close()

async def start_script(channel_id, cont):
    channel = client.get_channel(channel_id)
    await channel.send(f'Starting: the bee movie script one line at per a hour brought to u by sir tompham hats drunk brain')

    for line in lines:
        time.sleep(2)
        if len(line.strip())<3:
            continue
        await channel.send(line)
        if cont==False:
            break
        
    

@client.command()
async def start(ctx):
    await start_script(ctx.channel.id, True)


@client.command()
async def stopdaddypls(ctx):
    await ctx.channel.send(f'U CANT STOP IT HAHA ')
    
    
  

@client.command()
async def help(ctx):
    await ctx.send(f'ur getting no help lmao')


@client.event
async def on_command_error(ctx, error):
    if error == CommandNotFound:
        await ctx.send(f'Thats not a command fool lol')
    else:
        print(error)
 
    
client.run("Nzg2Mzc4MjYyNzQxMTIzMTUy.X9Fh1A.Z8N_ey4CpOCZErxf8p--OD_Rtg8")
