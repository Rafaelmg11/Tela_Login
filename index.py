#IMPORTAR BIBLIOTECAS
from tkinter import* #Importa todos os módulos do tkinter
from tkinter import messagebox #Importa o módulo de caixas de mensagem do tkinter
from tkinter import ttk #Impottar o módulo de widgets temáticos do tkinter
from DataBase import Database #Importa a classe Database do módulo DataBase

#CRIAR A JANELA
jan = Tk() #Cria uma instanci da janela principal
jan.title("SL Sytens - Painel de Acesso") #Define o título da janela
jan.geometry("600X300") #Define o tamanho da janela
jan.configure(background="white")#Configura a cor de fundo da janela
jan.resizable(width=False,height=False)#Impede que a janela seja redimensionada

#COMANDO PARA DEIXAR A TELA TRANSPARENTE
jan.attributes("-alpha",0.9) #Define a transparencia da janela (0.0 a 1.0)

#DEFINIR ÍCONE DA JANELA
#jan.iconbitmap(default="icons/1LogoIcon.ico") #Define o ícone da janela

#CARREGAR IMAGEM
logo = PhotoImage(file="icons/LogoRafaelMagalhaes.png") #Carrega a imagem da logo

#CRIAR FRAME
LeftFrame = Frame(jan,width=200,height=300,bg="MIDNIGHTBLUE",relief="raise") #Cria um frama à esquerda
LeftFrame.pack(side=LEFT)#Posiciona o frama à direita

#ADICIONAR LOGO
LogoLabel = Label(LeftFrame,image = logo,bg = "MIDBIGHTBLUE") #Cria um label para a image, do logo
LogoLabel.place(x=50,y=100) #Posiciona o label no frama esquerdo 

#ADICIONAR CAMPOS DE USUARIO E SENHA
UsuarioLabel = Label(RightFrame,text = "Usuario: ",font=("Century Gothic",20),bg = "MIDNIGHTBLUE",fg="White")

#=================================
#AQUI PRA BAIXO
#=================================


#Cria um label para o usuario
UsuarioLabel.place(x=5,y=100) #Posiciona o label no frame direito

UsuarioEntry = ttk.Entry(RightFrame,width=30)#Cria um campo de entrada para o usuario
UsuarioEntry.place(x=120,y=115) #Posiciona o campo de entrada

SenhaLabel = Label(RightFrame,text="Senha: ",font=("Century Gothic",20),bg = "MIDNIGHTBLUE",fg = "White")#Cria um label pra senha
SenhaLabel. place(x=5,y=150) #Posiciona o label no frame direito
SenhaEntry = ttk.Entry(RightFrame,width=30,show="°") #Cria um campo de entrada para a senha
SenhaEntry.place(x=120,y=165)#Posiciona o campo de entrada 
#FUNÇÃO DE LOGIN
def Login():
    usuario = UsuarioEntry.get()#Obtém o valor do campo de texto de entrada do usuario
    senha = SenhaEntry.get() #Obtém o valor do campo de entrada da senha

    #Conectar o banco de dados
    db = Database() #Cria uma instancia da classe Database
    db.cursor.execute("""
    SELECT*FROM usuario WHERE usuario = %s AND senha = %s""",(usuario,senha))#Executa a consulta SQL para verificar o usuário e a senha
    VerifyLogin = db.cursor.fetchone() #Obtem o resultado da consulta

    #Verificar se o usuario foi encontrado

    if VerifyLogin:
        messagebox.showinfo(title = "INFO LOGIN",message="Acesso Confirmado, Bem Vindo!")#Ebibe mensagem de sucesso
        
    else:messagebox.showinfo(title = "INFO LOGIN",message = "Acesso Negado. Verifique se está cadastrado no Sistema!")#Exibe mensagem de erro

#FUNÇÃO PARA REGISTRAR NOVO USUÁRIO
    def