import emoji
# 1
# Написать класс цветы
# У класса цветов должны быть атрибуты
# Вид
# Цвет
# Количество
# 2
# Добавить дочерный класс цветочки использую класс цветы
# И добавить к имеющиеся классам атрибут (цена)
# Цену задаёшь сама
# Добавить метод на свое усмотрение которое должно выводить цену и другие атрибуты
# Написать 1 метод должна выводиться надпись вид- роза, количество 101, красного цвета

import emoji

import emoji

while True:
    class Flower:
        def __init__(self, type, color, quantity):  # ✅ "__init__" must have *two* underscores
            self.type = type
            self.color = color
            self.quantity = quantity

        def info(self):
            return f'{self.type} {self.color} {self.quantity}'

    rose = Flower('floribunda_roses', 'red', '101')
    print(rose.type, rose.color, rose.quantity)

    user_text = input('Do you like this flower? ').strip().lower()

    if user_text == 'yes':
        print(emoji.emojize("A perfect choice :smiling_face_with_hearts:"))
    elif user_text == 'no':
        print(emoji.emojize("That's okay :smiling_face_with_smiling_eyes:"))
    elif user_text == 'stop':
        print(emoji.emojize("The program was stopped. :saluting_face:"))
        break  # ✅ Added break so the loop actually stops when user types "stop"
    else:
        print(emoji.emojize("You have to text only yes/no :expressionless_face:"))

