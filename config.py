import os, time, re
id_pattern = re.compile(r'^.\d+$')



class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "")
    API_HASH  = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
   
    # database config
    DATABASE_NAME = os.environ.get("DATABASE_NAME","")     
    DATABASE_URL  = os.environ.get("DATABASE_URL","")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "")
    ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]

    # channels logs
    FORCE_SUBS   = os.environ.get("FORCE_SUBS", "") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))

    # web response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", "True"))



class Txt(object):
    # part of text configuration
    START_TXT = """Hello {} 👋 

➻ This Is An Advanced And Yet Powerful Rename Bot.

➻ Using This Bot You Can Rename And Change Thumbnail Of Your Files.

➻ You Can Also Convert Video To File And File To Video.

➻ This Bot Also Supports Custom Thumbnail And Custom Caption.

<b>Bot Is Made By :</b> @OnAnimeSeries"""

    ABOUT_TXT = """
╭───────────────⍟
├<b>🤖 My Name</b> : {}
├<b>🖥️ Developer</b> : <a href=https://t.me/OnAnimeSeries>OnAnimeSeries</a> 
├<b>👨‍💻 Programer</b> : <a href=https://t.me/VoidZero_Dev>VoidZero</a>
├<b>📕 Library</b> : <a href=https://github.com/pyrogram>Pyrogram</a>
├<b>✏️ Language</b> : <a href=https://www.python.org>Python 3</a>
├<b>💾 Database</b> : <a href=https://cloud.mongodb.com>Mongo DB</a>
├<b>📊 Build Version</b> : <a href=https://t.me/VoidZero_Dev>Rename v4.7.0</a></b>     
╰───────────────⍟
"""

    HELP_TXT = """
🌌 <b><u>How To Set Thumbnail</u></b>

➪ /start - Start the bot and send any photo to automatically set as your thumbnail.
➪ /view_thumb - View your current thumbnail.
➪ /del_thumb - Delete your current thumbnail.

📑 <b><u>How To Set Custom Caption</u></b>

➪ /set_caption - Set a custom caption.
➪ /see_caption - View your custom caption.
➪ /del_caption - Delete your custom caption.
➪ <b>Example:</b>
<code>/set_caption 📕 Name ➠ : {filename}
🔗 Size ➠ : {filesize} 
⏰ Duration ➠ : {duration}</code>

🎭 <b><u>How To Set Prefix and Suffix</u></b>

➪ /set_prefix - Set your custom prefix.
➪ /see_prefix - View your current prefix.
➪ /del_prefix - Delete your prefix.
➪ <b>Example:</b> <code>/set_prefix @OnAnimeSeries</code>

➪ /set_suffix - Set your custom suffix.
➪ /see_suffix - View your current suffix.
➪ /del_suffix - Delete your suffix.
➪ <b>Example:</b> <code>/set_suffix @OnAnimeSeries</code>

📝 <b><u>How To Rename A File</u></b>

➪ Send any file and type the new file name.
➪ Then select the format: [ Document | Video | Audio ].

🎛️ <b><u>Metadata Options</u></b>

➪ /metadata - Change or set metadata for your files.

🛰️ <b><u>Other Commands</u></b>

➪ /ping - Check bot ping and responsiveness.
➪ /donate - Support the developer to keep the bot alive ❤️

🔧 <b><u>Need Help?</u></b>

𝗔𝗻𝘆 𝗼𝘁𝗵𝗲𝗿 𝗾𝘂𝗲𝘀𝘁𝗶𝗼𝗻𝘀 𝗼𝗿 𝗵𝗲𝗹𝗽:
<a href="https://t.me/VoidZero_Dev">Contact Developer</a>
"""

    PROGRESS_BAR = """\n
 <b>🔗 Size :</b> {1} | {2}
️ <b>⏳️ Done :</b> {0}%
 <b>🚀 Speed :</b> {3}/s
️ <b>⏰️ ETA :</b> {4}
"""

    DONATE_TXT = """
<b>🥲 Thanks For Showing Interest In Donation! ❤️</b>

If You Like My Bots & Projects, You Can 🎁 Donate Me Any Amount From 10 Rs Upto Your Choice.

<b>🛍 Message:</b> `@VoidZero_Dev`
"""


    SEND_METADATA = """<b><u>🖼️  HOW TO SET CUSTOM METADATA</u></b>

For Example :-

<code>By :- @VoidZero_Dev</code>

💬 For Any Help Contact @VoidZero_Dev
"""







## Fixed by @VoidZero_Dev ##
# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @MadflixBotz
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
# Contact @MadflixSupport
## Fixed by @VoidZero_Dev ##