# utilizando a fuçao Entry para receber entrada do usuario
import tkinter as tK

def mostrar_nomes():
    print("nome:%s\nsobrenome:%s" % (e1.get(), e2.get()))

janela = tK.Tk()
janela.title("interface com aplicação Entry")
tK.Label(janela, text="nome").grid(row=0)
e1 = tK.Entry(janela)
e2 = tK.Entry(janela)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
tK.Button(janela, text="sair", command=janela.quit).grid(row=3, column=0, sticky=tK.W, pady=4)
tK.Button(janela, text="exibir dados", command=mostrar_nomes).grid(row=3, column=1, sticky=tK.W, pady=4)

janela.mainloop()
