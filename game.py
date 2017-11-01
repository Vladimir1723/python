import tkinter, os, random
from tkinter import messagebox

IMG_PATH = 'nums'
SIZE = 4

main_window = tkinter.Tk()
main_window.title('game 15')

file_list = sorted(os.listdir(IMG_PATH))

files_path_list = []
for file in file_list:
	file_path = os.path.join(IMG_PATH, file)
	files_path_list.append(file_path)

images_list = []
for file_path in files_path_list:
   	image = tkinter.PhotoImage(file=file_path)
   	images_list.append(image)

labels_list = []
for x, image in enumerate(images_list):
   	row = x // SIZE
   	column = x % SIZE
	label = tkinter.Label(main_window, image=image)
   	label.grid(row=row, column=column)
   	label.x = x
   	label.row = row
   	label.column = column
   	labels_list.append(label)

curr = labels_list[-1]


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
   	return labels_list[x]


def exchangeItems(arg):
   	x_near = arg.row * SIZE + arg.column
   	x_curr = curr.row * SIZE + curr.column
   	arg.row, curr.row = curr.row, arg.row
   	arg.column, curr.column= curr.column, arg.column
   	labels_list[x_near], labels_list[x_curr] = labels_list[x_curr], labels_list[x_near]


def renderItem(arg):
   	arg.grid(row=arg.row, column=arg.column)


def keyPress(arg):
   	near = None

   	if arg == 'u' and curr.row > 0:
       		near = upperItem(curr)
   	elif arg == 'd' and curr.row < SIZE - 1:
       		near = lowerItem(curr)
   	elif arg == 'l' and curr.column > 0:
       		near = leftItem(curr)
   	elif arg == 'r' and curr.column < SIZE - 1:
       		near = rightItem(curr)

   	if near:
       		exchangeItems(near)
       		renderItem(near)
       		renderItem(curr)


def shuffleGame():
   	actions = ['u', 'd', 'l', 'r']
   	for i in range(100):
       		do_now = random.sample(actions, 1)[0]
       		# print(do_now)
       		keyPress(do_now)


main_window.bind('<Up>', lambda x: keyPress('u'))
main_window.bind('<Down>', lambda x: keyPress('d'))
main_window.bind('<Left>', lambda x: keyPress('l'))
main_window.bind('<Right>', lambda x: keyPress('r'))

label = tkinter.Label(main_window, text='Game was started')
label.grid(row=4, column=0)


# shuffleGame()
main_window.after(2000, shuffleGame)

main_window.mainloop()

