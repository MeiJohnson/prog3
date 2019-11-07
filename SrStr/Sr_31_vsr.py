#Угадай число
import random

random.seed(version=2)

flag = False
guess_num = random.randint(0,1000)
while flag != True:
    s = "Ваше число {}".format(guess_num)
    print(s)
    ans1 = str(input("Ответ(Да/Нет): "))
    if ans1 == "Да":
        flag = True
    ans2 = str(input("Загаданное число больше чем это?(Да/Нет) "))
    if ans2 == "Да":
        guess_num += 1
    else:
        guess_num -= 1