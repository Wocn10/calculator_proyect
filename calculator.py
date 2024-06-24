from tkinter import *
from tkinter import ttk
import math

def TemeBlack(*args):
    styles.configure("mainframe.TFrame", background = "#010924")
    styles_enter1.configure("Enter1.TLabel", background = "#010924", foreground = "white")
    styles_enter2.configure("Enter2.TLabel", background = "#010924", foreground = "white")

    styles_button_numbers.configure("Button_numbers.TButton", background = "#00044A", foreground = "white")
    styles_button_numbers.map("Button_numbers.TButton", background = [("active", "#E01000")])

    styles_button_erase.configure("Button_erase.TButton", background = "#010924", foreground = "white")
    styles_button_erase.map("Button_erase.TButton", background = [("active", "#325BD6")])

    styles_button_others.configure("Button_others.TButton", background = "#010924", foreground = "white")
    styles_button_others.map("Button_others.TButton", background = [("active", "#E05E00")])

def TemeWhite(*args):
    styles.configure("")

root = Tk()
root.title("Caluladora")
root.geometry("+500+80")
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)

#Estilos del Frame
styles = ttk.Style()
styles.theme_use("clam")
styles.configure("mainframe.TFrame", background ="#DBDBDB")

mainframe = ttk.Frame(root, style = "mainframe.TFrame")
mainframe.grid(column = 0, row = 0, sticky = (W, N, E, S))
mainframe.columnconfigure(0, weight = 1)
mainframe.columnconfigure(1, weight = 1)
mainframe.columnconfigure(2, weight = 1)
mainframe.columnconfigure(3, weight = 1)

mainframe.rowconfigure(0, weight = 1)
mainframe.rowconfigure(1, weight = 1)
mainframe.rowconfigure(2, weight = 1)
mainframe.rowconfigure(3, weight = 1)
mainframe.rowconfigure(4, weight = 1)
mainframe.rowconfigure(5, weight = 1)
mainframe.rowconfigure(6, weight = 1)
mainframe.rowconfigure(7, weight = 1)

#Estilis de los label_enter1
styles_enter1 = ttk.Style()
styles_enter1.configure("Enter1.TLabel", font = "arial 15", anchor = "E" )

enter1 = StringVar()
label_enter1 = ttk.Label(mainframe, textvar = enter1, style = "Enter1.TLabel")
label_enter1.grid(column = 0, row = 0, columnspan = 4, sticky = (W, N, E, S))

#Estilis de los label_enter2
styles_enter2 = ttk.Style()
styles_enter2.configure("Enter2.TLabel", font = "arial 40", anchor = "e" )

enter2 = StringVar()
label_enter2 = ttk.Label(mainframe, textvar=enter2, style = "Enter2.TLabel")
label_enter2.grid(column = 0, row = 1, columnspan = 4, sticky = (W, N, E, S))

#Estilos para los botones
styles_button_numbers = ttk.Style()
styles_button_numbers.configure("Button_numbers.TButton", font = "arial 22", width = 5, background = "#FFFFFF", relief = "flat")
styles_button_numbers.map("Button_numbers.TButton", foreground = [("active", "#3337E0")])

styles_button_erase = ttk.Style()
styles_button_erase.configure("Button_erase.TButton", font = "arial 22", width = 5, background = "#CECECE", relief = "flat")
styles_button_erase.map("Button_erase.TButton", foreground = [("active", "#FF0000")])

styles_button_others = ttk.Style()
styles_button_others.configure("Button_others.TButton", font = "arial 22", width = 5, background = "#CECECE", relief = "flat")
styles_button_others.map("Button_others.TButton", foreground = [("active", "#00E029")])

#Botones
button_0 = ttk.Button(mainframe, text = "0", style = "Button_numbers.TButton")
button_1 = ttk.Button(mainframe, text = "1", style = "Button_numbers.TButton")
button_2 = ttk.Button(mainframe, text = "2", style = "Button_numbers.TButton")
button_3 = ttk.Button(mainframe, text = "3", style = "Button_numbers.TButton")
button_4 = ttk.Button(mainframe, text = "4", style = "Button_numbers.TButton")
button_5 = ttk.Button(mainframe, text = "5", style = "Button_numbers.TButton")
button_6 = ttk.Button(mainframe, text = "6", style = "Button_numbers.TButton")
button_7 = ttk.Button(mainframe, text = "7", style = "Button_numbers.TButton")
button_8 = ttk.Button(mainframe, text = "8", style = "Button_numbers.TButton")
button_9 = ttk.Button(mainframe, text = "9", style = "Button_numbers.TButton")

button_erase = ttk.Button(mainframe, text = chr (9003), style = "Button_erase.TButton")
button_erase_all = ttk.Button(mainframe, text = "C", style = "Button_erase.TButton")
button_parentheses1 = ttk.Button(mainframe, text = "(", style = "Button_others.TButton")
button_parentheses2 = ttk.Button(mainframe, text = ")", style = "Button_others.TButton")
button_point = ttk.Button(mainframe, text = ".", style = "Button_others.TButton")

button_addition = ttk.Button(mainframe, text = "+", style = "Button_others.TButton") 
button_subtraction = ttk.Button(mainframe, text = "-", style = "Button_others.TButton")
button_multiplication = ttk.Button(mainframe, text = "x", style = "Button_others.TButton")
button_division = ttk.Button(mainframe , text = chr (247), style = "Button_others.TButton")

button_equal = ttk.Button(mainframe , text = "=", style = "Button_others.TButton")
button_square_root = ttk.Button(mainframe , text = "√", style = "Button_others.TButton")

#colocar botones en pantalla
#Fila 2
button_parentheses1.grid(column = 0, row = 2, sticky = (W, N, E, S))
button_parentheses2.grid(column = 1, row = 2, sticky = (W, N, E, S))
button_erase_all.grid(column = 2, row = 2, sticky = (W, N, E, S))
button_erase.grid(column = 3, row = 2, sticky = (W, N, E, S))

#Fila 3
button_7.grid(column = 0, row = 3, sticky = (W, N, E, S))
button_8.grid(column = 1, row = 3, sticky = (W, N, E, S))
button_9.grid(column = 2, row = 3, sticky = (W, N, E, S))
button_division.grid(column = 3, row = 3, sticky = (W, N, E, S))

#Fila 4
button_4.grid(column = 0, row = 4, sticky = (W, N, E, S))
button_5.grid(column = 1, row = 4, sticky = (W, N, E, S))
button_6.grid(column = 2, row = 4, sticky = (W, N, E, S))
button_multiplication.grid(column = 3, row = 4, sticky = (W, N, E, S))

#Fila 5
button_1.grid(column = 0, row = 5, sticky = (W, N, E, S))
button_2.grid(column = 1, row = 5, sticky = (W, N, E, S))
button_3.grid(column = 2, row = 5, sticky = (W, N, E, S))
button_addition.grid(column = 3, row = 5, sticky = (W, N, E, S))

#Fila 6
button_0.grid(column = 0, row = 6, columnspan = 2, sticky = (W, N, E, S))
button_point.grid (column = 2, row = 6, sticky = (W, N, E, S))
button_subtraction.grid (column = 3, row = 6, sticky = (W, N, E, S))

#Fila 7
button_equal.grid(column = 0, row = 7, columnspan = 3, sticky = (W, N, E, S))
button_square_root.grid(column = 3, row = 7, sticky = (W, N, E, S))

for child in mainframe.winfo_children():
    child.grid_configure(ipady = 10, padx = 1, pady = 1)

root.bind("<KeyPress-o>", TemeBlack)

root, mainloop()