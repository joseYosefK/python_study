# utilizando radioBUTTON em interface tk
import tkinter as tK
janela = tK.Tk()
v = tK.IntVar()
tK.Label(janela, text="Escolha uma linguagem de programação.", justify=tK.LEFT, padx=20).pack()
tK.Radiobutton(janela, text="Python", padx=20, variable=v, value=1).pack(anchor=tK.W)
tK.Radiobutton(janela, text="c++", padx=20, variable=v, value=2).pack(anchor=tK.W)
janela.mainloop()
