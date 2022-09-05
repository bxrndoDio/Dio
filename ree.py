import discord
from discord.ext import commands
import random

token = "MTAxNjM2MTA3NzkyNTIxNjI4Nw.G8Q8Yi.oO_KqOOw8TVzPzRgfc0FD0yXR3_XhV6sm2GHcc"

intents = discord.Intents.default()
intents.members = True

client =  commands.Bot(command_prefix = '.',intents=intents) 

@client.event 
async def on_member_join(ctx, member):
     channel=client.get_channel(1015976231235227738) 
     emj=discord.Embed(title="ยินดีต้อนรับ",description=f"ยินดีตัอนรับคุณ  {member.name} นะคะ") #แก้ได้เลย
     await ctx.channel.send(embed=emj)

@client.event
async def on_member_remove(ctx, member):
channel=client.get_channel(1015976235001716746)
     emb=discord.Embed(title="Bye",description=f"ลาก่อนนะคะคุณ  {member.name} ") #แก้ได้เลย
     await ctx.channel.send(embed=emb)


client.run(token)