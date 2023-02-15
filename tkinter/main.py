from tkinter import *

janela = Tk() # cria instância de Tk dentro do objeto janela
janela.title('Cadastro de Cliente')

janela.geometry('300x300')
janela.configure(background='#B0C4DE')

# cria istância de Label dentro do objeto labelArquivo
labelUm = Label(janela, 
    text='Label Teste 1',
    font=('Arial Bold', 20),
    fg='#ffffff',
    bg='#778899'
    )
labelUm.grid(column=0, row=0)

labelDois = Label(janela, text='Label Teste 2')
labelDois.grid(column=1, row=0)

janela.mainloop()