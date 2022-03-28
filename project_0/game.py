"""Игра угадай число"""

import numpy as np

number = np.random.randint(1, 101) #Загадываем число

#Количество попыток
count = 0


while True:
    count += 1
    predict_numer = int(input("Угадай число от 1 до 100\n"))

    if predict_numer > number:
        print("Число должно быть меньше\n")

    elif predict_numer < number:
        print("Число должно быть больше\n")
    
    else:
        print("Вы угадали число! Это было число = {} и отгадали вы его с {} попытки".format(number, count))
        break #Конец игры