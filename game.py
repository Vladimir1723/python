
# пространства имен
import tkinter, os, random, sys

from tkinter import messagebox

# from tkinter import * - так делать не стоит, потому что импортируются
# все функции,которые там есть, без какого-либо пространства имен; они могут
# перезаписать существующие функции, и получится каша

IMG_PATH = 'nums'
SIZE = 4

#from tkinter import Tk, PhotoImage - а вот так можно
main_window = tkinter.Tk();
main_window.title('Игра 15')

file_list = sorted(os.listdir(IMG_PATH))

files_path_list = []

for file in file_list:
#    file_path = IMG_PATH + '\\' + file	- работает только в винде
#    file_path = IMG_PATH + '/' + file - противоречит python-идеологии

    # метод join соединяет кусочки пути (python-style):
    file_path = os.path.join(IMG_PATH, file)
    files_path_list.append(file_path)

    
# nums\01.gif
# print(files_path_list)


images_list = []
for file_path in files_path_list:
    # класс PhotoImage хорош с gif, с jpeg придется обернуть в pillow
    # здесь file - именованный аргумент
    image = tkinter.PhotoImage(file = file_path)
    images_list.append(image)

# print(images_list)

labels_list = []


for x, image in enumerate(images_list):
    row = x // SIZE
    column = x % SIZE
    label = tkinter.Label(main_window, image = image)
    # grid размещает объекты по сетке. Здесь уже становится что-то видно
    label.grid(row = row, column = column)
    label.x = x
    label.row = row
    label.column = column
    labels_list.append(label)

static_list = labels_list


# в качестве текущего выбран белый квадрат
curr = labels_list[-1] # - индексы можно зацикливать (-1 = size + 1)


def upperItem(arg):
    x = (arg.row - 1) * SIZE + arg.column
    return labels_list[x]


def lowerItem(arg):
    x = (arg.row + 1) * SIZE + arg.column
    return labels_list[x]

    
def leftItem(arg):
    x = arg.row * SIZE + arg.column - 1
    return labels_list[x]


def rightItem(arg):
    x = arg.row * SIZE + arg.column + 1
    return labels_list[x];


def exchangeItems(arg):
    x_near = arg.row * SIZE + arg.column # - где сосед
    x_curr = curr.row * SIZE + curr.column # - где текущий
    arg.row, curr.row = curr.row, arg.row
    arg.column, curr.column = curr.column, arg.column
    labels_list[x_near], labels_list[x_curr] = labels_list[x_curr], labels_list[x_near]	# - поменяли местами

    
def renderItem(arg):
    arg.grid(row = arg.row, column = arg.column)


step = 0
shuffle = False


def stepsMove():
    if (not shuffle):
        steps = tkinter.Label(main_window, text='Шагов сделано: ' + str(0))
        steps.grid(row=5, column=0)
    elif (shuffle):
        global step
        step += 1
        steps = tkinter.Label(main_window, text='Шагов сделано: ' + str(step))
        steps.grid(row=5, column=0)

    
def keyPress(arg):
    near = None
    global step
    if arg == 'u' and curr.row > 0:
        near = upperItem(curr)
        stepsMove()
    elif arg == 'd' and curr.row < SIZE - 1:
        near = lowerItem(curr)
        stepsMove()
    elif arg == 'l' and curr.column > 0:
        near = leftItem(curr)
        stepsMove()
    elif arg == 'r' and curr.column < SIZE - 1:
        near = rightItem(curr)
        stepsMove()
    elif arg == 'q':
        sys.exit()

    if near:
        exchangeItems(near) # - меняет местами curr с near
        renderItem(near)
        renderItem(curr)


def shuffleGame():
    actions = ['r', 'd', 'u', 'l']
    # позволяет случайным образом взять из списка несколько эл-тов:
    for i in range(4):
        do_now = random.sample(actions, 1)[0] # возвращает список, а нужен эл-т
        keyPress(do_now)

    global shuffle
    shuffle = True
        

# здесь мы заставим программу реагировать на события
main_window.bind('<Up>', lambda x: keyPress('u'))
main_window.bind('<Down>', lambda x: keyPress('d'))
main_window.bind('<Left>', lambda x: keyPress('l'))
main_window.bind('<Right>', lambda x: keyPress('r'))


# можно также реализовать выход клавишей  q
main_window.bind('q', lambda x: keyPress('q'))
main_window.bind('Q', lambda x: keyPress('Q'))


label = tkinter.Label(main_window, text = 'Игра началась')
label.grid(row = 4, column = 0)


main_window.after(2000, shuffleGame)


main_window.mainloop();
# в mainloop(..) можно передать количество циклов
