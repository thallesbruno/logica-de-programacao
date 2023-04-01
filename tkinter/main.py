from tkinter import *

janela = Tk()  # cria instância de Tk dentro do objeto janela
janela.title('Cadastro de Cliente')
janela.geometry('600x300')
janela.configure(background='white')

# cria istância de Label dentro do objeto labelArquivo
labelUm = Label(janela,
    text='EFG Luiz Rassi',
    font=('Calibri Bold', 20),
    fg='#ffffff',
    bg='#778899'
    )
labelUm.grid(column=0, row=0)

labelDois = Label(janela,
    text='Endereço: Jd. Buriti Sereno',
    font=('Calibri Bold', 20),
    fg='#ffffff',
    bg='#778899'
    )
labelDois.grid(column = 0, row = 2)

janela.mainloop()
