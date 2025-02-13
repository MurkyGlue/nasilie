from tkinter import *
import random
import time

tk = Tk()
tk['bg'] = '#1f1f1f'
tk.geometry('500x700')
tk.resizable(height = False, width = False)
tk.title('wordle')
cv = Canvas(tk, width = 500, height = 700, bg = '#1f1f1f')
draws = []
st = []

def restart():
    global c, words, word, st, draw, cv, draws
    for i in draws:
        for j in i:
            j.destroy()
    for i in st:
        i.destroy()
    c = -100
    words = ['sword', 'thing', 'raise', 'weird', 'among', 'array', 'blind', 'chess', 'delay', 'devil', 'eagle', 'error']
    word = random.choice(words)
    st = [Entry(cv, bg = 'grey', font = 50, justify = 'center'), Entry(cv, bg = 'grey', font = 50, justify = 'center'), Entry(cv, bg = 'grey', font = 50, justify = 'center'), Entry(cv, bg = 'grey', font = 50, justify = 'center'), Entry(cv, bg = 'grey', font = 50, justify = 'center')]
    draws = []
    draw = []
    checking()
    
    

def checking():
    global word, st, c, draw, draws
    l = 0
    for i in range(5):
        if st[i].get() == '':
            draw.append(Label(cv, bg = 'grey', text = st[i].get(), font = 50))
        elif st[i].get() == word[i]:
            draw.append(Label(cv, bg = 'green', text = st[i].get(), font = 50))
            l += 1
        elif word.find(st[i].get()) != -1:
            draw.append(Label(cv, bg = 'yellow', text = st[i].get(), font = 50))
        else:
            draw.append(Label(cv, bg = 'grey', text = st[i].get(), font = 50))
    for i in range(5):
        draw[i].place(x = i*100, y = c, height = 100, width = 100)
    draws.append(draw)
    if l == 5:
        words.remove(word)
        restart()
        
    else:
        c += 100
        st = [Entry(cv, bg = 'grey', font = 50, justify = 'center'), Entry(cv, bg = 'grey', font = 50, justify = 'center'), Entry(cv, bg = 'grey', font = 50, justify = 'center'), Entry(cv, bg = 'grey', font = 50, justify = 'center'), Entry(cv, bg = 'grey', font = 50, justify = 'center')]
        for i in range(5):
            st[i].place(x = i*100, y = c, height = 100, width = 100)
        draw = []



restart()
check = Button(cv, bg = 'green', text = 'CHECK', font = 40, command = checking)
check.place(x = 0, y = 600, height = 100, width = 500)
cv.pack()
tk.mainloop()

