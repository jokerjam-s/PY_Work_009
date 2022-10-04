# Урок 9. Возможна ли жизнь без PIP?

Задача 1 обязательна для тех, кто реализовывал игру без библиотек (в консоли).
Далее берем либо задачу 2, либо 3,4,5.

1. Создайте программу для игры в ""Крестики-нолики"" при помощи виртуального окружения и PIP
2. Прикрутить бота к задачам с предыдущего семинара:

1. Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в неё систему логирования
1. Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.
1. Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и возвращает словарь, в котором каждый элемент списка является и ключом и значением. Предполагается, что элементы списка будут соответствовать правилам задания ключей в словарях.
1. Иван решил создать самый большой словарь в мире. Для этого он придумал функцию biggest_dict(**kwargs), которая принимает неограниченное количество параметров «ключ: значение» и обновляет созданный им словарь my_dict, состоящий всего из одного элемента «first_one» со значением «we can do it». Воссоздайте эту функцию.
1. Дана строка в виде случайной последовательности чисел от 0 до 9.
Требуется создать словарь, который в качестве ключей будет принимать данные числа (т. е. ключи будут типом int), а в качестве значений – количество этих чисел в имеющейся последовательности. Для построения словаря создайте функцию count_it(sequence), принимающую строку из цифр. Функция должна возвратить словарь из 3-х самых часто встречаемых чисел.

# Крестики-нолики

<span style="color:red">**Важно!**</span> Версия python понижена до 3.9 т.к. на 3.10 <code>pip install pyqt5-tools</code> возвращает ошибку

Скриншоты

!["Скриншот 1"](/ScreenShot/CZ_001.png 'Screen 1')
!["Скриншот 2"](/ScreenShot/CZ_002.png 'Screen 2')
!["Скриншот 3"](/ScreenShot/CZ_003.png 'Screen 3')
!["Скриншот 4"](/ScreenShot/CZ_004.png 'Screen 4')
!["Скриншот 5"](/ScreenShot/CZ_005.png 'Screen 5')

# Телеграм бот по составлению словаря (Задача 5)

Скриншот

!["Скриншот 6"](/ScreenShot/BOT_001.png 'Screen 6')

---