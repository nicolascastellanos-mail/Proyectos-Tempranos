from tkinter import *
from random import choice, randint

def falta_llenar():
	global validar_lleno

	lista_numeros = [
		numero_01_01, numero_01_02, numero_01_03, numero_01_04, numero_01_05, numero_01_06, numero_01_07, numero_01_08, numero_01_09,
		numero_02_01, numero_02_02, numero_02_03, numero_02_04, numero_02_05, numero_02_06, numero_02_07, numero_02_08, numero_02_09,
		numero_03_01, numero_03_02, numero_03_03, numero_03_04, numero_03_05, numero_03_06, numero_03_07, numero_03_08, numero_03_09,
		numero_04_01, numero_04_02, numero_04_03, numero_04_04, numero_04_05, numero_04_06, numero_04_07, numero_04_08, numero_04_09,
		numero_05_01, numero_05_02, numero_05_03, numero_05_04, numero_05_05, numero_05_06, numero_05_07, numero_05_08, numero_05_09,
		numero_06_01, numero_06_02, numero_06_03, numero_06_04, numero_06_05, numero_06_06, numero_06_07, numero_06_08, numero_06_09,
		numero_07_01, numero_07_02, numero_07_03, numero_07_04, numero_07_05, numero_07_06, numero_07_07, numero_07_08, numero_07_09,
		numero_08_01, numero_08_02, numero_08_03, numero_08_04, numero_08_05, numero_08_06, numero_08_07, numero_08_08, numero_08_09,
		numero_09_01, numero_09_02, numero_09_03, numero_09_04, numero_09_05, numero_09_06, numero_09_07, numero_09_08, numero_09_09
	]

	casilla_llena = 0
	contador = 0
	while contador < 81:
		if lista_numeros[contador].cget("text") != "":
			casilla_llena += 1
			contador += 1
		else:
			contador += 1

	if casilla_llena == 81:
		validar_lleno = True
	else:
		validar_lleno = False

def ventana_completado():
	lista_numeros = [
		numero_01_01, numero_01_02, numero_01_03, numero_01_04, numero_01_05, numero_01_06, numero_01_07, numero_01_08, numero_01_09,
		numero_02_01, numero_02_02, numero_02_03, numero_02_04, numero_02_05, numero_02_06, numero_02_07, numero_02_08, numero_02_09,
		numero_03_01, numero_03_02, numero_03_03, numero_03_04, numero_03_05, numero_03_06, numero_03_07, numero_03_08, numero_03_09,
		numero_04_01, numero_04_02, numero_04_03, numero_04_04, numero_04_05, numero_04_06, numero_04_07, numero_04_08, numero_04_09,
		numero_05_01, numero_05_02, numero_05_03, numero_05_04, numero_05_05, numero_05_06, numero_05_07, numero_05_08, numero_05_09,
		numero_06_01, numero_06_02, numero_06_03, numero_06_04, numero_06_05, numero_06_06, numero_06_07, numero_06_08, numero_06_09,
		numero_07_01, numero_07_02, numero_07_03, numero_07_04, numero_07_05, numero_07_06, numero_07_07, numero_07_08, numero_07_09,
		numero_08_01, numero_08_02, numero_08_03, numero_08_04, numero_08_05, numero_08_06, numero_08_07, numero_08_08, numero_08_09,
		numero_09_01, numero_09_02, numero_09_03, numero_09_04, numero_09_05, numero_09_06, numero_09_07, numero_09_08, numero_09_09
	]

	contador = 0
	while contador < 81:
		lista_numeros[contador].config(state=DISABLED)
		contador += 1

	lista_poner = [
		poner_01, poner_02, poner_03, poner_04, poner_05, poner_06, poner_07, poner_08, poner_09, poner_00
	]

	contador = 0
	while contador < 9:
		lista_poner[contador].config(state=DISABLED)
		contador += 1

	ventana_emergente = Tk()
	ventana_emergente.title("Sudoku completo")
	ventana_emergente.resizable(0, 0)
	def destruir():
		ventana_emergente.destroy()
	mensaje = Label(ventana_emergente, text="Felicidades, has completado el sudoku")
	aceptar = Button(ventana_emergente, text="Aceptar", command=destruir)
	mensaje.grid(row=0, column=0, padx=4, pady=4)
	aceptar.grid(row=1, column=1, padx=4, pady=4)
	ventana_emergente.mainloop()

def sudoku_incorrecto():
	ventana_emergente = Tk()
	ventana_emergente.title("Sudoku incorrecto")
	ventana_emergente.resizable(0, 0)
	def destruir():
		ventana_emergente.destroy()
	mensaje = Label(ventana_emergente, text="No has solucionado bien el sudoku >:(")
	aceptar = Button(ventana_emergente, text="Aceptar", command=destruir)
	mensaje.grid(row=0, column=0, padx=4, pady=4)
	aceptar.grid(row=1, column=1, padx=4, pady=4)
	ventana_emergente.mainloop()

def comprobar_correcto():
	lista_numeros = [
		numero_01_01, numero_01_02, numero_01_03, numero_02_01, numero_02_02, numero_02_03, numero_03_01, numero_03_02, numero_03_03,
		numero_01_04, numero_01_05, numero_01_06, numero_02_04, numero_02_05, numero_02_06, numero_03_04, numero_03_05, numero_03_06,
		numero_01_07, numero_01_08, numero_01_09, numero_02_07, numero_02_08, numero_02_09, numero_03_07, numero_03_08, numero_03_09,
		numero_04_01, numero_04_02, numero_04_03, numero_05_01, numero_05_02, numero_05_03, numero_06_01, numero_06_02, numero_06_03,
		numero_04_04, numero_04_05, numero_04_06, numero_05_04, numero_05_05, numero_05_06, numero_06_04, numero_06_05, numero_06_06,
		numero_04_07, numero_04_08, numero_04_09, numero_05_07, numero_05_08, numero_05_09, numero_06_07, numero_06_08, numero_06_09,
		numero_07_01, numero_07_02, numero_07_03, numero_08_01, numero_08_02, numero_08_03, numero_09_01, numero_09_02, numero_09_03,
		numero_07_04, numero_07_05, numero_07_06, numero_08_04, numero_08_05, numero_08_06, numero_09_04, numero_09_05, numero_09_06,
		numero_07_07, numero_07_08, numero_07_09, numero_08_07, numero_08_08, numero_08_09, numero_09_07, numero_09_08, numero_09_09,
	]

	casilla_llena = 0
	contador = 0
	while contador < 81:
		if lista_numeros[contador].cget("text") == solucion[contador]:
			contador += 1
			casilla_llena += 1
		else:
			break

	if casilla_llena == 81:
		ventana_completado()
	else:
		sudoku_incorrecto()

def nuevo_numero(new):
	global change_numero
	change_numero = new

def numero_change():
	return change_numero

def editar_01_01():
	numero_01_01.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_01_02():
	numero_01_02.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_01_03():
	numero_01_03.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_01_04():
	numero_01_04.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_01_05():
	numero_01_05.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_01_06():
	numero_01_06.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_01_07():
	numero_01_07.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_01_08():
	numero_01_08.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_01_09():
	numero_01_09.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_02_01():
	numero_02_01.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_02_02():
	numero_02_02.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_02_03():
	numero_02_03.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_02_04():
	numero_02_04.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_02_05():
	numero_02_05.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_02_06():
	numero_02_06.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_02_07():
	numero_02_07.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_02_08():
	numero_02_08.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_02_09():
	numero_02_09.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_03_01():
	numero_03_01.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_03_02():
	numero_03_02.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_03_03():
	numero_03_03.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_03_04():
	numero_03_04.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_03_05():
	numero_03_05.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_03_06():
	numero_03_06.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_03_07():
	numero_03_07.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_03_08():
	numero_03_08.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_03_09():
	numero_03_09.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_04_01():
	numero_04_01.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_04_02():
	numero_04_02.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_04_03():
	numero_04_03.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_04_04():
	numero_04_04.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_04_05():
	numero_04_05.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_04_06():
	numero_04_06.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_04_07():
	numero_04_07.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_04_08():
	numero_04_08.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_04_09():
	numero_04_09.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_05_01():
	numero_05_01.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_05_02():
	numero_05_02.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_05_03():
	numero_05_03.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_05_04():
	numero_05_04.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_05_05():
	numero_05_05.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_05_06():
	numero_05_06.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_05_07():
	numero_05_07.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_05_08():
	numero_05_08.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_05_09():
	numero_05_09.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_06_01():
	numero_06_01.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_06_02():
	numero_06_02.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_06_03():
	numero_06_03.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_06_04():
	numero_06_04.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_06_05():
	numero_06_05.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_06_06():
	numero_06_06.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_06_07():
	numero_06_07.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_06_08():
	numero_06_08.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_06_09():
	numero_06_09.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_07_01():
	numero_07_01.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_07_02():
	numero_07_02.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_07_03():
	numero_07_03.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_07_04():
	numero_07_04.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_07_05():
	numero_07_05.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_07_06():
	numero_07_06.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_07_07():
	numero_07_07.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_07_08():
	numero_07_08.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_07_09():
	numero_07_09.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_08_01():
	numero_08_01.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_08_02():
	numero_08_02.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_08_03():
	numero_08_03.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_08_04():
	numero_08_04.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_08_05():
	numero_08_05.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_08_06():
	numero_08_06.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_08_07():
	numero_08_07.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_08_08():
	numero_08_08.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_08_09():
	numero_08_09.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_09_01():
	numero_09_01.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_09_02():
	numero_09_02.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_09_03():
	numero_09_03.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_09_04():
	numero_09_04.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_09_05():
	numero_09_05.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_09_06():
	numero_09_06.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_09_07():
	numero_09_07.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_09_08():
	numero_09_08.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def editar_09_09():
	numero_09_09.config(text=numero_change())
	falta_llenar()
	if validar_lleno == True:
		comprobar_correcto()
	else:
		pass

def aplicar_01():
	nuevo_numero("1")

def aplicar_02():
	nuevo_numero("2")

def aplicar_03():
	nuevo_numero("3")

def aplicar_04():
	nuevo_numero("4")

def aplicar_05():
	nuevo_numero("5")

def aplicar_06():
	nuevo_numero("6")

def aplicar_07():
	nuevo_numero("7")

def aplicar_08():
	nuevo_numero("8")

def aplicar_09():
	nuevo_numero("9")

def aplicar_00():
	nuevo_numero("")

ventana_raiz = Tk()
ventana_raiz.title("Sudoku")
ventana_raiz.resizable(0, 0)

tablero = Frame(ventana_raiz)

cuadro_01 = Frame(tablero)
numero_01_01 = Button(cuadro_01, width=2, height=1, state=DISABLED, command=editar_01_01, relief=GROOVE)
numero_01_02 = Button(cuadro_01, width=2, height=1, state=DISABLED, command=editar_01_02, relief=GROOVE)
numero_01_03 = Button(cuadro_01, width=2, height=1, state=DISABLED, command=editar_01_03, relief=GROOVE)
numero_01_04 = Button(cuadro_01, width=2, height=1, state=DISABLED, command=editar_01_04, relief=GROOVE)
numero_01_05 = Button(cuadro_01, width=2, height=1, state=DISABLED, command=editar_01_05, relief=GROOVE)
numero_01_06 = Button(cuadro_01, width=2, height=1, state=DISABLED, command=editar_01_06, relief=GROOVE)
numero_01_07 = Button(cuadro_01, width=2, height=1, state=DISABLED, command=editar_01_07, relief=GROOVE)
numero_01_08 = Button(cuadro_01, width=2, height=1, state=DISABLED, command=editar_01_08, relief=GROOVE)
numero_01_09 = Button(cuadro_01, width=2, height=1, state=DISABLED, command=editar_01_09, relief=GROOVE)

cuadro_02 = Frame(tablero)
numero_02_01 = Button(cuadro_02, width=2, height=1, state=DISABLED, command=editar_02_01, relief=GROOVE)
numero_02_02 = Button(cuadro_02, width=2, height=1, state=DISABLED, command=editar_02_02, relief=GROOVE)
numero_02_03 = Button(cuadro_02, width=2, height=1, state=DISABLED, command=editar_02_03, relief=GROOVE)
numero_02_04 = Button(cuadro_02, width=2, height=1, state=DISABLED, command=editar_02_04, relief=GROOVE)
numero_02_05 = Button(cuadro_02, width=2, height=1, state=DISABLED, command=editar_02_05, relief=GROOVE)
numero_02_06 = Button(cuadro_02, width=2, height=1, state=DISABLED, command=editar_02_06, relief=GROOVE)
numero_02_07 = Button(cuadro_02, width=2, height=1, state=DISABLED, command=editar_02_07, relief=GROOVE)
numero_02_08 = Button(cuadro_02, width=2, height=1, state=DISABLED, command=editar_02_08, relief=GROOVE)
numero_02_09 = Button(cuadro_02, width=2, height=1, state=DISABLED, command=editar_02_09, relief=GROOVE)

cuadro_03 = Frame(tablero)
numero_03_01 = Button(cuadro_03, width=2, height=1, state=DISABLED, command=editar_03_01, relief=GROOVE)
numero_03_02 = Button(cuadro_03, width=2, height=1, state=DISABLED, command=editar_03_02, relief=GROOVE)
numero_03_03 = Button(cuadro_03, width=2, height=1, state=DISABLED, command=editar_03_03, relief=GROOVE)
numero_03_04 = Button(cuadro_03, width=2, height=1, state=DISABLED, command=editar_03_04, relief=GROOVE)
numero_03_05 = Button(cuadro_03, width=2, height=1, state=DISABLED, command=editar_03_05, relief=GROOVE)
numero_03_06 = Button(cuadro_03, width=2, height=1, state=DISABLED, command=editar_03_06, relief=GROOVE)
numero_03_07 = Button(cuadro_03, width=2, height=1, state=DISABLED, command=editar_03_07, relief=GROOVE)
numero_03_08 = Button(cuadro_03, width=2, height=1, state=DISABLED, command=editar_03_08, relief=GROOVE)
numero_03_09 = Button(cuadro_03, width=2, height=1, state=DISABLED, command=editar_03_09, relief=GROOVE)

cuadro_04 = Frame(tablero)
numero_04_01 = Button(cuadro_04, width=2, height=1, state=DISABLED, command=editar_04_01, relief=GROOVE)
numero_04_02 = Button(cuadro_04, width=2, height=1, state=DISABLED, command=editar_04_02, relief=GROOVE)
numero_04_03 = Button(cuadro_04, width=2, height=1, state=DISABLED, command=editar_04_03, relief=GROOVE)
numero_04_04 = Button(cuadro_04, width=2, height=1, state=DISABLED, command=editar_04_04, relief=GROOVE)
numero_04_05 = Button(cuadro_04, width=2, height=1, state=DISABLED, command=editar_04_05, relief=GROOVE)
numero_04_06 = Button(cuadro_04, width=2, height=1, state=DISABLED, command=editar_04_06, relief=GROOVE)
numero_04_07 = Button(cuadro_04, width=2, height=1, state=DISABLED, command=editar_04_07, relief=GROOVE)
numero_04_08 = Button(cuadro_04, width=2, height=1, state=DISABLED, command=editar_04_08, relief=GROOVE)
numero_04_09 = Button(cuadro_04, width=2, height=1, state=DISABLED, command=editar_04_09, relief=GROOVE)

cuadro_05 = Frame(tablero)
numero_05_01 = Button(cuadro_05, width=2, height=1, state=DISABLED, command=editar_05_01, relief=GROOVE)
numero_05_02 = Button(cuadro_05, width=2, height=1, state=DISABLED, command=editar_05_02, relief=GROOVE)
numero_05_03 = Button(cuadro_05, width=2, height=1, state=DISABLED, command=editar_05_03, relief=GROOVE)
numero_05_04 = Button(cuadro_05, width=2, height=1, state=DISABLED, command=editar_05_04, relief=GROOVE)
numero_05_05 = Button(cuadro_05, width=2, height=1, state=DISABLED, command=editar_05_05, relief=GROOVE)
numero_05_06 = Button(cuadro_05, width=2, height=1, state=DISABLED, command=editar_05_06, relief=GROOVE)
numero_05_07 = Button(cuadro_05, width=2, height=1, state=DISABLED, command=editar_05_07, relief=GROOVE)
numero_05_08 = Button(cuadro_05, width=2, height=1, state=DISABLED, command=editar_05_08, relief=GROOVE)
numero_05_09 = Button(cuadro_05, width=2, height=1, state=DISABLED, command=editar_05_09, relief=GROOVE)

cuadro_06 = Frame(tablero)
numero_06_01 = Button(cuadro_06, width=2, height=1, state=DISABLED, command=editar_06_01, relief=GROOVE)
numero_06_02 = Button(cuadro_06, width=2, height=1, state=DISABLED, command=editar_06_02, relief=GROOVE)
numero_06_03 = Button(cuadro_06, width=2, height=1, state=DISABLED, command=editar_06_03, relief=GROOVE)
numero_06_04 = Button(cuadro_06, width=2, height=1, state=DISABLED, command=editar_06_04, relief=GROOVE)
numero_06_05 = Button(cuadro_06, width=2, height=1, state=DISABLED, command=editar_06_05, relief=GROOVE)
numero_06_06 = Button(cuadro_06, width=2, height=1, state=DISABLED, command=editar_06_06, relief=GROOVE)
numero_06_07 = Button(cuadro_06, width=2, height=1, state=DISABLED, command=editar_06_07, relief=GROOVE)
numero_06_08 = Button(cuadro_06, width=2, height=1, state=DISABLED, command=editar_06_08, relief=GROOVE)
numero_06_09 = Button(cuadro_06, width=2, height=1, state=DISABLED, command=editar_06_09, relief=GROOVE)

cuadro_07 = Frame(tablero)
numero_07_01 = Button(cuadro_07, width=2, height=1, state=DISABLED, command=editar_07_01, relief=GROOVE)
numero_07_02 = Button(cuadro_07, width=2, height=1, state=DISABLED, command=editar_07_02, relief=GROOVE)
numero_07_03 = Button(cuadro_07, width=2, height=1, state=DISABLED, command=editar_07_03, relief=GROOVE)
numero_07_04 = Button(cuadro_07, width=2, height=1, state=DISABLED, command=editar_07_04, relief=GROOVE)
numero_07_05 = Button(cuadro_07, width=2, height=1, state=DISABLED, command=editar_07_05, relief=GROOVE)
numero_07_06 = Button(cuadro_07, width=2, height=1, state=DISABLED, command=editar_07_06, relief=GROOVE)
numero_07_07 = Button(cuadro_07, width=2, height=1, state=DISABLED, command=editar_07_07, relief=GROOVE)
numero_07_08 = Button(cuadro_07, width=2, height=1, state=DISABLED, command=editar_07_08, relief=GROOVE)
numero_07_09 = Button(cuadro_07, width=2, height=1, state=DISABLED, command=editar_07_09, relief=GROOVE)

cuadro_08 = Frame(tablero)
numero_08_01 = Button(cuadro_08, width=2, height=1, state=DISABLED, command=editar_08_01, relief=GROOVE)
numero_08_02 = Button(cuadro_08, width=2, height=1, state=DISABLED, command=editar_08_02, relief=GROOVE)
numero_08_03 = Button(cuadro_08, width=2, height=1, state=DISABLED, command=editar_08_03, relief=GROOVE)
numero_08_04 = Button(cuadro_08, width=2, height=1, state=DISABLED, command=editar_08_04, relief=GROOVE)
numero_08_05 = Button(cuadro_08, width=2, height=1, state=DISABLED, command=editar_08_05, relief=GROOVE)
numero_08_06 = Button(cuadro_08, width=2, height=1, state=DISABLED, command=editar_08_06, relief=GROOVE)
numero_08_07 = Button(cuadro_08, width=2, height=1, state=DISABLED, command=editar_08_07, relief=GROOVE)
numero_08_08 = Button(cuadro_08, width=2, height=1, state=DISABLED, command=editar_08_08, relief=GROOVE)
numero_08_09 = Button(cuadro_08, width=2, height=1, state=DISABLED, command=editar_08_09, relief=GROOVE)

cuadro_09 = Frame(tablero)
numero_09_01 = Button(cuadro_09, width=2, height=1, state=DISABLED, command=editar_09_01, relief=GROOVE)
numero_09_02 = Button(cuadro_09, width=2, height=1, state=DISABLED, command=editar_09_02, relief=GROOVE)
numero_09_03 = Button(cuadro_09, width=2, height=1, state=DISABLED, command=editar_09_03, relief=GROOVE)
numero_09_04 = Button(cuadro_09, width=2, height=1, state=DISABLED, command=editar_09_04, relief=GROOVE)
numero_09_05 = Button(cuadro_09, width=2, height=1, state=DISABLED, command=editar_09_05, relief=GROOVE)
numero_09_06 = Button(cuadro_09, width=2, height=1, state=DISABLED, command=editar_09_06, relief=GROOVE)
numero_09_07 = Button(cuadro_09, width=2, height=1, state=DISABLED, command=editar_09_07, relief=GROOVE)
numero_09_08 = Button(cuadro_09, width=2, height=1, state=DISABLED, command=editar_09_08, relief=GROOVE)
numero_09_09 = Button(cuadro_09, width=2, height=1, state=DISABLED, command=editar_09_09, relief=GROOVE)

cuadro_numeros = Frame(ventana_raiz)
numeros_c01 = Frame(cuadro_numeros)
numeros_c02 = Frame(cuadro_numeros)
numeros_c03 = Frame(cuadro_numeros)
poner_01 = Button(numeros_c01, width=2, height=1, state=DISABLED, text="1", command=aplicar_01, relief=GROOVE)
poner_02 = Button(numeros_c01, width=2, height=1, state=DISABLED, text="2", command=aplicar_02, relief=GROOVE)
poner_03 = Button(numeros_c01, width=2, height=1, state=DISABLED, text="3", command=aplicar_03, relief=GROOVE)
poner_04 = Button(numeros_c02, width=2, height=1, state=DISABLED, text="4", command=aplicar_04, relief=GROOVE)
poner_05 = Button(numeros_c02, width=2, height=1, state=DISABLED, text="5", command=aplicar_05, relief=GROOVE)
poner_06 = Button(numeros_c02, width=2, height=1, state=DISABLED, text="6", command=aplicar_06, relief=GROOVE)
poner_07 = Button(numeros_c03, width=2, height=1, state=DISABLED, text="7", command=aplicar_07, relief=GROOVE)
poner_08 = Button(numeros_c03, width=2, height=1, state=DISABLED, text="8", command=aplicar_08, relief=GROOVE)
poner_09 = Button(numeros_c03, width=2, height=1, state=DISABLED, text="9", command=aplicar_09, relief=GROOVE)
poner_00 = Button(ventana_raiz, width=2, height=1, state=DISABLED, text="", command=aplicar_00, relief=GROOVE)

def comprobar_fila(cuadricula, fila, numero):
	return numero in cuadricula[fila]

def comprobar_columna(cuadricula, columna, numero):
	return numero in (fila[columna] for fila in cuadricula)


def comprobar_caja(cuadricula, fila, columna, numero):
	fila_caja, columna_caja = obtener_caja(fila, columna)
	numeros_caja = desempaquetar(
		fila[columna_caja*3:columna_caja*3 + 3]
		for fila in cuadricula[fila_caja*3:fila_caja*3 + 3]
	)
	return numero in numeros_caja


def reducir(n):
	n /= 3
	if n == 0 or n != int(n):
		n += 1
	return int(n)


def obtener_caja(fila, columna):
	fila += 1
	columna += 1
	return reducir(fila) - 1, reducir(columna) - 1


def desempaquetar(iterable):
	for item in iterable:
		yield from item


def obtener_posibilidades(cuadricula, fila, columna):
	for numero in range(1, 10):
		if (not comprobar_fila(cuadricula, fila, numero) and
			not comprobar_columna(cuadricula, columna, numero) and
			not comprobar_caja(cuadricula, fila, columna, numero)):
			yield numero

def modo_jugar():
	nuevo_numero("")

	lista_numeros = [
		numero_01_01, numero_01_02, numero_01_03, numero_01_04, numero_01_05, numero_01_06, numero_01_07, numero_01_08, numero_01_09,
		numero_02_01, numero_02_02, numero_02_03, numero_02_04, numero_02_05, numero_02_06, numero_02_07, numero_02_08, numero_02_09,
		numero_03_01, numero_03_02, numero_03_03, numero_03_04, numero_03_05, numero_03_06, numero_03_07, numero_03_08, numero_03_09,
		numero_04_01, numero_04_02, numero_04_03, numero_04_04, numero_04_05, numero_04_06, numero_04_07, numero_04_08, numero_04_09,
		numero_05_01, numero_05_02, numero_05_03, numero_05_04, numero_05_05, numero_05_06, numero_05_07, numero_05_08, numero_05_09,
		numero_06_01, numero_06_02, numero_06_03, numero_06_04, numero_06_05, numero_06_06, numero_06_07, numero_06_08, numero_06_09,
		numero_07_01, numero_07_02, numero_07_03, numero_07_04, numero_07_05, numero_07_06, numero_07_07, numero_07_08, numero_07_09,
		numero_08_01, numero_08_02, numero_08_03, numero_08_04, numero_08_05, numero_08_06, numero_08_07, numero_08_08, numero_08_09,
		numero_09_01, numero_09_02, numero_09_03, numero_09_04, numero_09_05, numero_09_06, numero_09_07, numero_09_08, numero_09_09
	]

	contador = 0
	while contador < 81:
		lista_numeros[contador].config(text="", state=DISABLED)
		contador += 1

	while True:
		cuadricula = [
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
			numeros_posibles = {
				(fila, columna): None for fila in range(9) for columna in range(9)
			}
			for fila in range(9):
				for columna in range(9):
					numero = cuadricula[fila][columna]
					if numero == 0:
						opciones = list(
							obtener_posibilidades(cuadricula, fila, columna)
						)
						if opciones:
							numeros_posibles[(fila, columna)] = opciones
			numeros_posibles = sorted(
				(
					(k, v)
					for (k, v) in numeros_posibles.items()
					if v is not None
				),
				key=lambda kv: len(kv[1])
			)
			
			if numeros_posibles:
				(fila, columna), numeros = numeros_posibles[0]
				cuadricula[fila][columna] = choice(numeros)
			else:
				break
		if 0 not in desempaquetar(cuadricula):
			print(s.format(*(desempaquetar(cuadricula))))
			break

	numero_01 = str(cuadricula[0][0])
	numero_02 = str(cuadricula[0][1])
	numero_03 = str(cuadricula[0][2])
	numero_04 = str(cuadricula[0][3])
	numero_05 = str(cuadricula[0][4])
	numero_06 = str(cuadricula[0][5])
	numero_07 = str(cuadricula[0][6])
	numero_08 = str(cuadricula[0][7])
	numero_09 = str(cuadricula[0][8])
	numero_10 = str(cuadricula[1][0])
	numero_11 = str(cuadricula[1][1])
	numero_12 = str(cuadricula[1][2])
	numero_13 = str(cuadricula[1][3])
	numero_14 = str(cuadricula[1][4])
	numero_15 = str(cuadricula[1][5])
	numero_16 = str(cuadricula[1][6])
	numero_17 = str(cuadricula[1][7])
	numero_18 = str(cuadricula[1][8])
	numero_19 = str(cuadricula[2][0])
	numero_20 = str(cuadricula[2][1])
	numero_21 = str(cuadricula[2][2])
	numero_22 = str(cuadricula[2][3])
	numero_23 = str(cuadricula[2][4])
	numero_24 = str(cuadricula[2][5])
	numero_25 = str(cuadricula[2][6])
	numero_26 = str(cuadricula[2][7])
	numero_27 = str(cuadricula[2][8])
	numero_28 = str(cuadricula[3][0])
	numero_29 = str(cuadricula[3][1])
	numero_30 = str(cuadricula[3][2])
	numero_31 = str(cuadricula[3][3])
	numero_32 = str(cuadricula[3][4])
	numero_33 = str(cuadricula[3][5])
	numero_34 = str(cuadricula[3][6])
	numero_35 = str(cuadricula[3][7])
	numero_36 = str(cuadricula[3][8])
	numero_37 = str(cuadricula[4][0])
	numero_38 = str(cuadricula[4][1])
	numero_39 = str(cuadricula[4][2])
	numero_40 = str(cuadricula[4][3])
	numero_41 = str(cuadricula[4][4])
	numero_42 = str(cuadricula[4][5])
	numero_43 = str(cuadricula[4][6])
	numero_44 = str(cuadricula[4][7])
	numero_45 = str(cuadricula[4][8])
	numero_46 = str(cuadricula[5][0])
	numero_47 = str(cuadricula[5][1])
	numero_48 = str(cuadricula[5][2])
	numero_49 = str(cuadricula[5][3])
	numero_50 = str(cuadricula[5][4])
	numero_51 = str(cuadricula[5][5])
	numero_52 = str(cuadricula[5][6])
	numero_53 = str(cuadricula[5][7])
	numero_54 = str(cuadricula[5][8])
	numero_55 = str(cuadricula[6][0])
	numero_56 = str(cuadricula[6][1])
	numero_57 = str(cuadricula[6][2])
	numero_58 = str(cuadricula[6][3])
	numero_59 = str(cuadricula[6][4])
	numero_60 = str(cuadricula[6][5])
	numero_61 = str(cuadricula[6][6])
	numero_62 = str(cuadricula[6][7])
	numero_63 = str(cuadricula[6][8])
	numero_64 = str(cuadricula[7][0])
	numero_65 = str(cuadricula[7][1])
	numero_66 = str(cuadricula[7][2])
	numero_67 = str(cuadricula[7][3])
	numero_68 = str(cuadricula[7][4])
	numero_69 = str(cuadricula[7][5])
	numero_70 = str(cuadricula[7][6])
	numero_71 = str(cuadricula[7][7])
	numero_72 = str(cuadricula[7][8])
	numero_73 = str(cuadricula[8][0])
	numero_74 = str(cuadricula[8][1])
	numero_75 = str(cuadricula[8][2])
	numero_76 = str(cuadricula[8][3])
	numero_77 = str(cuadricula[8][4])
	numero_78 = str(cuadricula[8][5])
	numero_79 = str(cuadricula[8][6])
	numero_80 = str(cuadricula[8][7])
	numero_81 = str(cuadricula[8][8])

	global solucion
	solucion = [
		numero_01, numero_02, numero_03, numero_04, numero_05, numero_06, numero_07, numero_08, numero_09,
		numero_10, numero_11, numero_12, numero_13, numero_14, numero_15, numero_16, numero_17, numero_18,
		numero_19, numero_20, numero_21, numero_22, numero_23, numero_24, numero_25, numero_26, numero_27,
		numero_28, numero_29, numero_30, numero_31, numero_32, numero_33, numero_34, numero_35, numero_36,
		numero_37, numero_38, numero_39, numero_40, numero_41, numero_42, numero_43, numero_44, numero_45,
		numero_46, numero_47, numero_48, numero_49, numero_50, numero_51, numero_52, numero_53, numero_54,
		numero_55, numero_56, numero_57, numero_58, numero_59, numero_60, numero_61, numero_62, numero_63,
		numero_64, numero_65, numero_66, numero_67, numero_68, numero_69, numero_70, numero_71, numero_72,
		numero_73, numero_74, numero_75, numero_76, numero_77, numero_78, numero_79, numero_80, numero_81
	]

	numero_01_01.config(text=numero_01)
	numero_01_02.config(text=numero_02)
	numero_01_03.config(text=numero_03)
	numero_02_01.config(text=numero_04)
	numero_02_02.config(text=numero_05)
	numero_02_03.config(text=numero_06)
	numero_03_01.config(text=numero_07)
	numero_03_02.config(text=numero_08)
	numero_03_03.config(text=numero_09)
	numero_01_04.config(text=numero_10)
	numero_01_05.config(text=numero_11)
	numero_01_06.config(text=numero_12)
	numero_02_04.config(text=numero_13)
	numero_02_05.config(text=numero_14)
	numero_02_06.config(text=numero_15)
	numero_03_04.config(text=numero_16)
	numero_03_05.config(text=numero_17)
	numero_03_06.config(text=numero_18)
	numero_01_07.config(text=numero_19)
	numero_01_08.config(text=numero_20)
	numero_01_09.config(text=numero_21)
	numero_02_07.config(text=numero_22)
	numero_02_08.config(text=numero_23)
	numero_02_09.config(text=numero_24)
	numero_03_07.config(text=numero_25)
	numero_03_08.config(text=numero_26)
	numero_03_09.config(text=numero_27)
	numero_04_01.config(text=numero_28)
	numero_04_02.config(text=numero_29)
	numero_04_03.config(text=numero_30)
	numero_05_01.config(text=numero_31)
	numero_05_02.config(text=numero_32)
	numero_05_03.config(text=numero_33)
	numero_06_01.config(text=numero_34)
	numero_06_02.config(text=numero_35)
	numero_06_03.config(text=numero_36)
	numero_04_04.config(text=numero_37)
	numero_04_05.config(text=numero_38)
	numero_04_06.config(text=numero_39)
	numero_05_04.config(text=numero_40)
	numero_05_05.config(text=numero_41)
	numero_05_06.config(text=numero_42)
	numero_06_04.config(text=numero_43)
	numero_06_05.config(text=numero_44)
	numero_06_06.config(text=numero_45)
	numero_04_07.config(text=numero_46)
	numero_04_08.config(text=numero_47)
	numero_04_09.config(text=numero_48)
	numero_05_07.config(text=numero_49)
	numero_05_08.config(text=numero_50)
	numero_05_09.config(text=numero_51)
	numero_06_07.config(text=numero_52)
	numero_06_08.config(text=numero_53)
	numero_06_09.config(text=numero_54)
	numero_07_01.config(text=numero_55)
	numero_07_02.config(text=numero_56)
	numero_07_03.config(text=numero_57)
	numero_08_01.config(text=numero_58)
	numero_08_02.config(text=numero_59)
	numero_08_03.config(text=numero_60)
	numero_09_01.config(text=numero_61)
	numero_09_02.config(text=numero_62)
	numero_09_03.config(text=numero_63)
	numero_07_04.config(text=numero_64)
	numero_07_05.config(text=numero_65)
	numero_07_06.config(text=numero_66)
	numero_08_04.config(text=numero_67)
	numero_08_05.config(text=numero_68)
	numero_08_06.config(text=numero_69)
	numero_09_04.config(text=numero_70)
	numero_09_05.config(text=numero_71)
	numero_09_06.config(text=numero_72)
	numero_07_07.config(text=numero_73)
	numero_07_08.config(text=numero_74)
	numero_07_09.config(text=numero_75)
	numero_08_07.config(text=numero_76)
	numero_08_08.config(text=numero_77)
	numero_08_09.config(text=numero_78)
	numero_09_07.config(text=numero_79)
	numero_09_08.config(text=numero_80)
	numero_09_09.config(text=numero_81)

	lista_numeros = [
		numero_01_01, numero_01_02, numero_01_03, numero_01_04, numero_01_05, numero_01_06, numero_01_07, numero_01_08, numero_01_09,
		numero_02_01, numero_02_02, numero_02_03, numero_02_04, numero_02_05, numero_02_06, numero_02_07, numero_02_08, numero_02_09,
		numero_03_01, numero_03_02, numero_03_03, numero_03_04, numero_03_05, numero_03_06, numero_03_07, numero_03_08, numero_03_09,
		numero_04_01, numero_04_02, numero_04_03, numero_04_04, numero_04_05, numero_04_06, numero_04_07, numero_04_08, numero_04_09,
		numero_05_01, numero_05_02, numero_05_03, numero_05_04, numero_05_05, numero_05_06, numero_05_07, numero_05_08, numero_05_09,
		numero_06_01, numero_06_02, numero_06_03, numero_06_04, numero_06_05, numero_06_06, numero_06_07, numero_06_08, numero_06_09,
		numero_07_01, numero_07_02, numero_07_03, numero_07_04, numero_07_05, numero_07_06, numero_07_07, numero_07_08, numero_07_09,
		numero_08_01, numero_08_02, numero_08_03, numero_08_04, numero_08_05, numero_08_06, numero_08_07, numero_08_08, numero_08_09,
		numero_09_01, numero_09_02, numero_09_03, numero_09_04, numero_09_05, numero_09_06, numero_09_07, numero_09_08, numero_09_09
	]

	numero_espacios = randint(49, 54)

	contador = 0
	while contador < numero_espacios:
		numero_eliminar = choice(lista_numeros)
		if numero_eliminar.cget("text") != "":
			numero_eliminar.config(state=NORMAL, text="")
			contador += 1
		else:
			continue

	poner_01.config(state=NORMAL)
	poner_02.config(state=NORMAL)
	poner_03.config(state=NORMAL)
	poner_04.config(state=NORMAL)
	poner_05.config(state=NORMAL)
	poner_06.config(state=NORMAL)
	poner_07.config(state=NORMAL)
	poner_08.config(state=NORMAL)
	poner_09.config(state=NORMAL)
	poner_00.config(state=NORMAL)

def advertencia():
	ventana_advertencia = Tk()
	ventana_advertencia.title("Advertencia")
	ventana_advertencia.resizable(0, 0)
	def destruir():
		ventana_advertencia.destroy()
	mensaje = Label(ventana_advertencia, text="NO proponga un ejercicio sin solución.\nPodría causar que su computadora se congele...")
	aceptar = Button(ventana_advertencia, text="Aceptar", command=destruir)
	mensaje.grid(row=0, column=0, padx=4, pady=4)
	aceptar.grid(row=1, column=1, padx=4, pady=4)
	ventana_advertencia.mainloop()

def crear_juego():
	nuevo_numero("")
	lista_numeros = [
		numero_01_01, numero_01_02, numero_01_03, numero_01_04, numero_01_05, numero_01_06, numero_01_07, numero_01_08, numero_01_09,
		numero_02_01, numero_02_02, numero_02_03, numero_02_04, numero_02_05, numero_02_06, numero_02_07, numero_02_08, numero_02_09,
		numero_03_01, numero_03_02, numero_03_03, numero_03_04, numero_03_05, numero_03_06, numero_03_07, numero_03_08, numero_03_09,
		numero_04_01, numero_04_02, numero_04_03, numero_04_04, numero_04_05, numero_04_06, numero_04_07, numero_04_08, numero_04_09,
		numero_05_01, numero_05_02, numero_05_03, numero_05_04, numero_05_05, numero_05_06, numero_05_07, numero_05_08, numero_05_09,
		numero_06_01, numero_06_02, numero_06_03, numero_06_04, numero_06_05, numero_06_06, numero_06_07, numero_06_08, numero_06_09,
		numero_07_01, numero_07_02, numero_07_03, numero_07_04, numero_07_05, numero_07_06, numero_07_07, numero_07_08, numero_07_09,
		numero_08_01, numero_08_02, numero_08_03, numero_08_04, numero_08_05, numero_08_06, numero_08_07, numero_08_08, numero_08_09,
		numero_09_01, numero_09_02, numero_09_03, numero_09_04, numero_09_05, numero_09_06, numero_09_07, numero_09_08, numero_09_09
	]

	contador = 0
	while contador < 81:
		lista_numeros[contador].config(text="", state=NORMAL)
		contador += 1

	lista_poner = [
		poner_01, poner_02, poner_03, poner_04, poner_05, poner_06, poner_07, poner_08, poner_09, poner_00
	]

	contador = 0
	while contador < 10:
		lista_poner[contador].config(state=NORMAL)
		contador += 1

	advertencia()

def solucionar():
	lista_numeros = [
		numero_01_01, numero_01_02, numero_01_03, numero_01_04, numero_01_05, numero_01_06, numero_01_07, numero_01_08, numero_01_09,
		numero_02_01, numero_02_02, numero_02_03, numero_02_04, numero_02_05, numero_02_06, numero_02_07, numero_02_08, numero_02_09,
		numero_03_01, numero_03_02, numero_03_03, numero_03_04, numero_03_05, numero_03_06, numero_03_07, numero_03_08, numero_03_09,
		numero_04_01, numero_04_02, numero_04_03, numero_04_04, numero_04_05, numero_04_06, numero_04_07, numero_04_08, numero_04_09,
		numero_05_01, numero_05_02, numero_05_03, numero_05_04, numero_05_05, numero_05_06, numero_05_07, numero_05_08, numero_05_09,
		numero_06_01, numero_06_02, numero_06_03, numero_06_04, numero_06_05, numero_06_06, numero_06_07, numero_06_08, numero_06_09,
		numero_07_01, numero_07_02, numero_07_03, numero_07_04, numero_07_05, numero_07_06, numero_07_07, numero_07_08, numero_07_09,
		numero_08_01, numero_08_02, numero_08_03, numero_08_04, numero_08_05, numero_08_06, numero_08_07, numero_08_08, numero_08_09,
		numero_09_01, numero_09_02, numero_09_03, numero_09_04, numero_09_05, numero_09_06, numero_09_07, numero_09_08, numero_09_09
	]

	contador = 0
	while contador < 81:
		if lista_numeros[contador].cget("text") == "":
			lista_numeros[contador].config(text="0")
		else:
			pass

		contador += 1

	while True:
		cuadricula = [
			[int(numero_01_01.cget("text")), int(numero_01_02.cget("text")), int(numero_01_03.cget("text")), int(numero_02_01.cget("text")), int(numero_02_02.cget("text")), int(numero_02_03.cget("text")), int(numero_03_01.cget("text")), int(numero_03_02.cget("text")), int(numero_03_03.cget("text"))],
			[int(numero_01_04.cget("text")), int(numero_01_05.cget("text")), int(numero_01_06.cget("text")), int(numero_02_04.cget("text")), int(numero_02_05.cget("text")), int(numero_02_06.cget("text")), int(numero_03_04.cget("text")), int(numero_03_05.cget("text")), int(numero_03_06.cget("text"))],
			[int(numero_01_07.cget("text")), int(numero_01_08.cget("text")), int(numero_01_09.cget("text")), int(numero_02_07.cget("text")), int(numero_02_08.cget("text")), int(numero_02_09.cget("text")), int(numero_03_07.cget("text")), int(numero_03_08.cget("text")), int(numero_03_09.cget("text"))],
			[int(numero_04_01.cget("text")), int(numero_04_02.cget("text")), int(numero_04_03.cget("text")), int(numero_05_01.cget("text")), int(numero_05_02.cget("text")), int(numero_05_03.cget("text")), int(numero_06_01.cget("text")), int(numero_06_02.cget("text")), int(numero_06_03.cget("text"))],
			[int(numero_04_04.cget("text")), int(numero_04_05.cget("text")), int(numero_04_06.cget("text")), int(numero_05_04.cget("text")), int(numero_05_05.cget("text")), int(numero_05_06.cget("text")), int(numero_06_04.cget("text")), int(numero_06_05.cget("text")), int(numero_06_06.cget("text"))],
			[int(numero_04_07.cget("text")), int(numero_04_08.cget("text")), int(numero_04_09.cget("text")), int(numero_05_07.cget("text")), int(numero_05_08.cget("text")), int(numero_05_09.cget("text")), int(numero_06_07.cget("text")), int(numero_06_08.cget("text")), int(numero_06_09.cget("text"))],
			[int(numero_07_01.cget("text")), int(numero_07_02.cget("text")), int(numero_07_03.cget("text")), int(numero_08_01.cget("text")), int(numero_08_02.cget("text")), int(numero_08_03.cget("text")), int(numero_09_01.cget("text")), int(numero_09_02.cget("text")), int(numero_09_03.cget("text"))],
			[int(numero_07_04.cget("text")), int(numero_07_05.cget("text")), int(numero_07_06.cget("text")), int(numero_08_04.cget("text")), int(numero_08_05.cget("text")), int(numero_08_06.cget("text")), int(numero_09_04.cget("text")), int(numero_09_05.cget("text")), int(numero_09_06.cget("text"))],
			[int(numero_07_07.cget("text")), int(numero_07_08.cget("text")), int(numero_07_09.cget("text")), int(numero_08_07.cget("text")), int(numero_08_08.cget("text")), int(numero_08_09.cget("text")), int(numero_09_07.cget("text")), int(numero_09_08.cget("text")), int(numero_09_09.cget("text"))]
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
			numeros_posibles = {
				(fila, columna): None for fila in range(9) for columna in range(9)
			}
			for fila in range(9):
				for columna in range(9):
					numero = cuadricula[fila][columna]
					if numero == 0:
						opciones = list(
							obtener_posibilidades(cuadricula, fila, columna)
						)
						if opciones:
							numeros_posibles[(fila, columna)] = opciones
			numeros_posibles = sorted(
				(
					(k, v)
					for (k, v) in numeros_posibles.items()
					if v is not None
				),
				key=lambda kv: len(kv[1])
			)
			
			if numeros_posibles:
				(fila, columna), numeros = numeros_posibles[0]
				cuadricula[fila][columna] = choice(numeros)
			else:
				break
		if 0 not in desempaquetar(cuadricula):
			print(s.format(*(desempaquetar(cuadricula))))
			break

	numero_01 = str(cuadricula[0][0])
	numero_02 = str(cuadricula[0][1])
	numero_03 = str(cuadricula[0][2])
	numero_04 = str(cuadricula[0][3])
	numero_05 = str(cuadricula[0][4])
	numero_06 = str(cuadricula[0][5])
	numero_07 = str(cuadricula[0][6])
	numero_08 = str(cuadricula[0][7])
	numero_09 = str(cuadricula[0][8])
	numero_10 = str(cuadricula[1][0])
	numero_11 = str(cuadricula[1][1])
	numero_12 = str(cuadricula[1][2])
	numero_13 = str(cuadricula[1][3])
	numero_14 = str(cuadricula[1][4])
	numero_15 = str(cuadricula[1][5])
	numero_16 = str(cuadricula[1][6])
	numero_17 = str(cuadricula[1][7])
	numero_18 = str(cuadricula[1][8])
	numero_19 = str(cuadricula[2][0])
	numero_20 = str(cuadricula[2][1])
	numero_21 = str(cuadricula[2][2])
	numero_22 = str(cuadricula[2][3])
	numero_23 = str(cuadricula[2][4])
	numero_24 = str(cuadricula[2][5])
	numero_25 = str(cuadricula[2][6])
	numero_26 = str(cuadricula[2][7])
	numero_27 = str(cuadricula[2][8])
	numero_28 = str(cuadricula[3][0])
	numero_29 = str(cuadricula[3][1])
	numero_30 = str(cuadricula[3][2])
	numero_31 = str(cuadricula[3][3])
	numero_32 = str(cuadricula[3][4])
	numero_33 = str(cuadricula[3][5])
	numero_34 = str(cuadricula[3][6])
	numero_35 = str(cuadricula[3][7])
	numero_36 = str(cuadricula[3][8])
	numero_37 = str(cuadricula[4][0])
	numero_38 = str(cuadricula[4][1])
	numero_39 = str(cuadricula[4][2])
	numero_40 = str(cuadricula[4][3])
	numero_41 = str(cuadricula[4][4])
	numero_42 = str(cuadricula[4][5])
	numero_43 = str(cuadricula[4][6])
	numero_44 = str(cuadricula[4][7])
	numero_45 = str(cuadricula[4][8])
	numero_46 = str(cuadricula[5][0])
	numero_47 = str(cuadricula[5][1])
	numero_48 = str(cuadricula[5][2])
	numero_49 = str(cuadricula[5][3])
	numero_50 = str(cuadricula[5][4])
	numero_51 = str(cuadricula[5][5])
	numero_52 = str(cuadricula[5][6])
	numero_53 = str(cuadricula[5][7])
	numero_54 = str(cuadricula[5][8])
	numero_55 = str(cuadricula[6][0])
	numero_56 = str(cuadricula[6][1])
	numero_57 = str(cuadricula[6][2])
	numero_58 = str(cuadricula[6][3])
	numero_59 = str(cuadricula[6][4])
	numero_60 = str(cuadricula[6][5])
	numero_61 = str(cuadricula[6][6])
	numero_62 = str(cuadricula[6][7])
	numero_63 = str(cuadricula[6][8])
	numero_64 = str(cuadricula[7][0])
	numero_65 = str(cuadricula[7][1])
	numero_66 = str(cuadricula[7][2])
	numero_67 = str(cuadricula[7][3])
	numero_68 = str(cuadricula[7][4])
	numero_69 = str(cuadricula[7][5])
	numero_70 = str(cuadricula[7][6])
	numero_71 = str(cuadricula[7][7])
	numero_72 = str(cuadricula[7][8])
	numero_73 = str(cuadricula[8][0])
	numero_74 = str(cuadricula[8][1])
	numero_75 = str(cuadricula[8][2])
	numero_76 = str(cuadricula[8][3])
	numero_77 = str(cuadricula[8][4])
	numero_78 = str(cuadricula[8][5])
	numero_79 = str(cuadricula[8][6])
	numero_80 = str(cuadricula[8][7])
	numero_81 = str(cuadricula[8][8])
	numero_01_01.config(text=numero_01)
	numero_01_02.config(text=numero_02)
	numero_01_03.config(text=numero_03)
	numero_02_01.config(text=numero_04)
	numero_02_02.config(text=numero_05)
	numero_02_03.config(text=numero_06)
	numero_03_01.config(text=numero_07)
	numero_03_02.config(text=numero_08)
	numero_03_03.config(text=numero_09)
	numero_01_04.config(text=numero_10)
	numero_01_05.config(text=numero_11)
	numero_01_06.config(text=numero_12)
	numero_02_04.config(text=numero_13)
	numero_02_05.config(text=numero_14)
	numero_02_06.config(text=numero_15)
	numero_03_04.config(text=numero_16)
	numero_03_05.config(text=numero_17)
	numero_03_06.config(text=numero_18)
	numero_01_07.config(text=numero_19)
	numero_01_08.config(text=numero_20)
	numero_01_09.config(text=numero_21)
	numero_02_07.config(text=numero_22)
	numero_02_08.config(text=numero_23)
	numero_02_09.config(text=numero_24)
	numero_03_07.config(text=numero_25)
	numero_03_08.config(text=numero_26)
	numero_03_09.config(text=numero_27)
	numero_04_01.config(text=numero_28)
	numero_04_02.config(text=numero_29)
	numero_04_03.config(text=numero_30)
	numero_05_01.config(text=numero_31)
	numero_05_02.config(text=numero_32)
	numero_05_03.config(text=numero_33)
	numero_06_01.config(text=numero_34)
	numero_06_02.config(text=numero_35)
	numero_06_03.config(text=numero_36)
	numero_04_04.config(text=numero_37)
	numero_04_05.config(text=numero_38)
	numero_04_06.config(text=numero_39)
	numero_05_04.config(text=numero_40)
	numero_05_05.config(text=numero_41)
	numero_05_06.config(text=numero_42)
	numero_06_04.config(text=numero_43)
	numero_06_05.config(text=numero_44)
	numero_06_06.config(text=numero_45)
	numero_04_07.config(text=numero_46)
	numero_04_08.config(text=numero_47)
	numero_04_09.config(text=numero_48)
	numero_05_07.config(text=numero_49)
	numero_05_08.config(text=numero_50)
	numero_05_09.config(text=numero_51)
	numero_06_07.config(text=numero_52)
	numero_06_08.config(text=numero_53)
	numero_06_09.config(text=numero_54)
	numero_07_01.config(text=numero_55)
	numero_07_02.config(text=numero_56)
	numero_07_03.config(text=numero_57)
	numero_08_01.config(text=numero_58)
	numero_08_02.config(text=numero_59)
	numero_08_03.config(text=numero_60)
	numero_09_01.config(text=numero_61)
	numero_09_02.config(text=numero_62)
	numero_09_03.config(text=numero_63)
	numero_07_04.config(text=numero_64)
	numero_07_05.config(text=numero_65)
	numero_07_06.config(text=numero_66)
	numero_08_04.config(text=numero_67)
	numero_08_05.config(text=numero_68)
	numero_08_06.config(text=numero_69)
	numero_09_04.config(text=numero_70)
	numero_09_05.config(text=numero_71)
	numero_09_06.config(text=numero_72)
	numero_07_07.config(text=numero_73)
	numero_07_08.config(text=numero_74)
	numero_07_09.config(text=numero_75)
	numero_08_07.config(text=numero_76)
	numero_08_08.config(text=numero_77)
	numero_08_09.config(text=numero_78)
	numero_09_07.config(text=numero_79)
	numero_09_08.config(text=numero_80)
	numero_09_09.config(text=numero_81)

	contador = 0
	while contador < 81:
		lista_numeros[contador].config(state=DISABLED)
		contador += 1

	lista_poner = [
		poner_01, poner_02, poner_03, poner_04, poner_05, poner_06, poner_07, poner_08, poner_09, poner_00
	]

	contador = 0
	while contador < 10:
		lista_poner[contador].config(state=DISABLED)
		contador += 1

def tutorial_tablero():
	pass

def limpiar_tablero():
	lista_numeros = [
		numero_01_01, numero_01_02, numero_01_03, numero_01_04, numero_01_05, numero_01_06, numero_01_07, numero_01_08, numero_01_09,
		numero_02_01, numero_02_02, numero_02_03, numero_02_04, numero_02_05, numero_02_06, numero_02_07, numero_02_08, numero_02_09,
		numero_03_01, numero_03_02, numero_03_03, numero_03_04, numero_03_05, numero_03_06, numero_03_07, numero_03_08, numero_03_09,
		numero_04_01, numero_04_02, numero_04_03, numero_04_04, numero_04_05, numero_04_06, numero_04_07, numero_04_08, numero_04_09,
		numero_05_01, numero_05_02, numero_05_03, numero_05_04, numero_05_05, numero_05_06, numero_05_07, numero_05_08, numero_05_09,
		numero_06_01, numero_06_02, numero_06_03, numero_06_04, numero_06_05, numero_06_06, numero_06_07, numero_06_08, numero_06_09,
		numero_07_01, numero_07_02, numero_07_03, numero_07_04, numero_07_05, numero_07_06, numero_07_07, numero_07_08, numero_07_09,
		numero_08_01, numero_08_02, numero_08_03, numero_08_04, numero_08_05, numero_08_06, numero_08_07, numero_08_08, numero_08_09,
		numero_09_01, numero_09_02, numero_09_03, numero_09_04, numero_09_05, numero_09_06, numero_09_07, numero_09_08, numero_09_09
	]

	contador = 0
	while contador < 81:
		if lista_numeros[contador].cget("state") == NORMAL:
			lista_numeros[contador].config(text="")
			contador += 1
		else:
			contador += 1
			continue

panel = Frame(ventana_raiz)
boton_panel_01 = Button(panel, width=9, relief=GROOVE, state=DISABLED)
boton_panel_02 = Button(panel, width=9, relief=GROOVE, state=DISABLED)
boton_panel_03 = Button(panel, width=9, relief=GROOVE, state=DISABLED)

def pista():
	pass

def modo_normal():
	boton_panel_01.config(text="Jugar", command=modo_jugar, state=NORMAL)
	boton_panel_02.config(text="Limpiar", command=limpiar_tablero, state=NORMAL)
	boton_panel_03.config(text="Pista", state=NORMAL, command=pista)
	nuevo_numero("")
	lista_numeros = [
		numero_01_01, numero_01_02, numero_01_03, numero_01_04, numero_01_05, numero_01_06, numero_01_07, numero_01_08, numero_01_09,
		numero_02_01, numero_02_02, numero_02_03, numero_02_04, numero_02_05, numero_02_06, numero_02_07, numero_02_08, numero_02_09,
		numero_03_01, numero_03_02, numero_03_03, numero_03_04, numero_03_05, numero_03_06, numero_03_07, numero_03_08, numero_03_09,
		numero_04_01, numero_04_02, numero_04_03, numero_04_04, numero_04_05, numero_04_06, numero_04_07, numero_04_08, numero_04_09,
		numero_05_01, numero_05_02, numero_05_03, numero_05_04, numero_05_05, numero_05_06, numero_05_07, numero_05_08, numero_05_09,
		numero_06_01, numero_06_02, numero_06_03, numero_06_04, numero_06_05, numero_06_06, numero_06_07, numero_06_08, numero_06_09,
		numero_07_01, numero_07_02, numero_07_03, numero_07_04, numero_07_05, numero_07_06, numero_07_07, numero_07_08, numero_07_09,
		numero_08_01, numero_08_02, numero_08_03, numero_08_04, numero_08_05, numero_08_06, numero_08_07, numero_08_08, numero_08_09,
		numero_09_01, numero_09_02, numero_09_03, numero_09_04, numero_09_05, numero_09_06, numero_09_07, numero_09_08, numero_09_09
	]

	contador = 0
	while contador < 81:
		lista_numeros[contador].config(text="", state=DISABLED)
		contador += 1

	lista_poner = [
		poner_01, poner_02, poner_03, poner_04, poner_05, poner_06, poner_07, poner_08, poner_09, poner_00
	]

	contador = 0
	while contador < 10:
		lista_poner[contador].config(state=DISABLED)
		contador += 1

def modo_crear():
	boton_panel_01.config(text="Crear", command=crear_juego, state=NORMAL)
	boton_panel_02.config(text="Limpiar", command=limpiar_tablero, state=NORMAL)
	boton_panel_03.config(text="Solucionar", command=solucionar, state=NORMAL)
	nuevo_numero("")
	lista_numeros = [
		numero_01_01, numero_01_02, numero_01_03, numero_01_04, numero_01_05, numero_01_06, numero_01_07, numero_01_08, numero_01_09,
		numero_02_01, numero_02_02, numero_02_03, numero_02_04, numero_02_05, numero_02_06, numero_02_07, numero_02_08, numero_02_09,
		numero_03_01, numero_03_02, numero_03_03, numero_03_04, numero_03_05, numero_03_06, numero_03_07, numero_03_08, numero_03_09,
		numero_04_01, numero_04_02, numero_04_03, numero_04_04, numero_04_05, numero_04_06, numero_04_07, numero_04_08, numero_04_09,
		numero_05_01, numero_05_02, numero_05_03, numero_05_04, numero_05_05, numero_05_06, numero_05_07, numero_05_08, numero_05_09,
		numero_06_01, numero_06_02, numero_06_03, numero_06_04, numero_06_05, numero_06_06, numero_06_07, numero_06_08, numero_06_09,
		numero_07_01, numero_07_02, numero_07_03, numero_07_04, numero_07_05, numero_07_06, numero_07_07, numero_07_08, numero_07_09,
		numero_08_01, numero_08_02, numero_08_03, numero_08_04, numero_08_05, numero_08_06, numero_08_07, numero_08_08, numero_08_09,
		numero_09_01, numero_09_02, numero_09_03, numero_09_04, numero_09_05, numero_09_06, numero_09_07, numero_09_08, numero_09_09
	]

	contador = 0
	while contador < 81:
		lista_numeros[contador].config(text="", state=DISABLED)
		contador += 1

	lista_poner = [
		poner_01, poner_02, poner_03, poner_04, poner_05, poner_06, poner_07, poner_08, poner_09, poner_00
	]

	contador = 0
	while contador < 10:
		lista_poner[contador].config(state=DISABLED)
		contador += 1

def modo_tutorial():
	pass

menu_bar = Menu(ventana_raiz)
ventana_raiz.config(menu=menu_bar)

menu_juego = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Juego", menu=menu_juego)

menu_modos = Menu(menu_juego, tearoff=0)
menu_juego.add_cascade(label="Modo", menu=menu_modos)

menu_modos.add_command(label="Jugar", command=modo_normal)
menu_modos.add_command(label="Crear", command=modo_crear)
menu_modos.add_command(label="Tutorial", command=modo_tutorial)

tablero.grid(row=0, column=0, padx=4, pady=4)

cuadro_01.grid(row=0, column=0, padx=2, pady=2)
numero_01_01.grid(row=0, column=0, padx=1, pady=1)
numero_01_02.grid(row=0, column=1, padx=1, pady=1)
numero_01_03.grid(row=0, column=2, padx=1, pady=1)
numero_01_04.grid(row=1, column=0, padx=1, pady=1)
numero_01_05.grid(row=1, column=1, padx=1, pady=1)
numero_01_06.grid(row=1, column=2, padx=1, pady=1)
numero_01_07.grid(row=2, column=0, padx=1, pady=1)
numero_01_08.grid(row=2, column=1, padx=1, pady=1)
numero_01_09.grid(row=2, column=2, padx=1, pady=1)

cuadro_02.grid(row=0, column=1, padx=2, pady=2)
numero_02_01.grid(row=0, column=0, padx=1, pady=1)
numero_02_02.grid(row=0, column=1, padx=1, pady=1)
numero_02_03.grid(row=0, column=2, padx=1, pady=1)
numero_02_04.grid(row=1, column=0, padx=1, pady=1)
numero_02_05.grid(row=1, column=1, padx=1, pady=1)
numero_02_06.grid(row=1, column=2, padx=1, pady=1)
numero_02_07.grid(row=2, column=0, padx=1, pady=1)
numero_02_08.grid(row=2, column=1, padx=1, pady=1)
numero_02_09.grid(row=2, column=2, padx=1, pady=1)

cuadro_03.grid(row=0, column=2, padx=2, pady=2)
numero_03_01.grid(row=0, column=0, padx=1, pady=1)
numero_03_02.grid(row=0, column=1, padx=1, pady=1)
numero_03_03.grid(row=0, column=2, padx=1, pady=1)
numero_03_04.grid(row=1, column=0, padx=1, pady=1)
numero_03_05.grid(row=1, column=1, padx=1, pady=1)
numero_03_06.grid(row=1, column=2, padx=1, pady=1)
numero_03_07.grid(row=2, column=0, padx=1, pady=1)
numero_03_08.grid(row=2, column=1, padx=1, pady=1)
numero_03_09.grid(row=2, column=2, padx=1, pady=1)

cuadro_04.grid(row=1, column=0, padx=2, pady=2)
numero_04_01.grid(row=0, column=0, padx=1, pady=1)
numero_04_02.grid(row=0, column=1, padx=1, pady=1)
numero_04_03.grid(row=0, column=2, padx=1, pady=1)
numero_04_04.grid(row=1, column=0, padx=1, pady=1)
numero_04_05.grid(row=1, column=1, padx=1, pady=1)
numero_04_06.grid(row=1, column=2, padx=1, pady=1)
numero_04_07.grid(row=2, column=0, padx=1, pady=1)
numero_04_08.grid(row=2, column=1, padx=1, pady=1)
numero_04_09.grid(row=2, column=2, padx=1, pady=1)

cuadro_05.grid(row=1, column=1, padx=2, pady=2)
numero_05_01.grid(row=0, column=0, padx=1, pady=1)
numero_05_02.grid(row=0, column=1, padx=1, pady=1)
numero_05_03.grid(row=0, column=2, padx=1, pady=1)
numero_05_04.grid(row=1, column=0, padx=1, pady=1)
numero_05_05.grid(row=1, column=1, padx=1, pady=1)
numero_05_06.grid(row=1, column=2, padx=1, pady=1)
numero_05_07.grid(row=2, column=0, padx=1, pady=1)
numero_05_08.grid(row=2, column=1, padx=1, pady=1)
numero_05_09.grid(row=2, column=2, padx=1, pady=1)

cuadro_06.grid(row=1, column=2, padx=2, pady=2)
numero_06_01.grid(row=0, column=0, padx=1, pady=1)
numero_06_02.grid(row=0, column=1, padx=1, pady=1)
numero_06_03.grid(row=0, column=2, padx=1, pady=1)
numero_06_04.grid(row=1, column=0, padx=1, pady=1)
numero_06_05.grid(row=1, column=1, padx=1, pady=1)
numero_06_06.grid(row=1, column=2, padx=1, pady=1)
numero_06_07.grid(row=2, column=0, padx=1, pady=1)
numero_06_08.grid(row=2, column=1, padx=1, pady=1)
numero_06_09.grid(row=2, column=2, padx=1, pady=1)

cuadro_07.grid(row=2, column=0, padx=2, pady=2)
numero_07_01.grid(row=0, column=0, padx=1, pady=1)
numero_07_02.grid(row=0, column=1, padx=1, pady=1)
numero_07_03.grid(row=0, column=2, padx=1, pady=1)
numero_07_04.grid(row=1, column=0, padx=1, pady=1)
numero_07_05.grid(row=1, column=1, padx=1, pady=1)
numero_07_06.grid(row=1, column=2, padx=1, pady=1)
numero_07_07.grid(row=2, column=0, padx=1, pady=1)
numero_07_08.grid(row=2, column=1, padx=1, pady=1)
numero_07_09.grid(row=2, column=2, padx=1, pady=1)

cuadro_08.grid(row=2, column=1, padx=2, pady=2)
numero_08_01.grid(row=0, column=0, padx=1, pady=1)
numero_08_02.grid(row=0, column=1, padx=1, pady=1)
numero_08_03.grid(row=0, column=2, padx=1, pady=1)
numero_08_04.grid(row=1, column=0, padx=1, pady=1)
numero_08_05.grid(row=1, column=1, padx=1, pady=1)
numero_08_06.grid(row=1, column=2, padx=1, pady=1)
numero_08_07.grid(row=2, column=0, padx=1, pady=1)
numero_08_08.grid(row=2, column=1, padx=1, pady=1)
numero_08_09.grid(row=2, column=2, padx=1, pady=1)

cuadro_09.grid(row=2, column=2, padx=2, pady=2)
numero_09_01.grid(row=0, column=0, padx=1, pady=1)
numero_09_02.grid(row=0, column=1, padx=1, pady=1)
numero_09_03.grid(row=0, column=2, padx=1, pady=1)
numero_09_04.grid(row=1, column=0, padx=1, pady=1)
numero_09_05.grid(row=1, column=1, padx=1, pady=1)
numero_09_06.grid(row=1, column=2, padx=1, pady=1)
numero_09_07.grid(row=2, column=0, padx=1, pady=1)
numero_09_08.grid(row=2, column=1, padx=1, pady=1)
numero_09_09.grid(row=2, column=2, padx=1, pady=1)

cuadro_numeros.grid(row=0, column=1, padx=4, pady=4)
numeros_c01.grid(row=0, column=1, padx=2, pady=2)
numeros_c02.grid(row=1, column=1, padx=2, pady=2)
numeros_c03.grid(row=2, column=1, padx=2, pady=2)
poner_01.grid(row=0, column=0, padx=1, pady=1)
poner_02.grid(row=1, column=0, padx=1, pady=1)
poner_03.grid(row=2, column=0, padx=1, pady=1)
poner_04.grid(row=0, column=0, padx=1, pady=1)
poner_05.grid(row=1, column=0, padx=1, pady=1)
poner_06.grid(row=2, column=0, padx=1, pady=1)
poner_07.grid(row=0, column=0, padx=1, pady=1)
poner_08.grid(row=1, column=0, padx=1, pady=1)
poner_09.grid(row=2, column=0, padx=1, pady=1)
poner_00.grid(row=1, column=1, padx=1, pady=1)

panel.grid(row=1, column=0, padx=4, pady=4)
boton_panel_01.grid(row=0, column=0, padx=4, pady=4)
boton_panel_02.grid(row=0, column=1, padx=4, pady=4)
boton_panel_03.grid(row=0, column=2, padx=4, pady=4)

ventana_raiz.mainloop()
