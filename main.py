from tkinter import *
from  tkinter import ttk
import os
import mysql.connector as sql
import pymysql


pymysql.install_as_MySQLdb()



app = Tk()
app.title("DanPDV")
app.geometry("1000x600")
app.resizable(False, False)
app.config(bg="red")

title = Label(app, text="DanPDV", bg="red", fg="yellow", font="Arial 36 bold italic").place(x=0, y=0)
app.attributes("-fullscreen", True)
i=10000
total = 0
########input
def adc():
    global lista
    global total

    print(cod_text.get())
    qt = qtd_text.get()
    price = pre_text.get()

    preco_prod = float(qt) * float(price)


    total += float(qt) * float(price)
    preco["text"] = "R$",total
    
    liss = lista.insert(i, cod_text.get() + "                                             "  + "R$" + str(preco_prod))

    #Fazer area de troco

def troco():
    global total
    pago = pg_text.get()

    qt = qtd_text.get()
    price = pre_text.get()


    tr = float(pago) - float(total)

    preco_troco["text"] = "R$",tr

    
cod = Label(app, text="Digite o nome ou codigo: ", bg="red",
            fg="yellow", font="Arial 12 bold").place(x=1000, y=100)
cod_text = Entry(width= 40)
cod_text.place(x=1000, y=140)

    #global preco
    #global textx
    #preco.config(text=textx)

qtd = Label(app, text="Quantidade: ", bg="red",
            fg="yellow", font="Arial 12 bold").place(x=1000, y=180)
qtd_text = Entry(width= 40)
qtd_text.place(x=1000, y=220)


################

pre = Label(app, text="Preço: ", bg="red",
            fg="yellow", font="Arial 12 bold").place(x=1000, y=260)
pre_text = Entry(width= 40)
pre_text.place(x=1000, y=300)

################

pg = Label(app, text="Valor pago: ", bg="red",
            fg="yellow", font="Arial 12 bold").place(x=1000, y=400)
pg_text = Entry(app, width= 40)
pg_text.place(x=1000, y=440)

pg_bt = Button(app, text="Conferir", bg="white", font=35, height=1,
             width=26, command=troco).place(x=1000, y=490)


#textx= "carro"
    
    


adc = Button(app, text="Adicionar", bg="white", font=35, height=1,
             width=26, command=adc).place(x=1000, y=360)


########

traco = " -----------------------------------------------------------------------------------------------------------------"


#LISTA
lista = Listbox(app, height = 20,width = 85,bg = "white",activestyle = 'dotbox',
                  font = "Arial 12")
#lista.insert(1, "XXX" + traco)
#lista.insert(2, "XXX" + traco)
#lista.insert(3, "XXX" + traco)

lista.place(x=200, y=100)

########## pagar

def deletar():
    lista.delete(0,END)
    app.destroy()
    os.popen("main.py")

def conc():
    global total
    
    con = sql.connect(host="localhost", user="root",
                            password="META100Kk#", database="mercado")
    cur = con.cursor()
    query = "INSERT INTO venda(id, valor) VALUES(null, %s)"
    val = ((total,))
    cur.execute(query, val)
    con.commit()
    con.close()
    print(total)

pag = Label(app, text="Total:", bg="red",fg="yellow", font="Arial 15").place(x=200, y=500)
preco = Label(app, text="R$00,00", bg="red",fg="yellow", font="Arial 25 bold italic")
preco.place(x=200, y=540)
troco = Label(app, text="Troco:", bg="red",fg="yellow", font="Arial 15").place(x=800, y=500)
preco_troco = Label(app, text="R$00,00", bg="red",fg="yellow", font="Arial 25 bold italic")
preco_troco.place(x=800, y=540)

##########


def produto():
    global n_text
    global code_text
    global pre_text
    
    app2 = Tk()
    app2.geometry("1000x600")
    app2.title("Produtos")
    app2.config(bg="red")

    title = Label(app2, text="Produtos", bg="red", fg="yellow", font="Arial 36 bold italic").place(x=0, y=0)

    lista = Label(app2, text="Lista", bg="red", fg="yellow", font="Arial 20").pack()#place(x=0, y=100)


    criar = Label(app2, text="Criar", bg="red", fg="yellow", font="Arial 20 bold").place(x=10, y=80)
    n = Label(app2, text="Nome", bg="red", fg="yellow", font="Arial 10 ").place(x=10, y=120)
    n_text= Entry(app2, width=40)
    n_text.place(x=10,y=140)
    code = Label(app2, text="Codigo", bg="red", fg="yellow", font="Arial 10 ").place(x=10, y=160)
    code_text= Entry(app2, width=40)
    code_text.place(x=10,y=180)
    pre = Label(app2, text="Preço", bg="red", fg="yellow", font="Arial 10 ").place(x=10, y=200)
    pre_text= Entry(app2, width=40)
    pre_text.place(x=10,y=220)

    def criar():
        name = n_text.get()
        cod = code_text.get()
        pr = pre_text.get()
        
        con = sql.connect(host="localhost", user="root",
                          password="META100Kk#", database="mercado")
        cur = con.cursor()
        query = "INSERT INTO produtos(id, nome, preco, codigo) VALUES(null, %s, %s, %s)"
        val = (name, cod, pr)
        cur.execute(query, val)
        con.commit()
        con.close()
        

    adc = Button(app2, text="Adicionar", bg="white", font=35, height=1,
             width=26, command=criar).place(x=10, y=260)

    Label(app2, height=18, bg="red").pack()

    

    tabela = Frame(app2)
    tabela.pack(anchor="center")

    table = ttk.Treeview(tabela)

    #table["columns"] = ("1", "2", "3","4","5")
  
# Defining heading
    table['show'] = 'headings'

    table["columns"] = ("id", "Nome", "Preço", "Codigo")
    table.column("#0", width=0, stretch=NO)
    table.column("id", anchor=CENTER, width=150)
    table.column("Nome", anchor=CENTER, width=150)
    table.column("Preço", anchor=CENTER, width=150)
    table.column("Codigo", anchor=CENTER, width=150)

    table.heading("#0", text="", anchor=CENTER)
    table.heading("id", text="ID", anchor=CENTER)
    table.heading("Nome", text="Nome", anchor=CENTER)
    table.heading("Preço", text="Preço", anchor=CENTER)
    table.heading("Codigo", text="Codigo", anchor=CENTER)

    # DADOS
    con = sql.connect(host="localhost", user="root",
                  password="META100Kk#", database="mercado")
    cur = con.cursor()
    cur.execute("SELECT * FROM produtos")

    ########
    i = 0
    for ro in cur:
        table.insert("", i, text="", values=(ro[i], ro[1], ro[2], ro[3]))
        i = i + 1
    table.pack()

    app2.mainloop()

    

def vendas():
    app3 = Tk()
    app3.geometry("1000x600")
    app3.title("Vendas")
    app3.config(bg="red")

    title = Label(app3, text="Vendas", bg="red", fg="yellow", font="Arial 36 bold italic").place(x=0, y=0)

    lista = Label(app3, text="Lista", bg="red", fg="yellow", font="Arial 20").pack()

    Label(app3, height=5, bg="red").pack()
    

    tabela = Frame(app3)
    tabela.pack(anchor="center")

    table = ttk.Treeview(tabela, height=20)

    table["columns"] = ("id", "Valor")
    table.column("#0", width=0, stretch=NO)
    table.column("id", anchor=CENTER, width=140)
    #table.column("CPF", anchor=CENTER, width=140)
    #table.column("Produtos", anchor=CENTER, width=140)
    table.column("Valor", anchor=CENTER, width=140)

    table.heading("#0", text="", anchor=CENTER)
    table.heading("id", text="ID", anchor=CENTER)
    #table.heading("CPF", text="CPF", anchor=CENTER)
    #table.heading("Produtos", text="Produtos", anchor=CENTER)
    table.heading("Valor", text="Valor", anchor=CENTER)

    # DADOS

    con = sql.connect(host="localhost", user="root",
                  password="META100Kk#", database="mercado")
    cur = con.cursor()
    cur.execute("SELECT * FROM vendas")

    ########
    i = 0
    for dt in cur:
        table.insert("", "end", iid=dt[0],text=dt[0],
                     values=(dt[0], dt[1]))
        i = i + 1
    
    table.pack()
    app3.mainloop()


pro = Button(app, text="Produtos", bg="white", font=35, height=2, width=20
             ,command=produto).place(x=0, y=100)
lis = Button(app, text="Vendas", bg="white", font=35, height=2, width=20
             ,command=vendas).place(x=0, y=150)

v = Label(app, text="v1.0.0", bg="red", fg="yellow", font="Arial 10").place(x=0, y=580)

'''
forma_pag = Label(app, text="Forma de pagamento:", font="Arial 12", fg="yellow", bg="red")
forma_pag.place(x=0, y=280)
'''

selecao = StringVar()




####################
def calc():
    os.startfile("C:\Windows\System32\calc.exe")

cal = Button(app, text="Calculadora", bg="white", font=35, height=2
             , width=20, command= calc).place(x=780, y=0)

####################


'''
def vista():
    

def card():
    print("Cartão")

    
# SE FOR A VISTA DESC, SE CARTAO , NAO
vista = Radiobutton(app, text='A vista', value='vist', variable=selecao,
                    bg="red", fg="yellow", command=vista).place(x=0, y=300)
card = Radiobutton(app, text='Cartão', value='cards', variable=selecao,
                    bg="red", fg="yellow", command=card).place(x=90, y=300)
'''
conc = Button(app, text="Concluir", bg="white", font=35, height=2, width=20,
              command=conc).place(x=0, y=385)
limp = Button(app, text="Limpar", bg="white", font=35, height=2, width=20,
              command=deletar).place(x=0, y=435)

# Tela do usuario
# Criação de produtos
# Lista de compras


app.mainloop()
