from ciraag.core.module_injector import *
try:
    from google import generativeai
except ImportError:
    pass

try:
    gemini_api = environ["gemini_api"]
except KeyError:
    gemini_api = ""

class Gemini:
    async def google_gemini(self, event):
        self.chat = event.to_id
        if gemini_api == "":
            await ciraag.send_message(self.chat, "Before you can utilize the capabilities of Gemini AI, it is imperative to first set up the Gemini API. This preliminary step is an essential prerequisite for accessing and interacting with the AI model.")
        else:
            self.get_query = event.message.raw_text.split()
            self.get_query.pop(0)
            self.get_user_query = " ".join(self.get_query)
            try:
                generativeai.configure(api_key=gemini_api)
                if len(self.get_user_query) == 0:
                    await ciraag.send_message(self.chat, "I haven't received any query from you. Please provide your question so I can assist you. What would you like to learn using Gemini?")
                else:
                    self.model = generativeai.GenerativeModel("gemini-1.5-flash")
                    self.get_response = self.model.generate_content(f"{self.get_user_query}")
                    self.response = self.get_response.text
                    await ciraag.send_message(self.chat, f"{self.response}", parse_mode="markdown")
            except NameError:
                await ciraag.send_message(self.chat, "Gemini is a language model that requires a specific runtime environment. To leverage its features, you would need to set up a suitable environment by installing Gemini and configuring its API.")