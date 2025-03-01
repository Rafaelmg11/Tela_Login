import mysql.connector #Importa o módulo mysql.connector para conectar ao banco de dados MySQL

#PARA RODAR O PROJETO NAO POSSO ESQUECER DE DIGITAR O CODIGO ABAIXO NO CONSOLE(TELA DE EXECUÇÃO)
# pip install mysql-connector-python

class Database:
    def __init__(self):
        #Conecta ao banco de dados MySQL com as credenciais fornecidas
        self.conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "rafaelmagalhaes_db"
        )
        self.cursor = self.conn.cursor()#Cria um cursor para executar comandos SQL
        #Cria a tabela 'usuario' se ela não existir
        self.cursor.execute(''' CREATE TABLE IF NOT EXISTS usuario1(
            idUsuario INT AUTO_INCREMENT PRIMARY KEY,
            nome TEXT (255),
            email TEXT (255),
            usuario TEXT (255),
            senha TEXT (255)
            );''')
        self.conn.commit()#Confirma a criação da tabela

        print("concectado ao banco de Dados")#Imprime uma mensagem de comfirmação

    #METODO PARA REGISTRAR UM NOVO USUARIO NO BANCO DE DADOS
    def RegistrarNoBanco(self,nome,email,usuario,senha):
        self.cursor.execute("INSERT INTO usuario1 (nome,email,usuario,senha)VALUES (%s,%s,%s,%s)",(nome,email,usuario,senha)) #INSERE OS DADOS DO USUARIO NA TABELA 
        self.conn.commit()#Confirma a inserção dos dados

#METODO PARA ALTERAR OS DADOS DE UM USUARIO EXISTENTE NO BANCO DE DADOS
def alterar(self,idUsuario,nome,email,usuario,senha):
    self.cursor.execute("UPDATE usuario1 SET nome = %s,email = %s,usuario = %s,senha = %s WHERE idUsuario = %s",(nome,email,usuario,senha))#Atualiza os dados do usuario com o id fornecido
    self.conn.commit()#Confirma a atualização dos dados


# METODO PARA EXCLUIR USUARIO DO BANCO DE DADOS
def exlcluir (self,idUsuario):
    self.cursor.execute("DELETE FROM usuario1 WHERE idUsuario = %s",(idUsuario,))#Exclui o usuario com o id fornecido
    self.conn.commit()# Confirma a exclusao dos dados

#METODO PARA BUSCAR OS DADOS DE UM USUARIO NO BANCO DE DADOS
def buscar (self,idUsuario):
    self.cursor.execute("SELECT * FROM usuario1 WHERE idUsuario = %s",(idUsuario,))#Seleciona os dados do usuario com id fornecido
    return self.cursor.fetchone()#Retorna os dados do usuario encontrado

#METODO CHAMADO QUANDO A INSTANCIA DA CLASSE É DESTRUIDA
def __del__(self):
    self.conn.close()#Fecha a conexão com o banco de dados 