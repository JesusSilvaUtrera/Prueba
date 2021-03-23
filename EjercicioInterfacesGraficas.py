import tkinter as tk
from tkinter import ttk
from MedidasSenseHat import *

class App:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Medidor SenseHat")
        self.sense = medida()
        self.midiendo = True

        self.labelframe1=ttk.LabelFrame(self.ventana, text="Boton controlador:")        
        self.labelframe1.grid(column=0, row=0)
        self.controlador()

        self.labelframe2=ttk.LabelFrame(self.ventana, text="Medidas:")        
        self.labelframe2.grid(column=0, row=1)
        self.medidor()

        self.ventana.mainloop()

    def controlador(self):
        self.boton=tk.Button(self.labelframe1, text="Parar", bg="green", command=self.configurar_boton)
        self.boton.grid(column=0, row=0)

        self.label = tk.Label(self.labelframe1, text = "Periodo = 1000 ms")
        self.label.grid(column=0, row=1)

    def medidor(self):
        self.seleccion=tk.IntVar()
        self.seleccion.set(1)
        variable = 0

        self.radio1=tk.Radiobutton(self.labelframe2,text="Humedad", variable=self.seleccion, value=1)
        self.radio1.grid(column=0, row=1)
        self.radio2=tk.Radiobutton(self.labelframe2,text="Temperatura", variable=self.seleccion, value=2)
        self.radio2.grid(column=1, row=1)
        self.radio3=tk.Radiobutton(self.labelframe2,text="Presion", variable=self.seleccion, value=3)
        self.radio3.grid(column=2, row=1)

        if self.seleccion == 2:
            variable = 1
        elif self.seleccion == 3:
            variable = 2

        self.entry=tk.Entry(self.labelframe2, width=10)
        self.entry.grid(column=1, row=0)

        while self.midiendo == True:
            self.entry.config(textvariable= self.sense[variable])
    
    def configurar_boton(self):
        self.boton.config(text="Comenzar", bg="red")
        self.midiendo = False

Aplicacion = App()