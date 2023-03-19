#Humberto Hernández Trejo
import tkinter as tk
from tkinter import *
from tkinter import ttk

raiz = Tk()
raiz.geometry("1265x600")

#frames

tituloFrame = Frame(raiz, bg="#097479",padx=10)
tituloFrame.grid(column=0, row= 0)

fondoFrame = Frame(raiz,bg="black",padx=125,pady=6)
fondoFrame.grid(column=0, row=1)

indiFrame = Frame(fondoFrame, padx=11,pady=15,bg="gray20")
indiFrame.grid(column=0, row=0,rowspan=3,sticky=(N))

tempFrame = Frame(fondoFrame,padx=22,pady=18,bg="gray20")
tempFrame.grid(column=2, row=0,columnspan=4,rowspan=3,sticky=())
ctempFrame= Frame(tempFrame,padx=5,pady=18,bg="gray20",)
ctempFrame.grid(column=0, row=1,columnspan=2)

prodFrame = Frame(fondoFrame,padx=5,pady=11,bg="gray20")
prodFrame.grid(column=7, row=0, sticky=(E),rowspan=5)

bombFrame = Frame(fondoFrame,padx=4,pady=35,bg="gray20")
bombFrame.grid(column=0, row=4,columnspan=3,rowspan=2,sticky=(W))

tanqFrame = Frame(fondoFrame,padx=27,pady=11,bg="gray20")
tanqFrame.grid(column=4, row=4, sticky=(),columnspan=2, rowspan=2)

#labels sep
fondo1Frame = Frame(raiz,bg="black",padx=630,pady=30)
fondo1Frame.grid(column=0, row=2)
ttk.Label(fondo1Frame,text="",foreground="black",background="black").grid()
#indi
ttk.Label(fondoFrame,text="",foreground="black",font=("Calibri",1),background="black").grid(column=1, row=0)
#temp
ttk.Label(fondoFrame,text="",foreground="black",font=("Calibri",1),background="black").grid(column=6, row=0)
#mid
ttk.Label(fondoFrame,text="", font=("Calibri",1),foreground="black",background="black").grid(column=0, row=3, columnspan=7)
#bomb
ttk.Label(fondoFrame,text="", font=("Calibri",1),foreground="black",background="black").grid(column=3, row=4)
#tanq
ttk.Label(fondoFrame,text="",font=("Calibri",1),foreground="black",background="black").grid(column=6, row=4)

#label titulo
ttk.Label(tituloFrame, text="SPAI 4.0 ",padding="0 0 1124 0",font=("Calibri", 14),foreground="white",background="#097479",compound=LEFT).grid(column=1, row=0,sticky=(W))

#boton imagen titulo
barras = PhotoImage(file="barras3.png")
Button(tituloFrame,image=barras,bg="light sea green",padx=10,borderwidth=0,highlightthickness=0,activebackground="#097479",compound=RIGHT).grid(column=0,row=0,sticky=(E))

#labels indi
ttk.Label(indiFrame, text="Indicadores Digitales",font=("Calibri", 13),foreground="light sea green",background="gray20").grid(column=0, row=0,columnspan=3,sticky=(W))
ttk.Label(indiFrame, text="Linea 1: ",font=("Calibri", 11),padding="2 10 10 8",foreground="white",background="gray20").grid(column=0, row=1,sticky=(W))
ttk.Label(indiFrame, text="Linea 2: ",font=("Calibri", 11),padding="2 10 10 10",foreground="white",background="gray20").grid(column=0, row=2,sticky=(W))
ttk.Label(indiFrame, text="Linea 1:",font=("Calibri", 11),padding="2 10 10 10",foreground="white",background="gray20").grid(column=0, row=3, sticky=(W))
ttk.Label(indiFrame, text="Gabinete:",font=("Calibri", 11),padding="2 10 10 10",foreground="white",background="gray20").grid(column=0, row=4, sticky=(W))
ttk.Label(indiFrame, text="Alarma:",font=("Calibri", 11),padding="2 10 10 10",foreground="white",background="gray20").grid(column=0, row=5, sticky=(W))
ttk.Label(indiFrame, text="Alarma 2: ",font=("Calibri", 11),padding="2 8 10 10",foreground="white",background="gray20").grid(column=0, row=6, sticky=(W))

#buttons indi
class ToggleButton(tk.Canvas):
    def __init__(self, parent, size=50, active_color="green", inactive_color="red", initial_value=False, **kwargs):
        super().__init__(parent, width=size, height=size, highlightthickness=0, **kwargs)

        self.active_color = active_color
        self.inactive_color = inactive_color

        self.on = initial_value
        self.color = active_color if initial_value else inactive_color
        self.create_oval(0, 0, size, size, fill=self.color, width=0)

        self.bind("<Button-1>", self.toggle)
        self.label = tk.Label(parent, text="On" if initial_value else "Off",font=("Calibri", 11,"bold"),background="gray20",foreground="white")
        self.label.grid(column=1,row=1)

    def toggle(self, event=None):
        self.on = not self.on
        self.color = self.active_color if self.on else self.inactive_color
        self.itemconfigure(1, fill=self.color)
        self.label.config(text="On" if self.on else "Off")

class ToggleButton2(tk.Canvas):
    def __init__(self, parent, size=50, active_color="green", inactive_color="red", initial_value=False, **kwargs):
        super().__init__(parent, width=size, height=size, highlightthickness=0, **kwargs)

        self.active_color = active_color
        self.inactive_color = inactive_color

        self.on = initial_value
        self.color = active_color if initial_value else inactive_color
        self.create_oval(0, 0, size, size, fill=self.color, width=0)

        self.bind("<Button-1>", self.toggle)
        self.label = tk.Label(parent, text="On" if initial_value else "Off",font=("Calibri", 11,"bold"),background="gray20",foreground="white")
        self.label.grid(column=1,row=2)

    def toggle(self, event=None):
        self.on = not self.on
        self.color = self.active_color if self.on else self.inactive_color
        self.itemconfigure(1, fill=self.color)
        self.label.config(text="On" if self.on else "Off")

class ToggleButton3(tk.Canvas):
    def __init__(self, parent, size=50, active_color="green", inactive_color="red", initial_value=False, **kwargs):
        super().__init__(parent, width=size, height=size, highlightthickness=0, **kwargs)

        self.active_color = active_color
        self.inactive_color = inactive_color

        self.on = initial_value
        self.color = active_color if initial_value else inactive_color
        self.create_oval(0, 0, size, size, fill=self.color, width=0)

        self.bind("<Button-1>", self.toggle)
        self.label = tk.Label(parent, text="On" if initial_value else "Off",font=("Calibri", 11,"bold"),background="gray20",foreground="white")
        self.label.grid(column=1,row=3)

    def toggle(self, event=None):
        self.on = not self.on
        self.color = self.active_color if self.on else self.inactive_color
        self.itemconfigure(1, fill=self.color)
        self.label.config(text="On" if self.on else "Off")

class ToggleButton4(tk.Canvas):
    def __init__(self, parent, size=50, active_color="green", inactive_color="red", initial_value=False, **kwargs):
        super().__init__(parent, width=size, height=size, highlightthickness=0, **kwargs)

        self.active_color = active_color
        self.inactive_color = inactive_color

        self.on = initial_value
        self.color = active_color if initial_value else inactive_color
        self.create_oval(0, 0, size, size, fill=self.color, width=0)

        self.bind("<Button-1>", self.toggle)
        self.label = tk.Label(parent, text="Abierto        " if initial_value else "Cerrado       ",font=("Calibri", 11,"bold"),background="gray20",foreground="white")
        self.label.grid(column=1, row=4,sticky=W)

    def toggle(self, event=None):
        self.on = not self.on
        self.color = self.active_color if self.on else self.inactive_color
        self.itemconfigure(1, fill=self.color)
        self.label.config(text="Abierto        " if self.on else "Cerrado       ")

class ToggleButton5(tk.Canvas):
    def __init__(self, parent, size=50, active_color="green", inactive_color="red", initial_value=False, **kwargs):
        super().__init__(parent, width=size, height=size, highlightthickness=0, **kwargs)

        self.active_color = active_color
        self.inactive_color = inactive_color

        self.on = initial_value
        self.color = active_color if initial_value else inactive_color
        self.create_oval(0, 0, size, size, fill=self.color, width=0)

        self.bind("<Button-1>", self.toggle)
        self.label = tk.Label(parent, text="On" if initial_value else "Off",font=("Calibri", 11,"bold"),background="gray20",foreground="white")
        self.label.grid(column=1,row=5)

    def toggle(self, event=None):
        self.on = not self.on
        self.color = self.active_color if self.on else self.inactive_color
        self.itemconfigure(1, fill=self.color)
        self.label.config(text="On" if self.on else "Off")

class ToggleButton6(tk.Canvas):
    def __init__(self, parent, size=50, active_color="green", inactive_color="red", initial_value=False, **kwargs):
        super().__init__(parent, width=size, height=size, highlightthickness=0, **kwargs)

        self.active_color = active_color
        self.inactive_color = inactive_color

        self.on = initial_value
        self.color = active_color if initial_value else inactive_color
        self.create_oval(0, 0, size, size, fill=self.color, width=0)

        self.bind("<Button-1>", self.toggle)
        self.label = tk.Label(parent, text="On" if initial_value else "Off",font=("Calibri", 11,"bold"),background="gray20",foreground="white")
        self.label.grid(column=1,row=6)

    def toggle(self, event=None):
        self.on = not self.on
        self.color = self.active_color if self.on else self.inactive_color
        self.itemconfigure(1, fill=self.color)
        self.label.config(text="On" if self.on else "Off")

button1 = ToggleButton(indiFrame, size=12, active_color="green", inactive_color="red", initial_value=False,background="gray20")
button1.grid(column=2,row=1)

button2 = ToggleButton2(indiFrame, size=12, active_color="green", inactive_color="red", initial_value=False,background="gray20")
button2.grid(column=2,row=2)

button3 = ToggleButton3(indiFrame, size=12, active_color="green", inactive_color="red", initial_value=False,background="gray20")
button3.grid(column=2,row=3)

button4 = ToggleButton4(indiFrame, size=12, active_color="green", inactive_color="red", initial_value=False,background="gray20")
button4.grid(column=2,row=4)

button5 = ToggleButton5(indiFrame, size=12, active_color="green", inactive_color="red", initial_value=False,background="gray20")
button5.grid(column=2,row=5)

button6 = ToggleButton6(indiFrame, size=12, active_color="green", inactive_color="red", initial_value=False,background="gray20")
button6.grid(column=2,row=6)

#imagenes temp
temp1 = PhotoImage(file="temp1.png")
temp2 = PhotoImage(file="temp2.png")
#labels temp
ttk.Label(tempFrame, text="Temperaturas",font=("Calibri", 13),padding="2 0 0 5",foreground="light sea green",background="gray20",compound=TOP).grid(column=0, row=0,sticky=(W,N))
ttk.Label(ctempFrame, text="Temperatura 1:",font=("Calibri", 11),foreground="white",background="gray20").grid(column=0, row=0, sticky=())
ttk.Label(ctempFrame, text="Temperatura 2:",font=("Calibri", 11),foreground="white",background="gray20").grid(column=1, row=0, sticky=())
ttk.Label(tempFrame, text="Temp. Agua:",font=("Calibri",11),padding="0 5 0 8",foreground="white",background="gray20").grid(column=0, row=2, sticky=(E))
ttk.Label(tempFrame, text="58 °C",font=("Calibri", 11,"bold"),padding="0 5 8 8",foreground="white",background="gray20").grid(column=1, row=2, sticky=(W))
ttk.Label(tempFrame, text="Temp. Ambiente:",font=("Calibri", 11),padding="0 8 0 9",foreground="white",background="gray20").grid(column=0, row=3, sticky=(E))
ttk.Label(tempFrame, text="32 °C",font=("Calibri", 11,"bold"),padding="0 8 8 9",foreground="white",background="gray20").grid(column=1, row=3, sticky=(W))
ttk.Label(ctempFrame,image=temp1,foreground="white",background="gray20").grid(column=0, row=3, sticky=(W))
ttk.Label(ctempFrame, image=temp2,foreground="white",background="gray20").grid(column=1, row=3, sticky=(W))

#imagen velocidad
vel = PhotoImage(file="bomba.png")
#labels velocidad
ttk.Label(bombFrame, text="Velocidad bomba: ",padding="0 2 0 2",font=("Calibri", 13),foreground="white",background="gray20").grid(column=0, row=0, sticky=())
ttk.Label(bombFrame, image=vel,background="gray20",padding="20 0 30 0").grid(column=0, row=1, sticky=(W))

#imagen tanque
tanq = PhotoImage(file="tanque.png")
#label tanque
ttk.Label(tanqFrame, text="Nivel del Tanque",font=("Calibri", 13),padding="0 5 0 5",foreground="light sea green",background="gray20").grid(column=0, row=0, sticky=(W))
ttk.Label(tanqFrame, image=tanq,foreground="gray20",background="gray20",padding="0 0 58 0").grid(column=0, row=1, sticky=(W))

#imagen producción
prod = PhotoImage(file="produccion.png")
#label producción
ttk.Label(prodFrame, text="Producción",font=("Calibri", 14),foreground="light sea green",background="gray20",padding="0 0 0 10").grid(column=1, row=3, sticky=(W))
ttk.Label(prodFrame, image=prod,background="gray20",padding="2 10 2 15").grid(column=1, row=4,columnspan=2, sticky=(W))
ttk.Label(prodFrame, text="Piezas producidas: ",font=("Calibri", 11),foreground="white",background="gray20",compound=RIGHT,padding="0 20 0 15").grid(column=1, row=5, sticky=(E))
ttk.Label(prodFrame, text="Piezas defectuosas: ",font=("Calibri", 11),foreground="white",background="gray20",compound=RIGHT,padding="0 10 0 9").grid(column=1, row=6, sticky=(E))
ttk.Label(prodFrame, text="50",font=("Calibri", 11,"bold"),foreground="white",background="gray20", compound=LEFT,padding="0 20 0 15").grid(column=2, row=5, sticky=(W))
ttk.Label(prodFrame, text="12",font=("Calibri", 11,"bold"),foreground="white",background="gray20", compound=LEFT,padding="0 10 0 9").grid(column=2, row=6, sticky=(W))
 
#scrollbar 
scrollbar = ttk.Scrollbar(orient=VERTICAL)
scrollbar.set(0, 0.96)
scrollbar.place(x=1249, y=50, height=550)

style=ttk.Style()
style.theme_use('winnative')
style.configure("Vertical.TScrollbar", )


raiz.mainloop()