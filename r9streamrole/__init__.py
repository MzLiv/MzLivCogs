from redbot.core.bot import Red

from .r9streamrole import StreamRole


def setup(bot: Red):
    bot.add_cog(StreamRole())
