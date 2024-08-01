from tkinter import *
import random
import time

sc = Tk()
s1 = 0 #первый слот
s2 = 0 #второй слот
s3 = 0 #третий слот
balance = 1000 #количество денег

sc['bg'] = '#1f1f1f'
sc.geometry('500x300')                          #объявление окна
sc.resizable(width = False, height = False)

cv = Canvas(sc, width = 500, height = 300, bg = '#1f1f1f')

cv.create_rectangle(280, 75, 435, 175, fill = 'red')
slot1 = Label(cv, text = s1, bg = 'yellow', font = 70) #слоты
slot2 = Label(cv, text = s2, bg = 'yellow', font = 70)
slot3 = Label(cv, text = s3, bg = 'yellow', font = 70)
showBalance = Label(cv, text = balance, bg = 'white', font = 60) #вывод баланса
price = Entry(cv, bg = 'grey') #ввод ставки

slot1.place(x = 300, y = 100)
slot2.place(x = 350, y = 100)
slot3.place(x = 400, y = 100)           #расположение
showBalance.place(x = 100, y = 100)
price.place(x = 100, y = 200)


def run():
    global balance, showBalance
    if int(price.get()) > balance:
        runButton.configure(bg = 'red')
    else:
        balance -= int(price.get()) #вычет ставки из баланса
        showBalance.configure(text = balance)
        s1 = random.randint(0,9)
        s2 = random.randint(0,9)
        s3 = random.randint(0,9)
        if s1 == s2 == s3:
            balance += int(price.get())*1000 #выигрыш
        slot1.configure(text = s1)
        slot2.configure(text = s2)
        slot3.configure(text = s3)

runButton = Button(cv, text = 'run', bg = 'green', font = 50, command = run) #кнопка

cv.pack()
runButton.place(x = 330, y = 200)

sc.mainloop()