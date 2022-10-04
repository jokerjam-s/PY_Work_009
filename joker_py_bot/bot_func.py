from telegram.ext import ContextTypes
from telegram import Update

help_info = "/hello - приветствие\n" \
            "/help  - справка\n" \
            "/dict  - создать словарь"


async def hello_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def dict_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    data = update.message.text.split()
    if len(data) > 1:
        await update.message.reply_text(str(count_it(data[1])))
    else:
        await update.message.reply_text('неверный формат команды')


def count_it(sequence: str) -> {}:
    dict = {int(x): sequence.count(x) for x in sequence if x.isdigit()}
    values = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    result = {x[0]: x[1] for x in values[:3]}
    return result


async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(help_info)

