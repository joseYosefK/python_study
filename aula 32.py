# manipulaçao de arquivoz
import os
import playsound
arquivo = open("C:\music\Kalun Escot.mp3")
print('arquivo aberto')
print(os.path.relpath(arquivo.name))# caminho relativo
print(os.path.abspath(arquivo.name))# caminho absoluto
print(arquivo.mode)# modo do arquivo

arquivo.close()
print('arquivo fechado?', arquivo.closed)