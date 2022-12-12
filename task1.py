# Создайте программу для игры с конфетами человек против человека.
#
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint

total_sweet = 200
take_sweet = 0
player_sweet = 0
bot_sweet = 0

def who_is_first():
    random_number = randint(1, 2)
    if random_number == 1:
        player_turn()
    else:
        bot_turn()

def player_turn():
    global total_sweet
    global take_sweet
    global player_sweet
    print(f'Ваш ход, сейчас на столе {total_sweet} конфет')
    take_sweet = int(input('Сколько конфет вы хотите взять?: '))
    while take_sweet > 28 or take_sweet <= 0 or take_sweet > total_sweet:
        take_sweet = int(input('Возьмите другое количество'))
    total_sweet -= take_sweet
    player_sweet += take_sweet
    if total_sweet > 0:
        bot_turn()
    else:
        print('Вы победили')
def bot_turn():
    global total_sweet
    global take_sweet
    global bot_sweet
    take_sweet = total_sweet % 29 if total_sweet % 29 != 0 else randint(1, 28)
    total_sweet -= take_sweet
    bot_sweet += take_sweet
    print(f'Бот взял {take_sweet} конфет! На столе осталось {total_sweet} конфет!')
    if total_sweet > 0:
        player_turn()
    else:
        print('Бот победил')
who_is_first()

