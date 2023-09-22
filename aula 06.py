# exibir uma interface em janela
from tkinter import *

janelaPrincipal = Tk()
janelaPrincipal.mainloop()
texto = Label(master=janelaPrincipal, text="Minha janela exibida")
texto.place(x=50, y=100)
janelaPrincipal.mainloop()

# janela com imagem e botão
"""from tkinter import *

def funcClicar():
    print('botão precionado')

janelaPrincipal = Tk()
texto = Label(master=janelaPrincipal, text='Minha janela exibida')
texto.pack()

pic = PhotoImage(file='floers.png')
logo = Label(master=janelaPrincipal, image=pic)
logo.pack()

botao = Button(master=janelaPrincipal, text='Cliqui', command=funcClicar)
botao.pack()

janelaPrincipal.mainloop()"""

