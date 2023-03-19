# def soma(a, b):
#     return a + b


# print(soma(1, 2))
# # saída - 3
# print(soma('EFG', ' Luiz Rassi'))
# # saida - EFG Luiz Rassi


# def multiplica(a, b):
#     return a*b


# a = int(input("Diga o primeiro número: "))
# b = int(input("Agora o segundo: "))

# print(multiplica(a, b))

import tkinter

top = tkinter.Tk()


def hello_world():
    l = tkinter.Label(top, text="Hello world!")
    l.pack()


w = tkinter.Button(top, text="Clica em mim!", command=hello_world)
w.pack()

top.mainloop()

