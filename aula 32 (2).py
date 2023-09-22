# interface frafica utilizando botao
import tkinter as tK

contador = 0
def contador_label(lblrotulo):
    def func_contar():
        global contador
        contador += 1
        lblrotulo.config(text=str(contador))
        lblrotulo.after(1000, func_contar)
    return func_contar()

janela = tK.Tk()
janela.title('contagem dos segundos')
lblrotulo = tK.Label(janela, fg="Red")
lblrotulo.pack()
contador_label(lblrotulo)
btacao = tK.Button(janela, text="clique aqui para interromper a contagem", width=50, command=janela.destroy)
btacao.pack()
janela.mainloop()
