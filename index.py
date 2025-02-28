#IMPORTAR BIBLIOTECAS
from tkinter import* # Importa todos os módulos do tkinter
from tkinter import messagebox # Importa o módulo de caixas de mensagem do tkinter
from tkinter import ttk # Impottar o módulo de widgets temáticos do tkinter
from DataBase import Database #Importa a classe Database do módulo DataBase

#CRIAR A JANELA
jan = Tk() # Cria uma instanci da janela principal
jan.title("SL Sytens - Painel de Acesso") #Define o título da janela
jan.geometry("600X300") #Define o tamanho da janela
jan.configure(background="white")#Configura a cor de fundo da janela
jan.resizable(width=False,height=False)#Impede que a janela seja redimensionada

# COMANDO PARA DEIXAR A TELA TRANSPARENTE
jan.attributes("-alpha",0.9) #Define a transparencia da janela (0.0 a 1.0)

# DEFINIR ÍCONE DA JANELA
#jan.iconbitmap(default="icons/1LogoIcon.ico") #Define o ícone da janela

# CARREGAR IMAGEM
logo = PhotoImage(file="icons/LogoRafaelMagalhaes.png") #Carrega a imagem da logo

# CRIAR FRAME
LeftFrame = Frame(jan,width=200,height=300,bg="MIDNIGHTBLUE",relief="raise") #Cria um frama à esquerda
LeftFrame.pack(side=LEFT)#Posiciona o frama à direita

# ADICIONAR LOGO
LogoLabel = Label(LeftFrame,image = logo,bg = "MIDBIGHTBLUE") #Cria um label para a image, do logo
LogoLabel.place(x=50,y=100) #Posiciona o label no frama esquerdo 

# ADICIONAR CAMPOS DE USUARIO E SENHA
UsuarioLabel = Label(RightFrame,text = "Usuario: ",font=("Century Gothic",20),bg = "MIDNIGHTBLUE",fg="White")

#=================================
#AQUI PRA BAIXO
#=================================


# Cria um label para o usuario
UsuarioLabel.place(x=5,y=100) #Posiciona o label no frame direito

UsuarioEntry = ttk.Entry(RightFrame,width=30)#Cria um campo de entrada para o usuario
UsuarioEntry.place(x=120,y=115) #Posiciona o campo de entrada

SenhaLabel = Label(RightFrame,text="Senha: ",font=("Century Gothic",20),bg = "MIDNIGHTBLUE",fg = "White")#Cria um label pra senha
SenhaLabel. place(x=5,y=150) #Posiciona o label no frame direito
SenhaEntry = ttk.Entry(RightFrame,width=30,show="°") #Cria um campo de entrada para a senha
SenhaEntry.place(x=120,y=165)#Posiciona o campo de entrada 

# FUNÇÃO DE LOGIN
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

#CRIANDO BOTÕES
LoginButton = ttk.Button(RightFrame,text="LOGIN",width=15,command=Login)#Cria um botão de login
LoginButton.place(x=150,y=225)#Posiciona o botao de login

#FUNÇÃO PARA REGISTRAR NOVO USUARIO
def Registrar():
    # REMOVENDO BOTOES DE LOGIN
    LoginButton.place(x=5000)#Move o botao de login pra fora da tela
    RegisterButton.place(x=5000)#Move o botao de registro pra fora da tela

    #INSERINDO WIDGETS DE CADASTRO
    NomeLabel = Label (RightFrame,text="Nome:",font=("Century Gothic",20),bg="MIDNIGHTBLUE",fg="White")#Cria um label para o nome
    NomeLabel.place(x=5,y=5)#Posiciona label no frame direito
    NomeEntry = ttk.Entry(RightFrame,width=30)#Cria um campo de entrada para o nome
    NomeEntry.place(x=120,y=20)#Posiciona o campo de entrada

    EmailLabel = Label(RightFrame,text="Email:",font=("Century Gothic,20"),bg="MIDNIGHTBLUE",fg="White")#Cria um label para o email
    EmailLabel.place(x=5,y=40)#Posiciona o label no frame direito
    EmailEntry = ttk.Entry(RightFrame,width=30)#Cria um campo de entrada para o email
    EmailEntry.place(x=120,y=55)#Posiciona o campo de entrada

    # FUNÇÃO PARA REGISTRAR NO BANCO DE DADOS
    def RegistrarNoBanco():
        nome = NomeEntry.get() #Obtem o valor do campo de entrada do nome
        email = EmailEntry.get()#Obtem o valor do campo de entrada do email
        usuario = UsuarioEntry.get()#Obtem o valor do campo de entrada do usuario
        senha = SenhaEntry.get()#Obtem o valor do campo de entrada da senha

        #Verifa se todos os campos estao preenchidos
        if nome == "" or email == "" or usuario == "" or senha == "":
            messagebox.showerror(title="Erro de Registro",message="PREENCHA TODOS OS CAMPOS")#Exibe mensagem de erro 
        else:
            db = Database()#Cria uma instancia da classe Database
            db.RegistrarNoBanco(nome,email,usuario,senha)#Chama o metodo para registar no banco de dados
            messagebox.showinfo("Success","Usuario registrado com sucesso!")#Exibe mensagem de sucesso

            #Limpar os campos após o registro
            NomeEntry.delete(0,END)#Limpa o campo de entrada do Nome
            EmailEntry.delete(0,END)#Limpa o campo de entrada do email
            UsuarioEntry.delete(0,END)#Limpa o campo de entrada do usuario
            SenhaEntry.delete(0,END)#Limpa o campo de entrada do senha

        Register = ttk.Button(RightFrame,text="REGISTRAR",width=15,command=RegistrarNoBanco) #Cria um botão de registro
        Register.place(x=150,y=225) #Posiciona o botão de registro



