from ciraag.core.module_injector import *
from ciraag.utils import buttons
from telethon.errors.rpcerrorlist import ChatSendInlineForbiddenError

assistant_bot_username = environ["assistant_bot_username"]

class Repository:
    async def show_repository(self, event):
        try:
            self.chat = event.chat_id
            self.inline_repo = await ciraag.inline_query(f"{assistant_bot_username}", "repo")
            await self.inline_repo[0].click(self.chat)
        except ChatSendInlineForbiddenError:
            self.get_group_details = await ciraag.get_entity(int(self.chat))
            self.chat_name = self.get_group_details.title
            await ciraag.send_message(self.chat, f"Inline message sending is currently disabled on {self.chat_name}")
        except:
            pass
    
    async def repo_query(self, query):
        try:
            if query.text == "repo":
                self.repo = buttons.repo
                self.build_repo_article = query.builder.article(
                        title = "Ciraag",
                        text = f"🧞‍♂️ Ciraag\nA powerful multi-featured userbot on Telegram.",
                        buttons = self.repo
                    )
                await query.answer([self.build_repo_article])
        except:
            pass