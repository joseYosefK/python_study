# implementando uma alerta a função
from tkinter import Tk, Label, Button, messagebox, PhotoImage, Entry
from saude import *

def acao():
    print('botão pescionado')
    indice = imc(peso=texto1.get(), altura=texto2.get())
    clasificação = class_imc(indice)
    msg = messagebox.showinfo('classificação do imc', clasificação)


janela = Tk()

imagem = PhotoImage(file='ilus imc.png')
log = Label(janela, image=imagem)
log.image = imagem
log.grid(row=0, column=0)

butao = Button(janela, text='clique aqui', command=acao)
butao.grid(row=1, column=3)

texto1 = Entry(janela)
texto1.grid(row=0, column=2)

texto2 = Entry(janela)
texto2.grid(row=1, column=2)

etiqueta1 = Label(janela, text='quanto você pesa?')
etiqueta1.grid(row=0, column=1)

etiqueta2 = Label(janela, text='qual é a sua altura?')
etiqueta2.grid(row=1, column=1)

janela.mainloop()
