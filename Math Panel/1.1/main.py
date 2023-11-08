from tkinter import *
from solver import *

def main():
	window = Tk()
	window.title("Math Panel")
	window.geometry("800x600")

	basic_math = Frame(window, relief=SOLID, bd=1)
	entry_01 = Entry(basic_math, relief=SOLID)
	button_01 = Button(basic_math, text="=", command=lambda:compile(entry_01.get(), label_01), relief=SOLID)
	label_01 = Label(basic_math, text="Here will be your issue", relief=SOLID)

	basic_math.place(x=10, y=10, width=465, height=45)
	entry_01.place(x=10, y=10, width=200, height=25)
	button_01.place(x=220, y=10, width=25, height=25)
	label_01.place(x=255, y=10, width=200, height=25)

	window.mainloop()

if __name__ == '__main__':
	main()