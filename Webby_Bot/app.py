from webex_bot.webex_bot import WebexBot
from gpt import gpt

bot = WebexBot("MWFlOTA1NWMtZWZiMS00Y2E4LWE3NjMtMmM5NTZjNjE1MTE5M2IzMzgzMzAtYTRl_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f")

bot.commands.clear()

bot.add_command(gpt())

bot.help_command = gpt()

bot.run()








