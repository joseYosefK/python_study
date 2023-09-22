# utilizando combobox em uma interface tk
import tkinter as tK
from tkinter import ttk
#criando uma janela com tkinter
janela = tK.Tk()
#titulo da janela
janela.title('combobox')
# atribuindo um tamanho inicial padrao
janela.geometry('500x250')
# componentes label
ttk.Label(janela, text='utilizando widget', background='green', foreground='white', font=('Times New Roman', 15)).grid(row=0, column=1)
ttk.Label(janela, text='selecione um mês', font=('Times New Roman', 15)).grid(row=5, column=0, padx=10, pady=25)
# componete combobox
n = tK.StringVar()
escolha = ttk.Combobox(janela, width=27, textvariable=n)
# adicao de itens ao combobox
escolha['values'] = (' Janeiro', ' Fevereiro', ' Março', ' Abril', ' Maio', ' Junho', ' Julho', ' Agosto', ' Setembro'
                     , ' Outubro', ' Novembro', ' Dezembro')
escolha.grid(row=5, column=1)
escolha.current()
janela.mainloop()
