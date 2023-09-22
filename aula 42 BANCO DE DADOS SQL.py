# utilizando o metodo crud
import psycopg2
class AppBD():
    def __init__(self):
        print('metodo contrutor')

    def abrir_conexao(self):
        try:
            self.conection = psycopg2.connect(user="postgres", password="Junior12",
                                              host="127.0.0.1", port="5432",database="postgres")
        except(Exception, psycopg2.Error) as error:
            if (self.conection):
                print('erro ao conectar ao banco de dados', error)

    def selecionador(self):
        try:
            self.abrir_conexao()
            cursor = self.conection.cursor()
            print('selecionando todos os produtos')
            sql_select_query = """select * public."PRODUTOS" """

            cursor.execute(sql_select_query)
            resistro = cursor.fetchall()
            print(resistro)

        except (Exception,psycopg2.Error) as error:
            print('error in select operation', error)

        finally:
            #close database
            if (self.conection):
                cursor.close()
                self.conection.close()
                print('a conexão com a postgreSQL foi fechada')

        return resistro

    def inserirdados(self,codigo, nome, preco):
        try:
            self.abrir_conexao()
            cursor = self.conection.cursor()
            postgre_insert_quey = """INSERT INTO public."PRODUTOS"("CODIGO", "NOME", "PRECO")
            VALUES(%s, %s, %s)"""
            record_to_insert = (nome, preco, codigo)
            cursor.execute(postgre_insert_quey,record_to_insert)
            self.conection.commit()
            count = cursor.rowcount
            print(count,'regidtro inserido com sucesso na tabela PRODUTOS')
        except(Exception, psycopg2.Error)  as error:
            if (self.conection):
                print('erro ao inserir registro na tabela PRODUTOS', error)
        finally:
            if (self.conection):
                cursor.close()
                self.conection.close()
                print('a conexão com postreSQL foi fechada')

    def atualizardados(self,nome, preco, codigo):
        try:
            self.abrir_conexao()
            cursor = self.conection.cursor()
            print('registro antes da atualização')
            sql_select_query = """select * from public "PRODUTOS" where "CODIGO" = %s"""
            cursor.execute(sql_select_query,(codigo,))
            record = cursor.fetchone()
            print(record)
            #atualizar registro
            sql_update_query = """update public."PRODUTOS"
             set "NOME" = %S, "PRECO" = %s where "CODIGO" = %s"""
            cursor.execute(sql_update_query,(nome, preco, codigo))
            self.conection.commit()
            count = cursor.rowcount
            print('registro atualizado com sucesso')
            print('registro depois da atualização')
            sql_select_query = """select * from public "PRODUTOS" where "CODIGO" = %s"""
            cursor.execute(sql_select_query, (codigo,))
            record = cursor.fetchone()
            print(record)

        except(Exception, psycopg2.Error) as error:
            if (self.conection):
                print('erro ao atualizar a tabela', error)
        finally:
            if (self.conection):
                cursor.close()
                self.conection.close()
                print('a conexão com postreSQL foi fechada')

    def excluirdados(self, codigo):
        try:
            self.abrir_conexao()
            cursor = self.conection.cursor()
            sql_delete_query = """delet from public."PRODUTOS" where "CODIGO" = %s"""
            cursor.execute(sql_delete_query,(codigo, ))
            self.conection.commit()
            count = cursor.rowcount
            print(count,'registro excluido com sucesso!')

        except(Exception, psycopg2.Error) as error:
            if (self.conection):
                print('erro ao excluir dados', error)
        finally:
            if (self.conection):
                cursor.close()
                self.conection.close()
                print('a conexão com postreSQL foi fechada')