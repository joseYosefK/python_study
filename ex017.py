panda
def funcCor_string():
   try:
     nome = input('Qual o seu nome?')
     cor_upper = nome.title().strip()
     print(cor_upper)
   except:
       print('digite somente letras')
funcCor_string()