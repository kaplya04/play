# библиотека позволяет генерировать случайные числа
import random
print ('Добро пожаловать в игру: Камень, ножницы, бумага.')
player = input('1. Камень?\n 2. Ножницы?\n 3. Бумага? \n 4. Ответ: ')
s = ['камень','ножницы', 'бумага'] # cписок
if player in s:
    # состоит в том, чтобы выбрать или сгенерировать случайный элемент
    ruslan = random.choice(s)
    print('Выбор Руслана: ', ruslan)
if ruslan == 'камень' and player == 'ножницы':
    print('Вы проиграли')
elif ruslan == 'камень' and player == 'бумага':
    print('Вы выиграли')
elif ruslan == 'камень' and player == 'камень':
    print('Ничья')
elif ruslan == 'ножницы' and player == 'бумага':
    print('Вы проиграли')
elif ruslan == 'ножницы' and player == 'камень':
    print('Вы выиграли')
elif ruslan == 'ножницы' and player == 'ножницы':
    print('Ничья')
elif ruslan == 'бумага' and player == 'камень':
    print('Вы проиграли')
elif ruslan == 'бумага' and player == 'ножницы':
    print('Вы выиграли')
elif ruslan == 'бумага' and player == 'бумага':
    print('Ничья')
