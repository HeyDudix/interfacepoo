from tkinter import *

teste = Tk()
teste.title("Turmas")#Titulo da página
teste.geometry ('700x400')#Tamanho da página
teste.configure(background="#8CA7C0")#Definindo a cor de fundo

#label é um "rótulo" e o Label é a classe
label = Label(teste, text="Primeiro teste", font = ("Arial Bold", 15), fg='black', bg='white')#Definindo texto, fonte, tamanho da letra, cor da letra e a cor de fundo da letra
label.grid(column=1, row=2)#Definindo posição

def ola():
    resultado=entrada.get()
    label.configure(text=resultado)#Mudando valores do atributo dentra da widget

entrada = Entry(teste, width=10)
entrada.grid(column=2, row=2)
    
#adicionando botão usando a classe Button
botao = Button(teste, text = "Clique!", command = ola)
botao.grid(column=3, row=2, padx=5, pady=15)#Posição
botao = Button(teste, text="Clique!", bg="white", fg="black")#Definindo texto, cor da letra e cor de fundo

teste.mainloop()