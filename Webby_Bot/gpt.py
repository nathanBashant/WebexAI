from webex_bot.models.command import Command
from webex_bot.models.response import Response
import openai

class gpt(Command):
    messages = []
    messages.append({"role": "system", "content": "You are a polite assistant answering questions regarding all Cisco technologies including but not limited to: Webex by Cisco, Cisco ACI and ACI Architecture, Cisco Data Center Technologies, and Ansible Network Automation Tasks"})
    
    def __init__(self):
        super().__init__()

    def execute(self, message, attatchment_actions, activity):
        openai.api_key = ("key")
        
        self.messages.append({"role": "user", "content": message})
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=self.messages)
        
        gpt_response=completion.choices[0].message.content
        self.messages.append({"role": "assistant", "content": message})
        return(gpt_response)
        
