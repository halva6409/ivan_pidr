import pytz, os, secret, asyncio
from aiogram import Bot, Dispatcher, types 
from aiogram.filters import Command
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import time
import pytz, os, secret


BOT_TOKEN = secret.TOKEN
TIMEZONE = pytz.timezone("Europe/Samara")
ADMIN_ID= 5139103016
USER_FILE = "users.json"
MESSAGE_FILE = "message.txt"




bot = Bot(BOT_TOKEN)
dp = Dispatcher()
scheduler = AsyncIOScheduler(timezone=TIMEZONE)


def load_users():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_users(users):
    with open(USER_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=2)

def get_messge_text():
    if os.path.exists(MESSAGE_FILE):
        with open(MESSAGE_FILE, "r", encoding="utf-8") as f:
            return f.read().strip()
        return

async def main():
    for job in scheduler.get_jobs():
        scheduler.remove_job(job.id)

    scheduler.add_job(
    send_broadcast,
    trigger="cron",
    hour=8,
    minute=0,
    id="daily_broadcast",
    replace_existing=True,
    misfire_grace_time=3600
    )

    scheduler.start()

    print("Бот запущен.Ежедневная рассылка в 8:00")

if __name__ == "__main__":
    asyncio.run(main())
        