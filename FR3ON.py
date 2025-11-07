
import re
import base64
import asyncio
import logging
from telethon import events
from config import *
from asyncio import sleep
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(name)s:%(message)s')
logger = logging.getLogger("𝐒𝐎𝐔𝐑𝐂𝐄 𝙈𝙖𝙏𝙍𝙞𝙭")
logger.info("سورس ماتركـس  اشتغل يحبيبي ✓")

anti = False
async def ahmed_nshr(fraon, sleeptimet, chat, message, seconds):
    global anti
    anti = True
    while anti:
        if message.media:
            sent_message = await fraon.send_file(chat, message.media, caption=message.text)
        else:
            sent_message = await fraon.send_message(chat, message.text)
        await asyncio.sleep(sleeptimet)
        
        
        
        
@fraon.on(events.NewMessage(outgoing=True, pattern=r"^\.نشر (\d+) (@?\S+)$"))
async def ahmedf(event):
    await event.delete()
    parameters = re.split(r'\s+', event.text.strip(), maxsplit=2)
    if len(parameters) != 3:
        return await event.reply("اڪتب الامر صح يغبي 😂♥")
    seconds = int(parameters[1])
    chat_usernames = parameters[2].split()
    fraon = event.client
    global anti
    anti = True
    message = await event.get_reply_message()
    for chat_username in chat_usernames:
        try:
            chat = await fraon.get_entity(chat_username)
            await ahmed_nshr(fraon, seconds, chat.id, message, seconds)  # تمرير قيمة seconds هنا لكل مجموعة
        except Exception as e:
            await event.reply(f"⌔∮ ماكو كروب بالاسم هذا 😂 {chat_username}: {str(e)}"
            )
        await asyncio.sleep(1)

    
async def ahmed_allnshr(fraon, sleeptimet, message):
    global anti
    anti = True
    ahmed_chats = await fraon.get_dialogs()
    while anti:
        for chat in ahmed_chats:
            if chat.is_group:
                try:
                    if message.media:
                        await fraon.send_file(chat.id, message.media, caption=message.text)
                    else:
                        await fraon.send_message(chat.id, message.text)
                except Exception as e:
                    print(f"Error in sending message to chat {chat.id}: {e}")
        await asyncio.sleep(sleeptimet)
@fraon.on(events.NewMessage(outgoing=True, pattern=r"^\.نشر_بالكروبات (\d+)$"))
async def ahmedf(event):
    await event.delete()
    seconds = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
    message =  await event.get_reply_message()
    try:
        sleeptimet = int(seconds[0])
    except Exception:
        return await event.reply("اڪتب الامر صح يغبي 😂♥")
    fraon = event.client
    global anti
    anti = True
    await ahmed_allnshr(fraon, sleeptimet, message)

super_groups = ["super", "سوبر"]
async def ahmed_supernshr(fraon, sleeptimet, message):
    global anti
    anti = True
    ahmed_chats = await fraon.get_dialogs()
    while anti:
        for chat in ahmed_chats:
            chat_title_lower = chat.title.lower()
            if chat.is_group and any(keyword in chat_title_lower for keyword in super_groups):
                try:
                    if message.media:
                        await fraon.send_file(chat.id, message.media, caption=message.text)
                    else:
                        await fraon.send_message(chat.id, message.text)
                except Exception as e:
                    print(f"انت مش هناك يعبيط 😂♥ {chat.id}: {e}")
        await asyncio.sleep(sleeptimet)
@fraon.on(events.NewMessage(outgoing=True, pattern=r"^\.سوبر (\d+)$"))
async def ahmedf(event):
    await event.delete()
    seconds = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
    message =  await event.get_reply_message()
    try:
        sleeptimet = int(seconds[0])
    except Exception:
        return await event.reply("اڪتب الامر صح يغبي 😂♥")
    fraon = event.client
    global anti
    anti = True
    await ahmed_supernshr(fraon, sleeptimet, message)

@fraon.on(events.NewMessage(outgoing=True, pattern='.وقف النشر'))
async def stop_ahmed(event):
    global anti
    anti = False
    await event.edit("**᯽︙ وقفتلك النشر ياعمي ♥ ** ")
@fraon.on(events.NewMessage(outgoing=True, pattern=r"^\.(الاوامر|فحص)$"))
async def ahmedf(event):
    await event.delete()
    if event.pattern_match.group(1) == "الاوامر":
        FR3ON = """**
🔰 قـائمة اوامر النشر التلقائي للمجموعات

== 𝐒𝐎𝐔𝐑𝐂𝐄 𝙈𝙖𝙏𝙍𝙞𝙭  : @BPB0B ==

`.نشر` عدد الثواني معرف الكروب :
 - للنشر في المجموعة التي وضعت معرفها مع عدد الثواني

`.نشر_بالكروبات` عدد الثواني : 
- للنشر في جميع المجموعات الموجوده في حسابك
 
`.سوبر` عدد الثواني : 
- للنشر بكافة المجموعات السوبر التي منظم اليها 

`.وقف النشر` :
- لأيقاف جميع انواع النشر اعلاه

• مُـلاحظة : جميع الأوامر اعلاه تستخدم بالرد على الرسالة او الكليشة المُراد نشرها

== 𝐒𝐎𝐔𝐑𝐂𝐄 𝙈𝙖𝙏𝙍𝙞𝙭  : @BPB0B ==
    **"""
        await event.reply(file='https://files.catbox.moe/g4ve8h.mp4', message=FR3ON)
    elif event.pattern_match.group(1) == "فحص":
        ahmedf_ali = "**[+] بوت النشر يعمل بنجاح✅\n[+] لو في مشكله كلمني\n t.me/div_bilal**"
        await event.reply(file='https://envs.sh/zjH.jpg', message=ahmedf_ali)




print('تم تشغيل بوت نشر سورس ماتركـس  ✅  ')
fraon.run_until_disconnected()
