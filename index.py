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