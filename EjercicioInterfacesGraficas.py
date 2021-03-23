import tkinter as tk
from tkinter import ttk
from MedidasSenseHat import *

Periodo = 1000

class App:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Medidor SenseHat")
        self.sense = medida()
        self.midiendo = True
        self.periodo = Periodo

        self.labelframe1=ttk.LabelFrame(self.ventana, text="Boton controlador:")        
        self.labelframe1.grid(column=0, row=0)
        self.controlador()

        self.labelframe2=ttk.LabelFrame(self.ventana, text="Medidas:")        
        self.labelframe2.grid(column=0, row=1)
        self.medidor()

        self.ventana.after(self.periodo,self.llamada_medir)
        self.ventana.mainloop()

    def controlador(self):
        self.boton=tk.Button(self.labelframe1, text="Parar", bg="green", command=self.configurar_boton)
        self.boton.grid(column=0, row=0)

        self.label = tk.Label(self.labelframe1, text = "Periodo = 1000 ms")
        self.label.grid(column=0, row=1)

    def medidor(self):
        self.seleccion=tk.IntVar()
        self.seleccion.set(1)
        self.variable = 0

        self.radio1=tk.Radiobutton(self.labelframe2,text="Humedad", variable=self.seleccion, value=1)
        self.radio1.grid(column=0, row=1)
        self.radio2=tk.Radiobutton(self.labelframe2,text="Temperatura", variable=self.seleccion, value=2)
        self.radio2.grid(column=1, row=1)
        self.radio3=tk.Radiobutton(self.labelframe2,text="Presion", variable=self.seleccion, value=3)
        self.radio3.grid(column=2, row=1)

        if self.seleccion == 2:
            self.variable = 1
        elif self.seleccion == 3:
            self.variable = 2

        self.label2=tk.Label(self.labelframe2, width=10)
        self.label2.config(bg = "white")
        self.label2.grid(column=1, row=0)

        self.label2.config(text= self.sense[self.variable])
    
    def configurar_boton(self):
        self.boton.config(text="Comenzar", bg="red")
        self.midiendo = False

    def llamada_medir(self):
        if self.midiendo == True:
            self.label2.config(text = self.sense[self.variable])
        else:
            self.label2.config(text = "")

Aplicacion = App()