from dotenv import load_dotenv
import discord
import os
from app.gpt_ai.openai import chatgpt_response

load_dotenv()

discord_token = os.env('DISCORD_TOKEN')

command_list =  ['/ai', '/bot', '/chatgpt', '/gpt']

class MyClient(discord.client):
    async def on_ready(self):
        print("Successfully logged in as: ", self.user)

    async def on_message(self, message):
        print(message.content)
        if(message.author == self.user):
            return
        command, user_message = None, None

        for text in command_list:
            if message.content.startswith(text):
                command = message.content.split(' ')[0]
                user_message = message.content.replace(text, '')
                print(command, user_message)

        if command in command_list:
            bot_response = chatgpt_response(prompt= user_message)
            await message.channel.send(f"Answer: {bot_response}")

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

        
