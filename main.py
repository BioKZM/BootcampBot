import disnake
import json
from disnake.ext import commands,tasks
from disnake.utils import get
# TOKEN = os.environ['TOKEN']
TOKEN = "MTEyNzQxNDE5NTY4MDQ2NDkwNg.Gw33q4.gR5YCTOi653LlO83OmAHb6wmpHRBql7l0hw9Jc"
client = commands.Bot(command_prefix="!",intents=disnake.Intents.all(),help_command=None, case_insensitive=True, sync_commands=True)


@client.event
async def on_ready():
    print("Bot hazır")

@tasks.loop(seconds=1)
async def startLoop():

    stageChannel = client.get_channel(1111085609436581959)
    # print(stageChannel.members)
    with open("time.json","r",encoding="utf-8") as file:
        data = json.load(file)
    # data['']
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

