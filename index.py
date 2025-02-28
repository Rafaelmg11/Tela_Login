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

#Cria um label para o usuario
UsuarioLabel.place(x=5,y=100) #Posiciona o label no frame direito

UsuarioEntry = ttk.Entry(RightFrame,width=30)#Cria um campo de entrada para o usuario
UsuarioEntry.place(x=120,y=115) #Posiciona o campo de entrada

SenhaLabel = Label(RightFrame,text="Senha: ",font=("Century Gothic",20),bg = "MIDNIGHTBLUE",fg = "White")

#Cria um label para a senha
SenhaLabel.place(x=5,y=150) #Posiciona o campo de entrada

#FUNÇÃO DE LOGIN