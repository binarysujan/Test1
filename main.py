import os
import subprocess

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)
Token = "5843106760:AAEJzYti3uRQLXw1zBT5IS9IPXWuAEvIAf8"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi...Testing")


async def test(update: Update, context: ContextTypes.DEFAULT_TYPE):
    cmd = "git --version"
    return_output_value = subprocess.check_output(cmd)
    returned_value = return_output_value.decode("utf-8")
    await update.message.reply_text(returned_value)


def testing():
    cmd = "git --version"
    return_output_value = subprocess.check_output(cmd)
    print(return_output_value.decode("utf-8"))


def main():
    print("Running...")
    application = Application.builder().token(Token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("test", test))

    application.run_polling()


if __name__ == "__main__":
    main()
    # testing()
