from tkinter import *

menu_inicial = Tk()
menu_inicial.title('Pirata Enterprise LTDA')
menu_inicial['bg'] = 'gray'
menu_inicial.geometry("500x250+200+200")
menu_inicial.resizable(True,True)
menu_inicial.minsize(500,250)
menu_inicial.minsize(720,480)
menu_inicial.iconbitmap("images/piratee.ico")

def piraton_click(mensagem):
    print(mensagem)

#botão
btn1 = Button(menu_inicial, text = "Executar", command=lambda: piraton_click('Nova mensagem'))
btn.pack()

btn2 = Button(menu_inicial, text = "Clicar", command=lambda: piraton_click('Outra mensagem'))
btn.pack()





menu_inicial.mainloop()

