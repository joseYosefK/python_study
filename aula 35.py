# utilizando checkbutton em uma interface tk
import tkinter as tK
from tkinter import ttk
janela = tK.Tk()
def escolha_carreira():
    print("gerencial:%d\ntecnico:%d" % (var1.get(), var2.get()))
ttk.Label(janela,text="escolha uma profição:").grid(row=0,sticky=tK.W)
var1 = tK.IntVar()
ttk.Checkbutton(janela, text="gerencial", variable=var1).grid(row=1, sticky=tK.W)
var2 = tK.IntVar()
ttk.Checkbutton(janela, text="tecnico", variable=var2).grid(row=2, sticky=tK.W)
ttk.Button(janela, text="sair", command=janela.quit).grid(row=3, sticky=tK.W, pady=4)
ttk.Button(janela, text="mostrar", command=escolha_carreira).grid(row=4, sticky=tK.W, pady=4)
janela.mainloop()
