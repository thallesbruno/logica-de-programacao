from tkinter import *


class Application:
    def __init__(self, master=None):
        self.HebeCamargoFrame = Frame(master)
        self.HebeCamargoFrame.pack()
        self.CazuzaMensagem = Label(self.HebeCamargoFrame, text="Vestido de bolinha")
        self.CazuzaMensagem["font"] = ("Verdana", "20", "italic", "bold")
        self.CazuzaMensagem['bg'] = ('#BEBEBE')
        self.CazuzaMensagem.pack()
        self.sair = Button(self.HebeCamargoFrame)
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Verdana", "10")
        self.sair["width"] = 5
        # self.sair["command"] = self.HebeCamargoFrame.quit
        self.sair.bind("<Button-1>", self.mudar_texto)
        self.sair.pack(side=LEFT)
        self.widget2 = Frame(master)
        self.widget2.pack(side=RIGHT)
        self.msg2 = Label(self.HebeCamargoFrame, text="Primeiro widget")
        self.msg2["font"] = ("Arial", "12", "italic", "bold")
        self.msg2['bg'] = ('#1C6118')
        self.msg2.pack(side=RIGHT)

    def mudar_texto(self, event):
        if self.CazuzaMensagem['text'] == "Primeiro widget":
            self.CazuzaMensagem['text'] = "Botão foi pressionado"
            self.CazuzaMensagem['bg'] = ('white')
        else:
            self.CazuzaMensagem['text'] = "Primeiro widget"


root = Tk()
root.geometry('250x150+300+300')
Application(root)
root.mainloop()
