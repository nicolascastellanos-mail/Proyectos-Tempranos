from tkinter import *
from random import choice, randint

def for_fill():
	global fill_valid

	num_list = [
		number_01_01, number_01_02, number_01_03, number_01_04, number_01_05, number_01_06, number_01_07, number_01_08, number_01_09,
		number_02_01, number_02_02, number_02_03, number_02_04, number_02_05, number_02_06, number_02_07, number_02_08, number_02_09,
		number_03_01, number_03_02, number_03_03, number_03_04, number_03_05, number_03_06, number_03_07, number_03_08, number_03_09,
		number_04_01, number_04_02, number_04_03, number_04_04, number_04_05, number_04_06, number_04_07, number_04_08, number_04_09,
		number_05_01, number_05_02, number_05_03, number_05_04, number_05_05, number_05_06, number_05_07, number_05_08, number_05_09,
		number_06_01, number_06_02, number_06_03, number_06_04, number_06_05, number_06_06, number_06_07, number_06_08, number_06_09,
		number_07_01, number_07_02, number_07_03, number_07_04, number_07_05, number_07_06, number_07_07, number_07_08, number_07_09,
		number_08_01, number_08_02, number_08_03, number_08_04, number_08_05, number_08_06, number_08_07, number_08_08, number_08_09,
		number_09_01, number_09_02, number_09_03, number_09_04, number_09_05, number_09_06, number_09_07, number_09_08, number_09_09
	]

	yet = 0
	contador = 0
	while contador < 81:
		if num_list[contador].cget("text") != "":
			yet += 1
			contador += 1
		else:
			contador += 1

	if yet == 81:
		fill_valid = True
	else:
		fill_valid = False

def completed():
	num_list = [
		number_01_01, number_01_02, number_01_03, number_01_04, number_01_05, number_01_06, number_01_07, number_01_08, number_01_09,
		number_02_01, number_02_02, number_02_03, number_02_04, number_02_05, number_02_06, number_02_07, number_02_08, number_02_09,
		number_03_01, number_03_02, number_03_03, number_03_04, number_03_05, number_03_06, number_03_07, number_03_08, number_03_09,
		number_04_01, number_04_02, number_04_03, number_04_04, number_04_05, number_04_06, number_04_07, number_04_08, number_04_09,
		number_05_01, number_05_02, number_05_03, number_05_04, number_05_05, number_05_06, number_05_07, number_05_08, number_05_09,
		number_06_01, number_06_02, number_06_03, number_06_04, number_06_05, number_06_06, number_06_07, number_06_08, number_06_09,
		number_07_01, number_07_02, number_07_03, number_07_04, number_07_05, number_07_06, number_07_07, number_07_08, number_07_09,
		number_08_01, number_08_02, number_08_03, number_08_04, number_08_05, number_08_06, number_08_07, number_08_08, number_08_09,
		number_09_01, number_09_02, number_09_03, number_09_04, number_09_05, number_09_06, number_09_07, number_09_08, number_09_09
	]

	counter = 0
	while counter < 81:
		num_list[counter].config(state=DISABLED)
		counter += 1

	change_list = [
		change_01, change_02, change_03, change_04, change_05, change_06, change_07, change_08, change_09, change_00
	]

	counter = 0
	while counter < 9:
		change_list[counter].config(state=DISABLED)
		counter += 1

	full = Tk()
	full.title("Sudoku completed")
	full.resizable(0, 0)
	def mydestroy():
		full.destroy()
	full_msg = Label(full, text="Congratulations, you´ve completed sudoku")
	acept = Button(full, text="Acept", command=mydestroy)
	full_msg.grid(row=0, column=0, padx=4, pady=4)
	acept.grid(row=1, column=1, padx=4, pady=4)
	full.mainloop()

def wrong():
	full = Tk()
	full.title("Wrong solution")
	full.resizable(0, 0)
	def mydestroy():
		full.destroy()
	full_msg = Label(full, text="You hasn´t solved correctly sudoku >:(")
	acept = Button(full, text="Acept", command=mydestroy)
	full_msg.grid(row=0, column=0, padx=4, pady=4)
	acept.grid(row=1, column=1, padx=4, pady=4)
	full.mainloop()

def check_true():
	global solved_sudoku

	num_list = [
		number_01_01, number_01_02, number_01_03, number_02_01, number_02_02, number_02_03, number_03_01, number_03_02, number_03_03,
		number_01_04, number_01_05, number_01_06, number_02_04, number_02_05, number_02_06, number_03_04, number_03_05, number_03_06,
		number_01_07, number_01_08, number_01_09, number_02_07, number_02_08, number_02_09, number_03_07, number_03_08, number_03_09,
		number_04_01, number_04_02, number_04_03, number_05_01, number_05_02, number_05_03, number_06_01, number_06_02, number_06_03,
		number_04_04, number_04_05, number_04_06, number_05_04, number_05_05, number_05_06, number_06_04, number_06_05, number_06_06,
		number_04_07, number_04_08, number_04_09, number_05_07, number_05_08, number_05_09, number_06_07, number_06_08, number_06_09,
		number_07_01, number_07_02, number_07_03, number_08_01, number_08_02, number_08_03, number_09_01, number_09_02, number_09_03,
		number_07_04, number_07_05, number_07_06, number_08_04, number_08_05, number_08_06, number_09_04, number_09_05, number_09_06,
		number_07_07, number_07_08, number_07_09, number_08_07, number_08_08, number_08_09, number_09_07, number_09_08, number_09_09,
	]

	yet = 0
	counter = 0
	while counter < 81:
		if num_list[counter].cget("text") == solution[counter]:
			counter += 1
			yet += 1
		else:
			break

	if yet == 81:
		completed()
	else:
		wrong()

def new_number(new):
	global change_number
	change_number = new

def num_change():
	return change_number

def select_01_01():
	number_01_01.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_01_02():
	number_01_02.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_01_03():
	number_01_03.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_01_04():
	number_01_04.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_01_05():
	number_01_05.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_01_06():
	number_01_06.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_01_07():
	number_01_07.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_01_08():
	number_01_08.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_01_09():
	number_01_09.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_02_01():
	number_02_01.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_02_02():
	number_02_02.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_02_03():
	number_02_03.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_02_04():
	number_02_04.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_02_05():
	number_02_05.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_02_06():
	number_02_06.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_02_07():
	number_02_07.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_02_08():
	number_02_08.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_02_09():
	number_02_09.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_03_01():
	number_03_01.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_03_02():
	number_03_02.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_03_03():
	number_03_03.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_03_04():
	number_03_04.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_03_05():
	number_03_05.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_03_06():
	number_03_06.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_03_07():
	number_03_07.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_03_08():
	number_03_08.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_03_09():
	number_03_09.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_04_01():
	number_04_01.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_04_02():
	number_04_02.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_04_03():
	number_04_03.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_04_04():
	number_04_04.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_04_05():
	number_04_05.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_04_06():
	number_04_06.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_04_07():
	number_04_07.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_04_08():
	number_04_08.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_04_09():
	number_04_09.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_05_01():
	number_05_01.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_05_02():
	number_05_02.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_05_03():
	number_05_03.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_05_04():
	number_05_04.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_05_05():
	number_05_05.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_05_06():
	number_05_06.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_05_07():
	number_05_07.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_05_08():
	number_05_08.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_05_09():
	number_05_09.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_06_01():
	number_06_01.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_06_02():
	number_06_02.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_06_03():
	number_06_03.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_06_04():
	number_06_04.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_06_05():
	number_06_05.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_06_06():
	number_06_06.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_06_07():
	number_06_07.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_06_08():
	number_06_08.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_06_09():
	number_06_09.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_07_01():
	number_07_01.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_07_02():
	number_07_02.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_07_03():
	number_07_03.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_07_04():
	number_07_04.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_07_05():
	number_07_05.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_07_06():
	number_07_06.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_07_07():
	number_07_07.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_07_08():
	number_07_08.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_07_09():
	number_07_09.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_08_01():
	number_08_01.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_08_02():
	number_08_02.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_08_03():
	number_08_03.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_08_04():
	number_08_04.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_08_05():
	number_08_05.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_08_06():
	number_08_06.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_08_07():
	number_08_07.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_08_08():
	number_08_08.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_08_09():
	number_08_09.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_09_01():
	number_09_01.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_09_02():
	number_09_02.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_09_03():
	number_09_03.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_09_04():
	number_09_04.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_09_05():
	number_09_05.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_09_06():
	number_09_06.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_09_07():
	number_09_07.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_09_08():
	number_09_08.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def select_09_09():
	number_09_09.config(text=num_change())
	for_fill()
	if fill_valid == True:
		check_true()
	else:
		pass

def global_set01():
	new_number("1")

def global_set02():
	new_number("2")

def global_set03():
	new_number("3")

def global_set04():
	new_number("4")

def global_set05():
	new_number("5")

def global_set06():
	new_number("6")

def global_set07():
	new_number("7")

def global_set08():
	new_number("8")

def global_set09():
	new_number("9")

def global_set00():
	new_number("")

root = Tk()
root.title("Sudoku")
root.resizable(0, 0)

game = Frame(root)

frame01 = Frame(game)
number_01_01 = Button(frame01, width=2, height=1, state=DISABLED, command=select_01_01, relief=GROOVE)
number_01_02 = Button(frame01, width=2, height=1, state=DISABLED, command=select_01_02, relief=GROOVE)
number_01_03 = Button(frame01, width=2, height=1, state=DISABLED, command=select_01_03, relief=GROOVE)
number_01_04 = Button(frame01, width=2, height=1, state=DISABLED, command=select_01_04, relief=GROOVE)
number_01_05 = Button(frame01, width=2, height=1, state=DISABLED, command=select_01_05, relief=GROOVE)
number_01_06 = Button(frame01, width=2, height=1, state=DISABLED, command=select_01_06, relief=GROOVE)
number_01_07 = Button(frame01, width=2, height=1, state=DISABLED, command=select_01_07, relief=GROOVE)
number_01_08 = Button(frame01, width=2, height=1, state=DISABLED, command=select_01_08, relief=GROOVE)
number_01_09 = Button(frame01, width=2, height=1, state=DISABLED, command=select_01_09, relief=GROOVE)

frame02 = Frame(game)
number_02_01 = Button(frame02, width=2, height=1, state=DISABLED, command=select_02_01, relief=GROOVE)
number_02_02 = Button(frame02, width=2, height=1, state=DISABLED, command=select_02_02, relief=GROOVE)
number_02_03 = Button(frame02, width=2, height=1, state=DISABLED, command=select_02_03, relief=GROOVE)
number_02_04 = Button(frame02, width=2, height=1, state=DISABLED, command=select_02_04, relief=GROOVE)
number_02_05 = Button(frame02, width=2, height=1, state=DISABLED, command=select_02_05, relief=GROOVE)
number_02_06 = Button(frame02, width=2, height=1, state=DISABLED, command=select_02_06, relief=GROOVE)
number_02_07 = Button(frame02, width=2, height=1, state=DISABLED, command=select_02_07, relief=GROOVE)
number_02_08 = Button(frame02, width=2, height=1, state=DISABLED, command=select_02_08, relief=GROOVE)
number_02_09 = Button(frame02, width=2, height=1, state=DISABLED, command=select_02_09, relief=GROOVE)

frame03 = Frame(game)
number_03_01 = Button(frame03, width=2, height=1, state=DISABLED, command=select_03_01, relief=GROOVE)
number_03_02 = Button(frame03, width=2, height=1, state=DISABLED, command=select_03_02, relief=GROOVE)
number_03_03 = Button(frame03, width=2, height=1, state=DISABLED, command=select_03_03, relief=GROOVE)
number_03_04 = Button(frame03, width=2, height=1, state=DISABLED, command=select_03_04, relief=GROOVE)
number_03_05 = Button(frame03, width=2, height=1, state=DISABLED, command=select_03_05, relief=GROOVE)
number_03_06 = Button(frame03, width=2, height=1, state=DISABLED, command=select_03_06, relief=GROOVE)
number_03_07 = Button(frame03, width=2, height=1, state=DISABLED, command=select_03_07, relief=GROOVE)
number_03_08 = Button(frame03, width=2, height=1, state=DISABLED, command=select_03_08, relief=GROOVE)
number_03_09 = Button(frame03, width=2, height=1, state=DISABLED, command=select_03_09, relief=GROOVE)

frame04 = Frame(game)
number_04_01 = Button(frame04, width=2, height=1, state=DISABLED, command=select_04_01, relief=GROOVE)
number_04_02 = Button(frame04, width=2, height=1, state=DISABLED, command=select_04_02, relief=GROOVE)
number_04_03 = Button(frame04, width=2, height=1, state=DISABLED, command=select_04_03, relief=GROOVE)
number_04_04 = Button(frame04, width=2, height=1, state=DISABLED, command=select_04_04, relief=GROOVE)
number_04_05 = Button(frame04, width=2, height=1, state=DISABLED, command=select_04_05, relief=GROOVE)
number_04_06 = Button(frame04, width=2, height=1, state=DISABLED, command=select_04_06, relief=GROOVE)
number_04_07 = Button(frame04, width=2, height=1, state=DISABLED, command=select_04_07, relief=GROOVE)
number_04_08 = Button(frame04, width=2, height=1, state=DISABLED, command=select_04_08, relief=GROOVE)
number_04_09 = Button(frame04, width=2, height=1, state=DISABLED, command=select_04_09, relief=GROOVE)

frame05 = Frame(game)
number_05_01 = Button(frame05, width=2, height=1, state=DISABLED, command=select_05_01, relief=GROOVE)
number_05_02 = Button(frame05, width=2, height=1, state=DISABLED, command=select_05_02, relief=GROOVE)
number_05_03 = Button(frame05, width=2, height=1, state=DISABLED, command=select_05_03, relief=GROOVE)
number_05_04 = Button(frame05, width=2, height=1, state=DISABLED, command=select_05_04, relief=GROOVE)
number_05_05 = Button(frame05, width=2, height=1, state=DISABLED, command=select_05_05, relief=GROOVE)
number_05_06 = Button(frame05, width=2, height=1, state=DISABLED, command=select_05_06, relief=GROOVE)
number_05_07 = Button(frame05, width=2, height=1, state=DISABLED, command=select_05_07, relief=GROOVE)
number_05_08 = Button(frame05, width=2, height=1, state=DISABLED, command=select_05_08, relief=GROOVE)
number_05_09 = Button(frame05, width=2, height=1, state=DISABLED, command=select_05_09, relief=GROOVE)

frame06 = Frame(game)
number_06_01 = Button(frame06, width=2, height=1, state=DISABLED, command=select_06_01, relief=GROOVE)
number_06_02 = Button(frame06, width=2, height=1, state=DISABLED, command=select_06_02, relief=GROOVE)
number_06_03 = Button(frame06, width=2, height=1, state=DISABLED, command=select_06_03, relief=GROOVE)
number_06_04 = Button(frame06, width=2, height=1, state=DISABLED, command=select_06_04, relief=GROOVE)
number_06_05 = Button(frame06, width=2, height=1, state=DISABLED, command=select_06_05, relief=GROOVE)
number_06_06 = Button(frame06, width=2, height=1, state=DISABLED, command=select_06_06, relief=GROOVE)
number_06_07 = Button(frame06, width=2, height=1, state=DISABLED, command=select_06_07, relief=GROOVE)
number_06_08 = Button(frame06, width=2, height=1, state=DISABLED, command=select_06_08, relief=GROOVE)
number_06_09 = Button(frame06, width=2, height=1, state=DISABLED, command=select_06_09, relief=GROOVE)

frame07 = Frame(game)
number_07_01 = Button(frame07, width=2, height=1, state=DISABLED, command=select_07_01, relief=GROOVE)
number_07_02 = Button(frame07, width=2, height=1, state=DISABLED, command=select_07_02, relief=GROOVE)
number_07_03 = Button(frame07, width=2, height=1, state=DISABLED, command=select_07_03, relief=GROOVE)
number_07_04 = Button(frame07, width=2, height=1, state=DISABLED, command=select_07_04, relief=GROOVE)
number_07_05 = Button(frame07, width=2, height=1, state=DISABLED, command=select_07_05, relief=GROOVE)
number_07_06 = Button(frame07, width=2, height=1, state=DISABLED, command=select_07_06, relief=GROOVE)
number_07_07 = Button(frame07, width=2, height=1, state=DISABLED, command=select_07_07, relief=GROOVE)
number_07_08 = Button(frame07, width=2, height=1, state=DISABLED, command=select_07_08, relief=GROOVE)
number_07_09 = Button(frame07, width=2, height=1, state=DISABLED, command=select_07_09, relief=GROOVE)

frame08 = Frame(game)
number_08_01 = Button(frame08, width=2, height=1, state=DISABLED, command=select_08_01, relief=GROOVE)
number_08_02 = Button(frame08, width=2, height=1, state=DISABLED, command=select_08_02, relief=GROOVE)
number_08_03 = Button(frame08, width=2, height=1, state=DISABLED, command=select_08_03, relief=GROOVE)
number_08_04 = Button(frame08, width=2, height=1, state=DISABLED, command=select_08_04, relief=GROOVE)
number_08_05 = Button(frame08, width=2, height=1, state=DISABLED, command=select_08_05, relief=GROOVE)
number_08_06 = Button(frame08, width=2, height=1, state=DISABLED, command=select_08_06, relief=GROOVE)
number_08_07 = Button(frame08, width=2, height=1, state=DISABLED, command=select_08_07, relief=GROOVE)
number_08_08 = Button(frame08, width=2, height=1, state=DISABLED, command=select_08_08, relief=GROOVE)
number_08_09 = Button(frame08, width=2, height=1, state=DISABLED, command=select_08_09, relief=GROOVE)

frame09 = Frame(game)
number_09_01 = Button(frame09, width=2, height=1, state=DISABLED, command=select_09_01, relief=GROOVE)
number_09_02 = Button(frame09, width=2, height=1, state=DISABLED, command=select_09_02, relief=GROOVE)
number_09_03 = Button(frame09, width=2, height=1, state=DISABLED, command=select_09_03, relief=GROOVE)
number_09_04 = Button(frame09, width=2, height=1, state=DISABLED, command=select_09_04, relief=GROOVE)
number_09_05 = Button(frame09, width=2, height=1, state=DISABLED, command=select_09_05, relief=GROOVE)
number_09_06 = Button(frame09, width=2, height=1, state=DISABLED, command=select_09_06, relief=GROOVE)
number_09_07 = Button(frame09, width=2, height=1, state=DISABLED, command=select_09_07, relief=GROOVE)
number_09_08 = Button(frame09, width=2, height=1, state=DISABLED, command=select_09_08, relief=GROOVE)
number_09_09 = Button(frame09, width=2, height=1, state=DISABLED, command=select_09_09, relief=GROOVE)

number_frame = Frame(root)
number_f01 = Frame(number_frame)
number_f02 = Frame(number_frame)
number_f03 = Frame(number_frame)
change_01 = Button(number_f01, width=2, height=1, state=DISABLED, text="1", command=global_set01, relief=GROOVE)
change_02 = Button(number_f01, width=2, height=1, state=DISABLED, text="2", command=global_set02, relief=GROOVE)
change_03 = Button(number_f01, width=2, height=1, state=DISABLED, text="3", command=global_set03, relief=GROOVE)
change_04 = Button(number_f02, width=2, height=1, state=DISABLED, text="4", command=global_set04, relief=GROOVE)
change_05 = Button(number_f02, width=2, height=1, state=DISABLED, text="5", command=global_set05, relief=GROOVE)
change_06 = Button(number_f02, width=2, height=1, state=DISABLED, text="6", command=global_set06, relief=GROOVE)
change_07 = Button(number_f03, width=2, height=1, state=DISABLED, text="7", command=global_set07, relief=GROOVE)
change_08 = Button(number_f03, width=2, height=1, state=DISABLED, text="8", command=global_set08, relief=GROOVE)
change_09 = Button(number_f03, width=2, height=1, state=DISABLED, text="9", command=global_set09, relief=GROOVE)
change_00 = Button(root, width=2, height=1, state=DISABLED, text="", command=global_set00, relief=GROOVE)

def number_in_row(grid, row, number):
	return number in grid[row]


def number_in_col(grid, col, number):
	return number in (row[col] for row in grid)


def number_in_box(grid, row, col, number):
	box_row, box_col = box_by_pos(row, col)
	numbers_in_box = unpack(
		row[box_col*3:box_col*3 + 3]
		for row in grid[box_row*3:box_row*3 + 3]
	)
	return number in numbers_in_box


def reduce(n):
	n /= 3
	if n == 0 or n != int(n):
		n += 1
	return int(n)


def box_by_pos(row, col):
	row += 1
	col += 1
	return reduce(row) - 1, reduce(col) - 1


def unpack(iterable):
	for item in iterable:
		yield from item


def get_possible_numbers(grid, row, col):
	for number in range(1, 10):
		if (not number_in_row(grid, row, number) and
			not number_in_col(grid, col, number) and
			not number_in_box(grid, row, col, number)):
			yield number

def new_game():
	new_number("")

	new_num_list = [
		number_01_01, number_01_02, number_01_03, number_01_04, number_01_05, number_01_06, number_01_07, number_01_08, number_01_09,
		number_02_01, number_02_02, number_02_03, number_02_04, number_02_05, number_02_06, number_02_07, number_02_08, number_02_09,
		number_03_01, number_03_02, number_03_03, number_03_04, number_03_05, number_03_06, number_03_07, number_03_08, number_03_09,
		number_04_01, number_04_02, number_04_03, number_04_04, number_04_05, number_04_06, number_04_07, number_04_08, number_04_09,
		number_05_01, number_05_02, number_05_03, number_05_04, number_05_05, number_05_06, number_05_07, number_05_08, number_05_09,
		number_06_01, number_06_02, number_06_03, number_06_04, number_06_05, number_06_06, number_06_07, number_06_08, number_06_09,
		number_07_01, number_07_02, number_07_03, number_07_04, number_07_05, number_07_06, number_07_07, number_07_08, number_07_09,
		number_08_01, number_08_02, number_08_03, number_08_04, number_08_05, number_08_06, number_08_07, number_08_08, number_08_09,
		number_09_01, number_09_02, number_09_03, number_09_04, number_09_05, number_09_06, number_09_07, number_09_08, number_09_09
	]

	new_counter = 0
	while new_counter < 81:
		new_num_list[new_counter].config(text="", state=DISABLED)
		new_counter += 1

	while True:
		grid = [
			[0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0],
		]
		
		s = \
		"""\
		+-----------------------+
		| {} {} {} | {} {} {} | {} {} {} |
		| {} {} {} | {} {} {} | {} {} {} |
		| {} {} {} | {} {} {} | {} {} {} |
		+-----------------------+
		| {} {} {} | {} {} {} | {} {} {} |
		| {} {} {} | {} {} {} | {} {} {} |
		| {} {} {} | {} {} {} | {} {} {} |
		+-----------------------+
		| {} {} {} | {} {} {} | {} {} {} |
		| {} {} {} | {} {} {} | {} {} {} |
		| {} {} {} | {} {} {} | {} {} {} |
		+-----------------------+
		"""
		
		while True:
			possible_numbers = {
				(row, col): None for row in range(9) for col in range(9)
			}
			for row in range(9):
				for col in range(9):
					number = grid[row][col]
					if number == 0:
						options = list(
							get_possible_numbers(grid, row, col)
						)
						if options:
							possible_numbers[(row, col)] = options
			possible_numbers = sorted(
				(
					(k, v)
					for (k, v) in possible_numbers.items()
					if v is not None
				),
				key=lambda kv: len(kv[1])
			)
			
			if possible_numbers:
				(row, col), numbers = possible_numbers[0]
				grid[row][col] = choice(numbers)
			else:
				break
		if 0 not in unpack(grid):
			print(s.format(*(unpack(grid))))
			break

	num_01 = str(grid[0][0])
	num_02 = str(grid[0][1])
	num_03 = str(grid[0][2])
	num_04 = str(grid[0][3])
	num_05 = str(grid[0][4])
	num_06 = str(grid[0][5])
	num_07 = str(grid[0][6])
	num_08 = str(grid[0][7])
	num_09 = str(grid[0][8])
	num_10 = str(grid[1][0])
	num_11 = str(grid[1][1])
	num_12 = str(grid[1][2])
	num_13 = str(grid[1][3])
	num_14 = str(grid[1][4])
	num_15 = str(grid[1][5])
	num_16 = str(grid[1][6])
	num_17 = str(grid[1][7])
	num_18 = str(grid[1][8])
	num_19 = str(grid[2][0])
	num_20 = str(grid[2][1])
	num_21 = str(grid[2][2])
	num_22 = str(grid[2][3])
	num_23 = str(grid[2][4])
	num_24 = str(grid[2][5])
	num_25 = str(grid[2][6])
	num_26 = str(grid[2][7])
	num_27 = str(grid[2][8])
	num_28 = str(grid[3][0])
	num_29 = str(grid[3][1])
	num_30 = str(grid[3][2])
	num_31 = str(grid[3][3])
	num_32 = str(grid[3][4])
	num_33 = str(grid[3][5])
	num_34 = str(grid[3][6])
	num_35 = str(grid[3][7])
	num_36 = str(grid[3][8])
	num_37 = str(grid[4][0])
	num_38 = str(grid[4][1])
	num_39 = str(grid[4][2])
	num_40 = str(grid[4][3])
	num_41 = str(grid[4][4])
	num_42 = str(grid[4][5])
	num_43 = str(grid[4][6])
	num_44 = str(grid[4][7])
	num_45 = str(grid[4][8])
	num_46 = str(grid[5][0])
	num_47 = str(grid[5][1])
	num_48 = str(grid[5][2])
	num_49 = str(grid[5][3])
	num_50 = str(grid[5][4])
	num_51 = str(grid[5][5])
	num_52 = str(grid[5][6])
	num_53 = str(grid[5][7])
	num_54 = str(grid[5][8])
	num_55 = str(grid[6][0])
	num_56 = str(grid[6][1])
	num_57 = str(grid[6][2])
	num_58 = str(grid[6][3])
	num_59 = str(grid[6][4])
	num_60 = str(grid[6][5])
	num_61 = str(grid[6][6])
	num_62 = str(grid[6][7])
	num_63 = str(grid[6][8])
	num_64 = str(grid[7][0])
	num_65 = str(grid[7][1])
	num_66 = str(grid[7][2])
	num_67 = str(grid[7][3])
	num_68 = str(grid[7][4])
	num_69 = str(grid[7][5])
	num_70 = str(grid[7][6])
	num_71 = str(grid[7][7])
	num_72 = str(grid[7][8])
	num_73 = str(grid[8][0])
	num_74 = str(grid[8][1])
	num_75 = str(grid[8][2])
	num_76 = str(grid[8][3])
	num_77 = str(grid[8][4])
	num_78 = str(grid[8][5])
	num_79 = str(grid[8][6])
	num_80 = str(grid[8][7])
	num_81 = str(grid[8][8])

	global solution
	solution = [
		num_01, num_02, num_03, num_04, num_05, num_06, num_07, num_08, num_09,
		num_10, num_11, num_12, num_13, num_14, num_15, num_16, num_17, num_18,
		num_19, num_20, num_21, num_22, num_23, num_24, num_25, num_26, num_27,
		num_28, num_29, num_30, num_31, num_32, num_33, num_34, num_35, num_36,
		num_37, num_38, num_39, num_40, num_41, num_42, num_43, num_44, num_45,
		num_46, num_47, num_48, num_49, num_50, num_51, num_52, num_53, num_54,
		num_55, num_56, num_57, num_58, num_59, num_60, num_61, num_62, num_63,
		num_64, num_65, num_66, num_67, num_68, num_69, num_70, num_71, num_72,
		num_73, num_74, num_75, num_76, num_77, num_78, num_79, num_80, num_81
	]

	number_01_01.config(text=num_01)
	number_01_02.config(text=num_02)
	number_01_03.config(text=num_03)
	number_02_01.config(text=num_04)
	number_02_02.config(text=num_05)
	number_02_03.config(text=num_06)
	number_03_01.config(text=num_07)
	number_03_02.config(text=num_08)
	number_03_03.config(text=num_09)
	number_01_04.config(text=num_10)
	number_01_05.config(text=num_11)
	number_01_06.config(text=num_12)
	number_02_04.config(text=num_13)
	number_02_05.config(text=num_14)
	number_02_06.config(text=num_15)
	number_03_04.config(text=num_16)
	number_03_05.config(text=num_17)
	number_03_06.config(text=num_18)
	number_01_07.config(text=num_19)
	number_01_08.config(text=num_20)
	number_01_09.config(text=num_21)
	number_02_07.config(text=num_22)
	number_02_08.config(text=num_23)
	number_02_09.config(text=num_24)
	number_03_07.config(text=num_25)
	number_03_08.config(text=num_26)
	number_03_09.config(text=num_27)
	number_04_01.config(text=num_28)
	number_04_02.config(text=num_29)
	number_04_03.config(text=num_30)
	number_05_01.config(text=num_31)
	number_05_02.config(text=num_32)
	number_05_03.config(text=num_33)
	number_06_01.config(text=num_34)
	number_06_02.config(text=num_35)
	number_06_03.config(text=num_36)
	number_04_04.config(text=num_37)
	number_04_05.config(text=num_38)
	number_04_06.config(text=num_39)
	number_05_04.config(text=num_40)
	number_05_05.config(text=num_41)
	number_05_06.config(text=num_42)
	number_06_04.config(text=num_43)
	number_06_05.config(text=num_44)
	number_06_06.config(text=num_45)
	number_04_07.config(text=num_46)
	number_04_08.config(text=num_47)
	number_04_09.config(text=num_48)
	number_05_07.config(text=num_49)
	number_05_08.config(text=num_50)
	number_05_09.config(text=num_51)
	number_06_07.config(text=num_52)
	number_06_08.config(text=num_53)
	number_06_09.config(text=num_54)
	number_07_01.config(text=num_55)
	number_07_02.config(text=num_56)
	number_07_03.config(text=num_57)
	number_08_01.config(text=num_58)
	number_08_02.config(text=num_59)
	number_08_03.config(text=num_60)
	number_09_01.config(text=num_61)
	number_09_02.config(text=num_62)
	number_09_03.config(text=num_63)
	number_07_04.config(text=num_64)
	number_07_05.config(text=num_65)
	number_07_06.config(text=num_66)
	number_08_04.config(text=num_67)
	number_08_05.config(text=num_68)
	number_08_06.config(text=num_69)
	number_09_04.config(text=num_70)
	number_09_05.config(text=num_71)
	number_09_06.config(text=num_72)
	number_07_07.config(text=num_73)
	number_07_08.config(text=num_74)
	number_07_09.config(text=num_75)
	number_08_07.config(text=num_76)
	number_08_08.config(text=num_77)
	number_08_09.config(text=num_78)
	number_09_07.config(text=num_79)
	number_09_08.config(text=num_80)
	number_09_09.config(text=num_81)

	num_list = [
		number_01_01, number_01_02, number_01_03, number_01_04, number_01_05, number_01_06, number_01_07, number_01_08, number_01_09,
		number_02_01, number_02_02, number_02_03, number_02_04, number_02_05, number_02_06, number_02_07, number_02_08, number_02_09,
		number_03_01, number_03_02, number_03_03, number_03_04, number_03_05, number_03_06, number_03_07, number_03_08, number_03_09,
		number_04_01, number_04_02, number_04_03, number_04_04, number_04_05, number_04_06, number_04_07, number_04_08, number_04_09,
		number_05_01, number_05_02, number_05_03, number_05_04, number_05_05, number_05_06, number_05_07, number_05_08, number_05_09,
		number_06_01, number_06_02, number_06_03, number_06_04, number_06_05, number_06_06, number_06_07, number_06_08, number_06_09,
		number_07_01, number_07_02, number_07_03, number_07_04, number_07_05, number_07_06, number_07_07, number_07_08, number_07_09,
		number_08_01, number_08_02, number_08_03, number_08_04, number_08_05, number_08_06, number_08_07, number_08_08, number_08_09,
		number_09_01, number_09_02, number_09_03, number_09_04, number_09_05, number_09_06, number_09_07, number_09_08, number_09_09
	]

	max_num = randint(49, 54)

	counter = 0
	while counter < max_num:
		delete_candidate = choice(num_list)
		if delete_candidate.cget("text") != "":
			delete_candidate.config(state=NORMAL, text="")
			counter += 1
		else:
			continue

	change_01.config(state=NORMAL)
	change_02.config(state=NORMAL)
	change_03.config(state=NORMAL)
	change_04.config(state=NORMAL)
	change_05.config(state=NORMAL)
	change_06.config(state=NORMAL)
	change_07.config(state=NORMAL)
	change_08.config(state=NORMAL)
	change_09.config(state=NORMAL)
	change_00.config(state=NORMAL)

def pop_up():
	pw = Tk()
	pw.title("Advertencia")
	pw.resizable(0, 0)
	def mydestroy():
		pw.destroy()
	pw_msg = Label(pw, text="Don´t write a impossible sudoku.\nYou may cause a PC freeze...")
	acept = Button(pw, text="Acept", command=mydestroy)
	pw_msg.grid(row=0, column=0, padx=4, pady=4)
	acept.grid(row=1, column=1, padx=4, pady=4)
	pw.mainloop()

def custom_game():
	new_number("")
	num_list = [
		number_01_01, number_01_02, number_01_03, number_01_04, number_01_05, number_01_06, number_01_07, number_01_08, number_01_09,
		number_02_01, number_02_02, number_02_03, number_02_04, number_02_05, number_02_06, number_02_07, number_02_08, number_02_09,
		number_03_01, number_03_02, number_03_03, number_03_04, number_03_05, number_03_06, number_03_07, number_03_08, number_03_09,
		number_04_01, number_04_02, number_04_03, number_04_04, number_04_05, number_04_06, number_04_07, number_04_08, number_04_09,
		number_05_01, number_05_02, number_05_03, number_05_04, number_05_05, number_05_06, number_05_07, number_05_08, number_05_09,
		number_06_01, number_06_02, number_06_03, number_06_04, number_06_05, number_06_06, number_06_07, number_06_08, number_06_09,
		number_07_01, number_07_02, number_07_03, number_07_04, number_07_05, number_07_06, number_07_07, number_07_08, number_07_09,
		number_08_01, number_08_02, number_08_03, number_08_04, number_08_05, number_08_06, number_08_07, number_08_08, number_08_09,
		number_09_01, number_09_02, number_09_03, number_09_04, number_09_05, number_09_06, number_09_07, number_09_08, number_09_09
	]

	counter = 0
	while counter < 81:
		num_list[counter].config(text="", state=NORMAL)
		counter += 1

	change_list = [
		change_01, change_02, change_03, change_04, change_05, change_06, change_07, change_08, change_09, change_00
	]

	counter = 0
	while counter < 10:
		change_list[counter].config(state=NORMAL)
		counter += 1

	pop_up()

def solve():
	num_list = [
		number_01_01, number_01_02, number_01_03, number_01_04, number_01_05, number_01_06, number_01_07, number_01_08, number_01_09,
		number_02_01, number_02_02, number_02_03, number_02_04, number_02_05, number_02_06, number_02_07, number_02_08, number_02_09,
		number_03_01, number_03_02, number_03_03, number_03_04, number_03_05, number_03_06, number_03_07, number_03_08, number_03_09,
		number_04_01, number_04_02, number_04_03, number_04_04, number_04_05, number_04_06, number_04_07, number_04_08, number_04_09,
		number_05_01, number_05_02, number_05_03, number_05_04, number_05_05, number_05_06, number_05_07, number_05_08, number_05_09,
		number_06_01, number_06_02, number_06_03, number_06_04, number_06_05, number_06_06, number_06_07, number_06_08, number_06_09,
		number_07_01, number_07_02, number_07_03, number_07_04, number_07_05, number_07_06, number_07_07, number_07_08, number_07_09,
		number_08_01, number_08_02, number_08_03, number_08_04, number_08_05, number_08_06, number_08_07, number_08_08, number_08_09,
		number_09_01, number_09_02, number_09_03, number_09_04, number_09_05, number_09_06, number_09_07, number_09_08, number_09_09
	]

	counter = 0
	while counter < 81:
		if num_list[counter].cget("text") == "":
			num_list[counter].config(text="0")
		else:
			pass

		counter += 1

	while True:
		grid = [
			[int(number_01_01.cget("text")), int(number_01_02.cget("text")), int(number_01_03.cget("text")), int(number_02_01.cget("text")), int(number_02_02.cget("text")), int(number_02_03.cget("text")), int(number_03_01.cget("text")), int(number_03_02.cget("text")), int(number_03_03.cget("text"))],
			[int(number_01_04.cget("text")), int(number_01_05.cget("text")), int(number_01_06.cget("text")), int(number_02_04.cget("text")), int(number_02_05.cget("text")), int(number_02_06.cget("text")), int(number_03_04.cget("text")), int(number_03_05.cget("text")), int(number_03_06.cget("text"))],
			[int(number_01_07.cget("text")), int(number_01_08.cget("text")), int(number_01_09.cget("text")), int(number_02_07.cget("text")), int(number_02_08.cget("text")), int(number_02_09.cget("text")), int(number_03_07.cget("text")), int(number_03_08.cget("text")), int(number_03_09.cget("text"))],
			[int(number_04_01.cget("text")), int(number_04_02.cget("text")), int(number_04_03.cget("text")), int(number_05_01.cget("text")), int(number_05_02.cget("text")), int(number_05_03.cget("text")), int(number_06_01.cget("text")), int(number_06_02.cget("text")), int(number_06_03.cget("text"))],
			[int(number_04_04.cget("text")), int(number_04_05.cget("text")), int(number_04_06.cget("text")), int(number_05_04.cget("text")), int(number_05_05.cget("text")), int(number_05_06.cget("text")), int(number_06_04.cget("text")), int(number_06_05.cget("text")), int(number_06_06.cget("text"))],
			[int(number_04_07.cget("text")), int(number_04_08.cget("text")), int(number_04_09.cget("text")), int(number_05_07.cget("text")), int(number_05_08.cget("text")), int(number_05_09.cget("text")), int(number_06_07.cget("text")), int(number_06_08.cget("text")), int(number_06_09.cget("text"))],
			[int(number_07_01.cget("text")), int(number_07_02.cget("text")), int(number_07_03.cget("text")), int(number_08_01.cget("text")), int(number_08_02.cget("text")), int(number_08_03.cget("text")), int(number_09_01.cget("text")), int(number_09_02.cget("text")), int(number_09_03.cget("text"))],
			[int(number_07_04.cget("text")), int(number_07_05.cget("text")), int(number_07_06.cget("text")), int(number_08_04.cget("text")), int(number_08_05.cget("text")), int(number_08_06.cget("text")), int(number_09_04.cget("text")), int(number_09_05.cget("text")), int(number_09_06.cget("text"))],
			[int(number_07_07.cget("text")), int(number_07_08.cget("text")), int(number_07_09.cget("text")), int(number_08_07.cget("text")), int(number_08_08.cget("text")), int(number_08_09.cget("text")), int(number_09_07.cget("text")), int(number_09_08.cget("text")), int(number_09_09.cget("text"))]
		]
		
		s = \
		"""\
		+-----------------------+
		| {} {} {} | {} {} {} | {} {} {} |
		| {} {} {} | {} {} {} | {} {} {} |
		| {} {} {} | {} {} {} | {} {} {} |
		+-----------------------+
		| {} {} {} | {} {} {} | {} {} {} |
		| {} {} {} | {} {} {} | {} {} {} |
		| {} {} {} | {} {} {} | {} {} {} |
		+-----------------------+
		| {} {} {} | {} {} {} | {} {} {} |
		| {} {} {} | {} {} {} | {} {} {} |
		| {} {} {} | {} {} {} | {} {} {} |
		+-----------------------+
		"""
		
		while True:
			possible_numbers = {
				(row, col): None for row in range(9) for col in range(9)
			}
			for row in range(9):
				for col in range(9):
					number = grid[row][col]
					if number == 0:
						options = list(
							get_possible_numbers(grid, row, col)
						)
						if options:
							possible_numbers[(row, col)] = options
			possible_numbers = sorted(
				(
					(k, v)
					for (k, v) in possible_numbers.items()
					if v is not None
				),
				key=lambda kv: len(kv[1])
			)
			
			if possible_numbers:
				(row, col), numbers = possible_numbers[0]
				grid[row][col] = choice(numbers)
			else:
				break
		if 0 not in unpack(grid):
			print(s.format(*(unpack(grid))))
			break

	num_01 = str(grid[0][0])
	num_02 = str(grid[0][1])
	num_03 = str(grid[0][2])
	num_04 = str(grid[0][3])
	num_05 = str(grid[0][4])
	num_06 = str(grid[0][5])
	num_07 = str(grid[0][6])
	num_08 = str(grid[0][7])
	num_09 = str(grid[0][8])
	num_10 = str(grid[1][0])
	num_11 = str(grid[1][1])
	num_12 = str(grid[1][2])
	num_13 = str(grid[1][3])
	num_14 = str(grid[1][4])
	num_15 = str(grid[1][5])
	num_16 = str(grid[1][6])
	num_17 = str(grid[1][7])
	num_18 = str(grid[1][8])
	num_19 = str(grid[2][0])
	num_20 = str(grid[2][1])
	num_21 = str(grid[2][2])
	num_22 = str(grid[2][3])
	num_23 = str(grid[2][4])
	num_24 = str(grid[2][5])
	num_25 = str(grid[2][6])
	num_26 = str(grid[2][7])
	num_27 = str(grid[2][8])
	num_28 = str(grid[3][0])
	num_29 = str(grid[3][1])
	num_30 = str(grid[3][2])
	num_31 = str(grid[3][3])
	num_32 = str(grid[3][4])
	num_33 = str(grid[3][5])
	num_34 = str(grid[3][6])
	num_35 = str(grid[3][7])
	num_36 = str(grid[3][8])
	num_37 = str(grid[4][0])
	num_38 = str(grid[4][1])
	num_39 = str(grid[4][2])
	num_40 = str(grid[4][3])
	num_41 = str(grid[4][4])
	num_42 = str(grid[4][5])
	num_43 = str(grid[4][6])
	num_44 = str(grid[4][7])
	num_45 = str(grid[4][8])
	num_46 = str(grid[5][0])
	num_47 = str(grid[5][1])
	num_48 = str(grid[5][2])
	num_49 = str(grid[5][3])
	num_50 = str(grid[5][4])
	num_51 = str(grid[5][5])
	num_52 = str(grid[5][6])
	num_53 = str(grid[5][7])
	num_54 = str(grid[5][8])
	num_55 = str(grid[6][0])
	num_56 = str(grid[6][1])
	num_57 = str(grid[6][2])
	num_58 = str(grid[6][3])
	num_59 = str(grid[6][4])
	num_60 = str(grid[6][5])
	num_61 = str(grid[6][6])
	num_62 = str(grid[6][7])
	num_63 = str(grid[6][8])
	num_64 = str(grid[7][0])
	num_65 = str(grid[7][1])
	num_66 = str(grid[7][2])
	num_67 = str(grid[7][3])
	num_68 = str(grid[7][4])
	num_69 = str(grid[7][5])
	num_70 = str(grid[7][6])
	num_71 = str(grid[7][7])
	num_72 = str(grid[7][8])
	num_73 = str(grid[8][0])
	num_74 = str(grid[8][1])
	num_75 = str(grid[8][2])
	num_76 = str(grid[8][3])
	num_77 = str(grid[8][4])
	num_78 = str(grid[8][5])
	num_79 = str(grid[8][6])
	num_80 = str(grid[8][7])
	num_81 = str(grid[8][8])
	number_01_01.config(text=num_01)
	number_01_02.config(text=num_02)
	number_01_03.config(text=num_03)
	number_02_01.config(text=num_04)
	number_02_02.config(text=num_05)
	number_02_03.config(text=num_06)
	number_03_01.config(text=num_07)
	number_03_02.config(text=num_08)
	number_03_03.config(text=num_09)
	number_01_04.config(text=num_10)
	number_01_05.config(text=num_11)
	number_01_06.config(text=num_12)
	number_02_04.config(text=num_13)
	number_02_05.config(text=num_14)
	number_02_06.config(text=num_15)
	number_03_04.config(text=num_16)
	number_03_05.config(text=num_17)
	number_03_06.config(text=num_18)
	number_01_07.config(text=num_19)
	number_01_08.config(text=num_20)
	number_01_09.config(text=num_21)
	number_02_07.config(text=num_22)
	number_02_08.config(text=num_23)
	number_02_09.config(text=num_24)
	number_03_07.config(text=num_25)
	number_03_08.config(text=num_26)
	number_03_09.config(text=num_27)
	number_04_01.config(text=num_28)
	number_04_02.config(text=num_29)
	number_04_03.config(text=num_30)
	number_05_01.config(text=num_31)
	number_05_02.config(text=num_32)
	number_05_03.config(text=num_33)
	number_06_01.config(text=num_34)
	number_06_02.config(text=num_35)
	number_06_03.config(text=num_36)
	number_04_04.config(text=num_37)
	number_04_05.config(text=num_38)
	number_04_06.config(text=num_39)
	number_05_04.config(text=num_40)
	number_05_05.config(text=num_41)
	number_05_06.config(text=num_42)
	number_06_04.config(text=num_43)
	number_06_05.config(text=num_44)
	number_06_06.config(text=num_45)
	number_04_07.config(text=num_46)
	number_04_08.config(text=num_47)
	number_04_09.config(text=num_48)
	number_05_07.config(text=num_49)
	number_05_08.config(text=num_50)
	number_05_09.config(text=num_51)
	number_06_07.config(text=num_52)
	number_06_08.config(text=num_53)
	number_06_09.config(text=num_54)
	number_07_01.config(text=num_55)
	number_07_02.config(text=num_56)
	number_07_03.config(text=num_57)
	number_08_01.config(text=num_58)
	number_08_02.config(text=num_59)
	number_08_03.config(text=num_60)
	number_09_01.config(text=num_61)
	number_09_02.config(text=num_62)
	number_09_03.config(text=num_63)
	number_07_04.config(text=num_64)
	number_07_05.config(text=num_65)
	number_07_06.config(text=num_66)
	number_08_04.config(text=num_67)
	number_08_05.config(text=num_68)
	number_08_06.config(text=num_69)
	number_09_04.config(text=num_70)
	number_09_05.config(text=num_71)
	number_09_06.config(text=num_72)
	number_07_07.config(text=num_73)
	number_07_08.config(text=num_74)
	number_07_09.config(text=num_75)
	number_08_07.config(text=num_76)
	number_08_08.config(text=num_77)
	number_08_09.config(text=num_78)
	number_09_07.config(text=num_79)
	number_09_08.config(text=num_80)
	number_09_09.config(text=num_81)

	counter = 0
	while counter < 81:
		num_list[counter].config(state=DISABLED)
		counter += 1

	change_list = [
		change_01, change_02, change_03, change_04, change_05, change_06, change_07, change_08, change_09, change_00
	]

	counter = 0
	while counter < 10:
		change_list[counter].config(state=DISABLED)
		counter += 1

def tutorial_game():
	pass

def clear_game():
	clear_num_list = [
		number_01_01, number_01_02, number_01_03, number_01_04, number_01_05, number_01_06, number_01_07, number_01_08, number_01_09,
		number_02_01, number_02_02, number_02_03, number_02_04, number_02_05, number_02_06, number_02_07, number_02_08, number_02_09,
		number_03_01, number_03_02, number_03_03, number_03_04, number_03_05, number_03_06, number_03_07, number_03_08, number_03_09,
		number_04_01, number_04_02, number_04_03, number_04_04, number_04_05, number_04_06, number_04_07, number_04_08, number_04_09,
		number_05_01, number_05_02, number_05_03, number_05_04, number_05_05, number_05_06, number_05_07, number_05_08, number_05_09,
		number_06_01, number_06_02, number_06_03, number_06_04, number_06_05, number_06_06, number_06_07, number_06_08, number_06_09,
		number_07_01, number_07_02, number_07_03, number_07_04, number_07_05, number_07_06, number_07_07, number_07_08, number_07_09,
		number_08_01, number_08_02, number_08_03, number_08_04, number_08_05, number_08_06, number_08_07, number_08_08, number_08_09,
		number_09_01, number_09_02, number_09_03, number_09_04, number_09_05, number_09_06, number_09_07, number_09_08, number_09_09
	]

	clear_counter = 0
	while clear_counter < 81:
		if clear_num_list[clear_counter].cget("state") == NORMAL:
			clear_num_list[clear_counter].config(text="")
			clear_counter += 1
		else:
			clear_counter += 1
			continue

panel = Frame(root)
panel_button_01 = Button(panel, width=9, relief=GROOVE, state=DISABLED)
panel_button_02 = Button(panel, width=9, relief=GROOVE, state=DISABLED)
panel_button_03 = Button(panel, width=9, relief=GROOVE, state=DISABLED)

def hint():
	pass

def gamemode_new():
	panel_button_01.config(text="Play", command=new_game, state=NORMAL)
	panel_button_02.config(text="Clean", command=clear_game, state=NORMAL)
	panel_button_03.config(text="Hint", state=NORMAL, command=hint)
	new_number("")
	num_list = [
		number_01_01, number_01_02, number_01_03, number_01_04, number_01_05, number_01_06, number_01_07, number_01_08, number_01_09,
		number_02_01, number_02_02, number_02_03, number_02_04, number_02_05, number_02_06, number_02_07, number_02_08, number_02_09,
		number_03_01, number_03_02, number_03_03, number_03_04, number_03_05, number_03_06, number_03_07, number_03_08, number_03_09,
		number_04_01, number_04_02, number_04_03, number_04_04, number_04_05, number_04_06, number_04_07, number_04_08, number_04_09,
		number_05_01, number_05_02, number_05_03, number_05_04, number_05_05, number_05_06, number_05_07, number_05_08, number_05_09,
		number_06_01, number_06_02, number_06_03, number_06_04, number_06_05, number_06_06, number_06_07, number_06_08, number_06_09,
		number_07_01, number_07_02, number_07_03, number_07_04, number_07_05, number_07_06, number_07_07, number_07_08, number_07_09,
		number_08_01, number_08_02, number_08_03, number_08_04, number_08_05, number_08_06, number_08_07, number_08_08, number_08_09,
		number_09_01, number_09_02, number_09_03, number_09_04, number_09_05, number_09_06, number_09_07, number_09_08, number_09_09
	]

	counter = 0
	while counter < 81:
		num_list[counter].config(text="", state=DISABLED)
		counter += 1

	change_list = [
		change_01, change_02, change_03, change_04, change_05, change_06, change_07, change_08, change_09, change_00
	]

	counter = 0
	while counter < 10:
		change_list[counter].config(state=DISABLED)
		counter += 1

def gamemode_custom():
	panel_button_01.config(text="Create", command=custom_game, state=NORMAL)
	panel_button_02.config(text="Clean", command=clear_game, state=NORMAL)
	panel_button_03.config(text="Solve", command=solve, state=NORMAL)
	new_number("")
	num_list = [
		number_01_01, number_01_02, number_01_03, number_01_04, number_01_05, number_01_06, number_01_07, number_01_08, number_01_09,
		number_02_01, number_02_02, number_02_03, number_02_04, number_02_05, number_02_06, number_02_07, number_02_08, number_02_09,
		number_03_01, number_03_02, number_03_03, number_03_04, number_03_05, number_03_06, number_03_07, number_03_08, number_03_09,
		number_04_01, number_04_02, number_04_03, number_04_04, number_04_05, number_04_06, number_04_07, number_04_08, number_04_09,
		number_05_01, number_05_02, number_05_03, number_05_04, number_05_05, number_05_06, number_05_07, number_05_08, number_05_09,
		number_06_01, number_06_02, number_06_03, number_06_04, number_06_05, number_06_06, number_06_07, number_06_08, number_06_09,
		number_07_01, number_07_02, number_07_03, number_07_04, number_07_05, number_07_06, number_07_07, number_07_08, number_07_09,
		number_08_01, number_08_02, number_08_03, number_08_04, number_08_05, number_08_06, number_08_07, number_08_08, number_08_09,
		number_09_01, number_09_02, number_09_03, number_09_04, number_09_05, number_09_06, number_09_07, number_09_08, number_09_09
	]

	counter = 0
	while counter < 81:
		num_list[counter].config(text="", state=DISABLED)
		counter += 1

	change_list = [
		change_01, change_02, change_03, change_04, change_05, change_06, change_07, change_08, change_09, change_00
	]

	counter = 0
	while counter < 10:
		change_list[counter].config(state=DISABLED)
		counter += 1

def gamemode_tutorial():
	pass

menu_bar = Menu(root)
root.config(menu=menu_bar)

game_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Game", menu=game_menu)

mode_menu = Menu(game_menu, tearoff=0)
game_menu.add_cascade(label="Mode", menu=mode_menu)

mode_menu.add_command(label="Play", command=gamemode_new)
mode_menu.add_command(label="Create", command=gamemode_custom)
mode_menu.add_command(label="Tutorial", command=gamemode_tutorial)

game.grid(row=0, column=0, padx=4, pady=4)

frame01.grid(row=0, column=0, padx=2, pady=2)
number_01_01.grid(row=0, column=0, padx=1, pady=1)
number_01_02.grid(row=0, column=1, padx=1, pady=1)
number_01_03.grid(row=0, column=2, padx=1, pady=1)
number_01_04.grid(row=1, column=0, padx=1, pady=1)
number_01_05.grid(row=1, column=1, padx=1, pady=1)
number_01_06.grid(row=1, column=2, padx=1, pady=1)
number_01_07.grid(row=2, column=0, padx=1, pady=1)
number_01_08.grid(row=2, column=1, padx=1, pady=1)
number_01_09.grid(row=2, column=2, padx=1, pady=1)

frame02.grid(row=0, column=1, padx=2, pady=2)
number_02_01.grid(row=0, column=0, padx=1, pady=1)
number_02_02.grid(row=0, column=1, padx=1, pady=1)
number_02_03.grid(row=0, column=2, padx=1, pady=1)
number_02_04.grid(row=1, column=0, padx=1, pady=1)
number_02_05.grid(row=1, column=1, padx=1, pady=1)
number_02_06.grid(row=1, column=2, padx=1, pady=1)
number_02_07.grid(row=2, column=0, padx=1, pady=1)
number_02_08.grid(row=2, column=1, padx=1, pady=1)
number_02_09.grid(row=2, column=2, padx=1, pady=1)

frame03.grid(row=0, column=2, padx=2, pady=2)
number_03_01.grid(row=0, column=0, padx=1, pady=1)
number_03_02.grid(row=0, column=1, padx=1, pady=1)
number_03_03.grid(row=0, column=2, padx=1, pady=1)
number_03_04.grid(row=1, column=0, padx=1, pady=1)
number_03_05.grid(row=1, column=1, padx=1, pady=1)
number_03_06.grid(row=1, column=2, padx=1, pady=1)
number_03_07.grid(row=2, column=0, padx=1, pady=1)
number_03_08.grid(row=2, column=1, padx=1, pady=1)
number_03_09.grid(row=2, column=2, padx=1, pady=1)

frame04.grid(row=1, column=0, padx=2, pady=2)
number_04_01.grid(row=0, column=0, padx=1, pady=1)
number_04_02.grid(row=0, column=1, padx=1, pady=1)
number_04_03.grid(row=0, column=2, padx=1, pady=1)
number_04_04.grid(row=1, column=0, padx=1, pady=1)
number_04_05.grid(row=1, column=1, padx=1, pady=1)
number_04_06.grid(row=1, column=2, padx=1, pady=1)
number_04_07.grid(row=2, column=0, padx=1, pady=1)
number_04_08.grid(row=2, column=1, padx=1, pady=1)
number_04_09.grid(row=2, column=2, padx=1, pady=1)

frame05.grid(row=1, column=1, padx=2, pady=2)
number_05_01.grid(row=0, column=0, padx=1, pady=1)
number_05_02.grid(row=0, column=1, padx=1, pady=1)
number_05_03.grid(row=0, column=2, padx=1, pady=1)
number_05_04.grid(row=1, column=0, padx=1, pady=1)
number_05_05.grid(row=1, column=1, padx=1, pady=1)
number_05_06.grid(row=1, column=2, padx=1, pady=1)
number_05_07.grid(row=2, column=0, padx=1, pady=1)
number_05_08.grid(row=2, column=1, padx=1, pady=1)
number_05_09.grid(row=2, column=2, padx=1, pady=1)

frame06.grid(row=1, column=2, padx=2, pady=2)
number_06_01.grid(row=0, column=0, padx=1, pady=1)
number_06_02.grid(row=0, column=1, padx=1, pady=1)
number_06_03.grid(row=0, column=2, padx=1, pady=1)
number_06_04.grid(row=1, column=0, padx=1, pady=1)
number_06_05.grid(row=1, column=1, padx=1, pady=1)
number_06_06.grid(row=1, column=2, padx=1, pady=1)
number_06_07.grid(row=2, column=0, padx=1, pady=1)
number_06_08.grid(row=2, column=1, padx=1, pady=1)
number_06_09.grid(row=2, column=2, padx=1, pady=1)

frame07.grid(row=2, column=0, padx=2, pady=2)
number_07_01.grid(row=0, column=0, padx=1, pady=1)
number_07_02.grid(row=0, column=1, padx=1, pady=1)
number_07_03.grid(row=0, column=2, padx=1, pady=1)
number_07_04.grid(row=1, column=0, padx=1, pady=1)
number_07_05.grid(row=1, column=1, padx=1, pady=1)
number_07_06.grid(row=1, column=2, padx=1, pady=1)
number_07_07.grid(row=2, column=0, padx=1, pady=1)
number_07_08.grid(row=2, column=1, padx=1, pady=1)
number_07_09.grid(row=2, column=2, padx=1, pady=1)

frame08.grid(row=2, column=1, padx=2, pady=2)
number_08_01.grid(row=0, column=0, padx=1, pady=1)
number_08_02.grid(row=0, column=1, padx=1, pady=1)
number_08_03.grid(row=0, column=2, padx=1, pady=1)
number_08_04.grid(row=1, column=0, padx=1, pady=1)
number_08_05.grid(row=1, column=1, padx=1, pady=1)
number_08_06.grid(row=1, column=2, padx=1, pady=1)
number_08_07.grid(row=2, column=0, padx=1, pady=1)
number_08_08.grid(row=2, column=1, padx=1, pady=1)
number_08_09.grid(row=2, column=2, padx=1, pady=1)

frame09.grid(row=2, column=2, padx=2, pady=2)
number_09_01.grid(row=0, column=0, padx=1, pady=1)
number_09_02.grid(row=0, column=1, padx=1, pady=1)
number_09_03.grid(row=0, column=2, padx=1, pady=1)
number_09_04.grid(row=1, column=0, padx=1, pady=1)
number_09_05.grid(row=1, column=1, padx=1, pady=1)
number_09_06.grid(row=1, column=2, padx=1, pady=1)
number_09_07.grid(row=2, column=0, padx=1, pady=1)
number_09_08.grid(row=2, column=1, padx=1, pady=1)
number_09_09.grid(row=2, column=2, padx=1, pady=1)

number_frame.grid(row=0, column=1, padx=4, pady=4)
number_f01.grid(row=0, column=1, padx=2, pady=2)
number_f02.grid(row=1, column=1, padx=2, pady=2)
number_f03.grid(row=2, column=1, padx=2, pady=2)
change_01.grid(row=0, column=0, padx=1, pady=1)
change_02.grid(row=1, column=0, padx=1, pady=1)
change_03.grid(row=2, column=0, padx=1, pady=1)
change_04.grid(row=0, column=0, padx=1, pady=1)
change_05.grid(row=1, column=0, padx=1, pady=1)
change_06.grid(row=2, column=0, padx=1, pady=1)
change_07.grid(row=0, column=0, padx=1, pady=1)
change_08.grid(row=1, column=0, padx=1, pady=1)
change_09.grid(row=2, column=0, padx=1, pady=1)
change_00.grid(row=1, column=1, padx=1, pady=1)

panel.grid(row=1, column=0, padx=4, pady=4)
panel_button_01.grid(row=0, column=0, padx=4, pady=4)
panel_button_02.grid(row=0, column=1, padx=4, pady=4)
panel_button_03.grid(row=0, column=2, padx=4, pady=4)

root.mainloop()
