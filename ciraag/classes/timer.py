from ciraag.core.module_injector import *
from telethon.tl.functions.users import GetFullUserRequest
from dotenv import load_dotenv
from os import remove

load_dotenv()
ciraag_protection = "@ciraag_protection"
ciraag_users = 7

class SelfDestruct:
    async def save(self, event):
        self.chat = event.to_id
        self.developer =  "<a href='https://t.me/about_iniridwanul'>iniridwanul</a>"
        if event.is_private:
            if event.reply_to:
                self.self_destruct = await event.get_reply_message()
                if self.self_destruct.media:
                    self.get_protected_users = await ciraag.get_messages(ciraag_protection, ids=ciraag_users)
                    self.protected_users = self.get_protected_users.message.split()
                    self.sender_id = self.self_destruct.sender_id
                    if str(self.sender_id) in self.protected_users:
                        await ciraag.send_message(self.chat, f"Unfortunately, self-destructing media downloads are not supported for this user due to the {self.developer}'s commitment to user privacy.", parse_mode="html", link_preview=False)
                    else:
                        self.download_self_destruct_media = await self.self_destruct.download_media()
                        self.get_sender_details = await ciraag(GetFullUserRequest(self.sender_id))
                        self.first_name = self.get_sender_details.users[0].first_name
                        self.gallery = int(environ["ciraag_gallery"])
                        await ciraag.send_file(self.gallery, self.download_self_destruct_media, caption=f"Sender: {self.first_name}\nType: Self-destruct\nDeveloper: {self.developer}", parse_mode="html")
                        remove(self.download_self_destruct_media)
                else:
                    await ciraag.send_message(self.chat, "This function is specifically designed for downloading media files. Since the content you're attempting to download does not fall under the media category, please restrict the use of this feature to media files only.")
            else:
                await ciraag.send_message(self.chat, "Please use the command in the media's reply.")
        else:
            await ciraag.send_message(self.chat, "This feature only works for private messages.")