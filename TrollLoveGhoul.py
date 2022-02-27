from .. import loader
from asyncio import sleep 

class TrollLoveMod(loader.Module):
	strings = {"name": "TrollLoveGhoul"}
	
	async def trolllovecmd(self, message):
		await message.edit("Я люблю тебя!")
		await sleep(2)
		await message.respond("А хотя...")
		await sleep(2)
		await message.respond("Нет, я же dead inside")
		await sleep(2)
		a = 1000
		while a > 7:
			await message.respond(str(a) + " - 7")
			a = a - 7
			
