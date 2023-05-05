import discord
from discord.ext import commands


class Test:
	"""Test cog to push commits for testing the downloader."""
	def __init__(self,bot):
		self.bot = bot

	@commands.command(pass_context=True)
	async def test(self, ctx):
		"""I really hope you didn't install this."""
		await self.bot.say("\N{NEWSPAPER}")

def setup(bot):
	n = Test(bot)
	bot.add_cog(n)
