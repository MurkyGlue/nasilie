import random
import os
sym = 'qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*<>?-_=+'
pas = ''
try:
    name = input()
    lenght = int(input())
    for i in range(lenght):
        pas += sym[random.randint(0, len(sym)-1)]
    if os.path.isfile(f'{name}.txt'):
        os.remove(f'{name}.txt')
    file = open(f'{name}.txt', 'w+')
    file.write(pas)
    file.close()
except ValueError:
    print('ошибка ввода')
