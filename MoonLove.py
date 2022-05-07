from .. import loader, utils
from telethon.tl.types import Message

FRAMES = [
    "🌘🌗🌖🌕🌔🌓🌒\n🌙❤️❤️🌙❤️❤️🌙\n❤️💓💓❤️💓💓❤️\n❤️💓💓💓💓💓❤️\n🌙❤️💓💓💓❤️🌙\n🌙🌙❤️💓❤️🌙🌙\n🌙🌙🌙❤️🌙🌙🌙\n🌘🌗🌖🌕🌔🌓🌒",
    "🌗🌖🌕🌔🌓🌒🌘\n🌙❤️❤️🌙❤️❤️🌙\n❤️💓💓❤️💓💓❤️\n❤️💓💓💗💓💓❤️\n🌙❤️💓💓💓❤️🌙\n🌙🌙❤️💓❤️🌙🌙\n🌙🌙🌙❤️🌙🌙🌙\n🌗🌖🌕🌔🌓🌒🌘",
    "🌖🌕🌔🌓🌒🌘🌗\n🌙❤️❤️🌙❤️❤️🌙\n❤️💓💗❤️💗💓❤️\n❤️💓💗💗💗💓❤️\n🌙❤️💓💗💓❤️🌙\n🌙🌙❤️💓❤️🌙🌙\n🌙🌙🌙❤️🌙🌙🌙\n🌖🌕🌔🌓🌒🌘🌗",
    "🌕🌔🌓🌒🌘🌗🌖\n🌙❤️❤️🌙❤️❤️🌙\n❤️💗💗❤️💗💗❤️\n❤️💗💗💗💗💗❤️\n🌙❤️💗💗💗❤️🌙\n🌙🌙❤️💗❤️🌙🌙\n🌙🌙🌙❤️🌙🌙🌙\n🌕🌔🌓🌒🌘🌗🌖",
    "🌔🌓🌒🌘🌗🌖🌕\n🌙❤️❤️🌙❤️❤️🌙\n❤️💗💗❤️💗💗❤️\n❤️💗💗💖💗💗❤️\n🌙❤️💗💗💗❤️🌙\n🌙🌙❤️💗❤️🌙🌙\n🌙🌙🌙❤️🌙🌙🌙\n🌔🌓🌒🌘🌗🌖🌕",
    "🌓🌒🌘🌗🌖🌕🌔\n🌙❤️❤️🌙❤️❤️🌙\n❤️💗💖❤️💖💗❤️\n❤️💗💖💖💖💗❤️\n🌙❤️💗💖💗❤️🌙\n🌙🌙❤️💗❤️🌙🌙\n🌙🌙🌙❤️🌙🌙🌙\n🌓🌒🌘🌗🌖🌕🌔",
    "🌒🌘🌗🌖🌕🌔🌓\n🌙❤️❤️🌙❤️❤️🌙\n❤️💖💖❤️💖💖❤️\n❤️💖💖💖💖💖❤️\n🌙❤️💖💖💖❤️🌙\n🌙🌙❤️💖❤️🌙🌙\n🌙🌙🌙❤️🌙🌙🌙\n🌒🌘🌗🌖🌕🌔🌓",
    "🌘🌗🌖🌕🌔🌓🌒\n🌙❤️❤️🌙❤️❤️🌙\n❤️💖💖❤️💖💖❤️\n❤️💖💖💓💖💖❤️\n🌙❤️💖💖💖❤️🌙\n🌙🌙❤️💖❤️🌙🌙\n🌙🌙🌙❤️🌙🌙🌙\n🌘🌗🌖🌕🌔🌓🌒",
    "🌗🌖🌕🌔🌓🌒🌘\n🌙❤️❤️🌙❤️❤️🌙\n❤️💖💓❤️💓💖❤️\n❤️💖💓💓💓💖❤️\n🌙❤️💖💓💖❤️🌙\n🌙🌙❤️💖❤️🌙🌙\n🌙🌙🌙❤️🌙🌙🌙\n🌗🌖🌕🌔🌓🌒🌘",
] * 3 + [  # It's shit, I know. But it's the easiest solution tho
    "💓",
    "💗",
    "💖",
]


@loader.tds
class MoonLoveMod(loader.Module):
    """Interesting animation with hearts and moons"""

    strings = {"name": "MoonLove"}

    async def moonlovecmd(self, message: Message):
        """[text] - Love you to the moon"""
        m = await self.animate(
            message,
            FRAMES,
            interval=0.3,
            inline=False,
        )
        await m.edit(utils.get_args_raw(message) or "❤️")

    async def moonloveicmd(self, message: Message):
        """[text] - Love you to the moon [Inline]"""
        m = await self.animate(
            message,
            FRAMES,
            interval=0.3,
            inline=True,
        )
        await m.edit(utils.get_args_raw(message) or "❤️")
