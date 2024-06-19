from tkinter import *
from tkinter import ttk
import math

root = Tk()
root.title ("Caluladora")
root.geometry ("+500+80")

mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0)

enter1 = StringVar()
label_enter1 = ttk.Label(mainframe, textvar=enter1)
label_enter1.grid(column=0, row=0 )

enter2 = StringVar()
label_enter2 = ttk.Label(mainframe, textvar=enter2)

button_0 = ttk.Button(mainframe, text="0")
button_1 = ttk.Button(mainframe, text="1")
button_2 = ttk.Button(mainframe, text="2")
button_3 = ttk.Button(mainframe, text="3")
button_4 = ttk.Button(mainframe, text="4")
button_5 = ttk.Button(mainframe, text="5")
button_6 = ttk.Button(mainframe, text="6")
button_7 = ttk.Button(mainframe, text="7")
button_8 = ttk.Button(mainframe, text="8")
button_9 = ttk.Button(mainframe, text="9")

button_erase = ttk.Button(mainframe, text = chr (9003))
button_erase_all = ttk.Button(mainframe, text = "C")
button_parentheses1 = ttk.Button(mainframe, text = "(")
button_parentheses2 = ttk.Button(mainframe, text = ")")
button_point = ttk.Button(mainframe, text = ".")

button_addition = ttk.Button(mainframe, text = "+") 
button_subtraction = ttk.Button(mainframe, text = "-")
button_multiplication = ttk.Button(mainframe, text = "x")
button_division = ttk.Button(mainframe , text = chr (247))

button_equal = ttk.Button(mainframe , text = "=")
button_square_root = ttk.Button(mainframe , text = chr ('\u221A'))

#colocar botones en pantalla

button_parentheses1.grid(column = 0, row = 2)
button_parentheses2.grid(column = 1, row = 2)
button_erase_all.grid(column = 2, row = 2 )