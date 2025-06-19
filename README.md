
<img src="https://graph.org/file/d3dde3480b703b3f34e77.jpg" alt="logo" target="_blank">

<h1 align="center">
 <b><a href="https://t.me/OnAnimeSeriesbot" target="_blank"> Rename Bot 2GB </a></b>
</h1>

<p align="center">🩵 Thanks for Being Here 🩵</p>

---

### ⚙️ CONFIG VARIABLES

* `BOT_TOKEN` - Get it from [@BotFather](https://t.me/BotFather)
* `API_ID` - Get it from [Telegram API](https://my.telegram.org)
* `API_HASH` - Get it from [Telegram API](https://my.telegram.org)
* `ADMIN` - Your Telegram user ID
* `LOG_CHANNEL` - Bot Log Channel (Must start with `-100`)
* `DATABASE_URL` - Get from [MongoDB Atlas](https://cloud.mongodb.com)
* `DATABASE_NAME` - Mongo database name (Optional)
* `FORCE_SUBS` - Force subscribe channel (without `@`) (Optional)
* `START_PIC` - Start message image URL (Optional)

---

### 🚀 DEPLOYMENT SUPPORT

<summary>Deploy to Koyeb</summary>
<p><br>                 
<a target="_blank" href="https://app.koyeb.com/deploy?name=rename-bot-2gb&repository=ibrahimkhan008%2FRename-Bot-2GB&branch=main&builder=dockerfile&instance_type=free&instances_min=0&autoscaling_sleep_idle_delay=300&ports=8080%3Bhttp%3B%2F&hc_protocol%5B8080%5D=tcp&hc_grace_period%5B8080%5D=5&hc_interval%5B8080%5D=30&hc_restart_limit%5B8080%5D=3&hc_timeout%5B8080%5D=5&hc_path%5B8080%5D=%2F&hc_method%5B8080%5D=get">
  <img src="https://www.koyeb.com/static/images/deploy/button.svg" alt="Deploy">
</a>
</p>

---

### 📦 FEATURES

- Rename any file quickly
- Permanent thumbnail support
- Force join to channel support
- Broadcast to users (admin only)
- Custom caption, prefix, suffix
- Koyeb/Heroku/Railway deployable
- Docker-based deployment
- Developer support available 🔥

---

### 📜 COMMANDS

```
/start - Start the bot
/viewthumb - View current thumbnail
/delthumb - Delete current thumbnail
/set_caption - Set a custom caption
/see_caption - View your caption
/del_caption - Delete your caption
/metadata - Change your file metadata
/ping - Check bot ping
/donate - Support the developer
/set_prefix - Set your filename prefix
/see_prefix - View your prefix
/del_prefix - Delete your prefix
/set_suffix - Set your filename suffix
/see_suffix - View your suffix
/del_suffix - Delete your suffix
/restart - Restart bot (Admins only)
/broadcast - Broadcast message (Admins only)
/status - Check bot status (Admins only)
```

---

### ✅ KOYEB DEPLOYMENT GUIDE

```
🔧 Requirements:
- GitHub account
- Koyeb account
- Telegram Bot Token
- MongoDB URI (Atlas or other)
```

1. Fork this repo.
2. Go to [Koyeb](https://app.koyeb.com) and click **Create App**.
3. Select GitHub → choose this repo and branch.
4. Under **Builder**, select `Dockerfile`.
   - Dockerfile location: `./Dockerfile`
   - Work directory: `.`

5. Add these environment variables:

| Key              | Value                          |
|------------------|--------------------------------|
| `BOT_TOKEN`      | Your Telegram bot token        |
| `API_ID`         | Telegram API ID                |
| `API_HASH`       | Telegram API HASH              |
| `ADMIN`          | Your Telegram user ID          |
| `DATABASE_URL`   | Your MongoDB URI               |
| `DATABASE_NAME`  | (Optional) Database name       |
| `LOG_CHANNEL`    | Channel ID starting with -100  |
| `FORCE_SUBS`     | (Optional) Channel username    |
| `START_PIC`      | (Optional) Start photo URL     |

✅ **Important:** Make sure Koyeb port is set to `8080`.

6. Click **Deploy** and wait for the build to finish.

7. Later changes to tokens/configs? Go to **Settings → Environment Variables → Redeploy without Rebuild**.

---

### 🛠 FIXED & ENHANCED BY @VoidZero_Dev

- FFmpeg not found → Docker image fixed ✅  
- Metadata command improved
- Full support for prefix/suffix customization
- Clean log tracing
- Secure ENV-based config

---

### 🤝 CREDITS

- [VoidZero_Dev](https://t.me/VoidZero_Dev)
- [JishuDeveloper](https://github.com/JishuDeveloper)
- [Madflix Official](https://github.com/jishusinha)
- [lntechnical2](https://github.com/lntechnical2)

---

### 📢 BOT CHANNEL
- [OnAnimeSeries](https://t.me/OnAnimeSeries)

---

### ☕ SUPPORT ME
- [PhonePe](https://envs.sh/3v.jpg)
- [UPI](https://envs.sh/3v.jpg)
