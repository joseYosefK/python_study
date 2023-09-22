# exibido uma mensagem para o usuario em um ainterface tk
import tkinter as tK
janela= tK.Tk()
msg_p_usuario = "esta eh uma mensagem para o usuario\npode ser bastante util"
msg = tK.Message(janela, text=msg_p_usuario)
msg.config(bg='lightgreen', font=('times', 24, 'italic'))
msg.pack()
janela.mainloop()
