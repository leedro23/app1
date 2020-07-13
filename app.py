from tkinter import *

menu_inicial = Tk()
menu_inicial.title('Pirata Enterprise LTDA')
menu_inicial['bg'] = 'blue'
menu_inicial.geometry("500x250+200+200")
menu_inicial.resizable(True,True)
menu_inicial.minsize(500,250)
menu_inicial.minsize(720,480)
menu_inicial.iconbitmap("images/piratee.ico")

#botão
btn = Button(menu_inicial, text = "Executar")
btn.pack()





menu_inicial.mainloop()

