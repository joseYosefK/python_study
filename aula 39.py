# implementando caixa de dialogos em uma interface tk
import tkinter as tK
from tkinter import messagebox as mb
def resposta():
    mb.showerror("Resposta","Desculpe nenhuma resposta disponivel")

def verificacao():
    if mb.askyesno("Verificar", 'Realmente deseja sair?'):
        mb.showwarning("Yes", 'ainda não foi implementado')
    else:
        mb.showinfo("No", 'A poção sair foi cancelada')
janela = tK.Tk()
janela.title("caixas dialogo")
janela.geometry('500x250')
tK.Button(janela, text="sair",command=verificacao).pack(fill=tK.X)
tK.Button(janela, text="resposta", command=resposta).pack(fill=tK.X)
janela.mainloop()