from redbot.core import commands

class Helloworld(commands.Cog):
    """My custom cog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        """This does stuff!"""
        # Your code will go here
        await ctx.send("hello world")