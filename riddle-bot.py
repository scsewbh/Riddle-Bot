import requests
import random
import asyncio
import discord
from discord.ext import commands

TOKEN = ''

bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"))
set = []
finishedset = []

class Main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def riddle(self, ctx):
        myid = '<@235185011941310468>'
        if ctx.author.id == 235185011941310468:
            await ctx.send("**MC Nerds Riddle**")
            await ctx.send("*Notice: You should not share or work together, the prize will not be split. Use the internet if you need to, actually it is required you do so. If you think "
                           "there is any error with the riddle or something went wrong feel free to contact me. I "
                           "may provide some help towards solving the riddle so you can ask. This riddle contains "
                           "5 steps, complete all and be first to win the prize. Good Luck! Await your first step!*")
            await asyncio.sleep(27.0)
            step1 = await ctx.send(">>> **Step 1: \n @here I forgot what country we are in, can you remind me? ** ")
            print(step1.id)

            @bot.event
            async def on_raw_reaction_add(payload):
                message_id = payload.message_id
                if message_id == step1.id:
                    if payload.emoji.name in "🇺🇸":
                        user = bot.get_user(payload.user_id)
                        print("Step 1 Completed:" + str(user))
                        await user.send(">>> **Step 2: Well Done Child. \n \n Try to solve this now:** \n 1 = Length "
                                        "of Mississipi River (in miles no commas) \n 2 = \"You would not believe your "
                                        "_____ if 10 million fireflies lit up the world as I said farewell\" (the "
                                        "blank) \n 3 = 20 times 3 plus 20 plus 10 minus 5 times 8 \n \n Type and Send "
                                        "!231 \n *(Do not share code)*")

    @commands.command()
    async def eyes502318(self, ctx):
        user = bot.get_user(ctx.author.id)
        print("Step 2 Completed:" + str(user))
        set.append(user)
        await ctx.send(">>> **Step 3: Let's play hide and seek. You will have to hide, I will try my best to find you!**")
        print(set)

        @bot.event
        async def on_member_update(before, after):
            status_user_id = after.id
            status_user = bot.get_user(status_user_id)
            if str(after.status) == "offline" and status_user in set and status_user not in finishedset:
                finishedset.append(user)
                print("Step 3 Completed:" + str(status_user))
                await status_user.send("Wow. Very Smart. Well done on to **Step 4**.")
                await status_user.send(">>> **Step 4: 2ManyCooks is your hint! Find my 4 digit password.** \n Send it "
                                       "in this format !mcxxxx \n (Example: !mc1234)")

    @commands.command()
    async def mc5742(self, ctx):
        user = bot.get_user(ctx.author.id)
        print("Step 4 Completed:" + str(user))
        await ctx.send(">>> **Step 5: Sickkkk! You made it to the last step. Good luck! Find the password "
                       "then send it to win. You will need the world wide web, you are only taking one part of each. "
                       "It is a Uniform Resource Locator. **")
        await ctx.send("warm women worlds . room blue . goat yankee / apple pen igloo kin come close")

    @commands.command()
    async def loading(self, ctx):
        y = 1
        dot = ' . '
        msg = await ctx.send('Loading')
        while y <= 2:
            con = 'Loading'
            x = 1
            while x <= 10:
                await asyncio.sleep(0.5)
                await msg.edit(content=con)
                con += dot
                x += 1
            y += 1

    @commands.command()
    async def mcnerds2020(self, ctx):
        user = bot.get_user(ctx.author.id)
        print("Step 5 Completed:" + str(user))
        id = ctx.author.id
        await ctx.send("Congratulations you won it is time to let everyone know!")
        y = 1
        dot = ' . '
        msg = await ctx.send('Loading')

        con = 'Loading'
        x = 1
        while x <= 4:
            await asyncio.sleep(1.0)
            await msg.edit(content=con)
            con += dot
            x += 1
        await msg.edit(content="Done!")

        channel = bot.get_channel(774394978599829575)
        await channel.send("SOLVED!! THE RIDDLE HAS BEEN SOLVED BY <@{0}>".format(id))


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')



bot.add_cog(Main(bot))
bot.run(TOKEN)