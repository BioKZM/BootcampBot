import disnake
import json
from disnake.ext import commands,tasks
from disnake.utils import get

client = commands.Bot(command_prefix="!",intents=disnake.Intents.all(),help_command=None, case_insensitive=True, sync_commands=True)


@client.event
async def on_ready():
    print("Bot hazır")

@tasks.loop(seconds=1)
async def startLoop():

    stageChannel = client.get_channel(1111085609436581959)
    with open("time.json","r",encoding="utf-8") as file:
        data = json.load(file)
    for member in stageChannel.members:
        data[f"{member.name}"] += 1

    with open("time.json","w",encoding="utf-8") as file:
        json.dump(data,file,indent=4,ensure_ascii=False)

@client.command(name="create")
async def createJSONFile(ctx):
    if ctx.message.author.id == 373457193271558145:
        with open("time.json","w",encoding="utf-8") as file:
            data = {}
            for member in client.get_all_members():
                data[f"{member.name}"] = 0
            json.dump(data,file,indent=4,ensure_ascii=False)

@client.command(name="startLoop")
async def loopStartCommand(ctx):
    if ctx.message.author.id == 373457193271558145:
        startLoop.start()

@startLoop.before_loop
async def beforeLoop():
    await client.wait_until_ready()

client.run(TOKEN)

