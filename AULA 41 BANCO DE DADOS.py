# interação com banco de dados sql criação de uma tabela em sql
import psycopg2
from faker import Faker
conn = psycopg2.connect(database="postgres", user="postgres",
                        password="Junior12", host="127.0.0.1", port="5432")
print('connexão esta aberta')
cursor = conn.cursor()
fake = Faker('pt_BR')
N = 10
for i in range(N):
    codigo = i + 10
    nome = 'produto_' + str(i + 1)
    preco = fake.pyfloat(left_digits=3, right_digits=2, positive=True, min_value=5, max_value=1000)
    print(preco)
    print(nome)



comandoSQL = """INSERT INTO public."PRODUTOS"("CODIGO", "NOME","PRECO")
VALUES(%s, %s, %s)"""

conn.commit()
print('inserção realizada com sucesso!')
conn.close()
