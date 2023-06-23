from webex_bot.webex_bot import WebexBot
from gpt import gpt

bot = WebexBot("API KEY")

bot.commands.clear()

bot.add_command(gpt())

bot.help_command = gpt()

bot.run()








