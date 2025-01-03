from ciraag.core.module_injector import *
from google import generativeai

gemini_api = environ["gemini_api"]

class Gemini:
    async def google_gemini(self, event):
        self.chat = event.to_id
        self.get_query = event.message.raw_text.split()
        self.get_query.pop(0)
        self.get_user_query = " ".join(self.get_query)
        if len(self.get_user_query) == 0:
            await ciraag.send_message(self.chat, "I haven't received any query from you. Please provide your question so I can assist you. What would you like to learn using Gemini?")
        else:
            generativeai.configure(api_key=gemini_api)
            self.model = generativeai.GenerativeModel("gemini-1.5-flash")
            self.get_response = self.model.generate_content(f"{self.get_user_query}")
            self.response = self.get_response.text
            await ciraag.send_message(self.chat, f"{self.response}", parse_mode="markdown")