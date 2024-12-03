from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

from bot.translation import translate_text
from bot.pinyin import get_pinyin


#Functions to handle the logic for different commands or messages received by the bot.


async def start(update: Update, context):
    await update.message.reply_text("Welcome! Send me some text to translate to Mandarin.")

async def handle_message(update: Update, context):
    text = update.message.text
    translated_text = await translate_text(text)
    pinyin = await get_pinyin(translated_text)
    
    response = f"Translation: {translated_text}\nPinyin: {pinyin}"
    await update.message.reply_text(response)

def main():
    app = Application.builder().token(config.TELEGRAM_BOT_TOKEN).build()

    # Handlers for different bot commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()
