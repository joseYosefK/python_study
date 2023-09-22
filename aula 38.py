# utilizando escala em uma interface tk
import tkinter as tK
from tkinter import ttk
def mostrar_valores():
    print(w1.get(), w2.get())
janela = tK.Tk()
w1 = ttk.Scale(janela, from_=0, to=50)
w1.pack()
w2 = ttk.Scale(janela, from_=0, to=100)
w2.pack()
ttk.Button(janela, text="guardar", command=mostrar_valores).pack()
janela.mainloop()
