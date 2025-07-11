from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

import os
BOT_TOKEN = os.environ.get("BOT_TOKEN")  # حتى لا نضع التوكن داخل الكود

async def reply_hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلاً 👋")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT | filters.ALL, reply_hello))

print("🤖 Bot is running...")
app.run_polling()
