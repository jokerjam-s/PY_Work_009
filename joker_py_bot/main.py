# Дана строка в виде случайной последовательности чисел от 0 до 9.
# Требуется создать словарь, который в качестве ключей будет принимать данные числа
# (т. е. ключи будут типом int), а в качестве значений – количество этих чисел в имеющейся последовательности.
# Для построения словаря создайте функцию count_it(sequence), принимающую строку из цифр.
# Функция должна возвратить словарь из 3-х самых часто встречаемых чисел.

from telegram.ext import ApplicationBuilder, CommandHandler
from bot_func import *


def main():
    app = ApplicationBuilder().token("5782264928:AAG7kgM_Dg8R1cPRwE5XZ7xYrJB9dU8-hkc").build()

    app.add_handler(CommandHandler("hello", hello_cmd))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("dict", dict_cmd))
    print('server started')
    app.run_polling()


if __name__ == '__main__':
    main()
