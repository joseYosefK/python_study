# envio de emal altomatico
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

msg = MIMEMultipart()
texto = 'Estou te enviando esse email com python'

# parametros
senha = 'Sua senha'
msg['From'] = 'Seu e-mail'
msg['To'] = 'E-mail de destino'
msg['Subject'] = 'Assunto'
# criação do corpo da mensagem
msg.attach(MIMEText(texto, 'plain'))

# criação do servisor
sever = smtplib.SMTP('smtp.gmail.com:  587')
sever.starttls()
# login na conta para enviar
sever.login(msg['Fron'], senha)

# envio de mensagem
sever.sendmail(msg['From'], msg['To'], msg.as_string())

# enserramento do servidor
sever.quit()

print('mensagem envida com sucesso!')