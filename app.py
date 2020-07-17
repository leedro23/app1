from tkinter import *

menu_inicial = Tk()
menu_inicial.title('Pirata Enterprise LTDA')
menu_inicial['bg'] = 'gray'
menu_inicial.geometry("500x250+200+200")
menu_inicial.resizable(True,True)
#menu_inicial.minsize(500,250)
#menu_inicial.minsize(720,480)
menu_inicial.iconbitmap("images/piratee.ico")

def piraton_click(mensagem):
    print(mensagem)

#botão
btn1 = Button(menu_inicial, text = "Incluir", command=lambda: piraton_click('Nova mensagem'))
btn1.pack()

btn2 = Button(menu_inicial, text = "Consultar", command=lambda: piraton_click('Outra mensagem'))
btn2.pack()

#label
label_1 = Label(menu_inicial, text = 'Item',
                font = 'Arial 15',
                bg = 'gray',
                fg = 'white',
                borderwidth = 5,
                bd = 5,
                relief = 'sunken',
                width = 25,
                height = 2
                ).pack()
#label_1.pack()
label_2 = Label(menu_inicial,
                text = 'Descrição',
                font = 'Arial 15',
                bg = 'gray',
                fg = 'white',
                borderwidth = 5,
                bd = 5,
                relief = 'sunken'
                ).pack()
#label_2.pack()

#pack
#label_1.pack()
#label_2.pack()
btn1.pack()
btn2.pack()

#dimensoes da janela
largura = 500
altura = 300

#resolução do nosso sistema
largura_screen =  menu_inicial.winfo_screenmmwidth()
altura_screen = menu_inicial.winfo_screenwidth()

posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2

#definir a geometry
menu_inicial.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))



print(largura_screen, altura_screen)

menu_inicial.mainloop()

