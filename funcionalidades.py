import sqlite3
# Conexão com SGDB
conn = sqlite3.connect("Perfumaria.db")
cursor = conn.cursor()

def func():
        
    while True:
        op = input("""\nO que desseja fazer?\n==============================
(A) Listar nome e preço de vendados produtos em ordem alfabética pelo nome.
(B) Listar código, nome, saldo em estoque e saldo mínimo de um produto identificado pelo seu código.
(C) Listar código, nome, saldo em estoque e saldomínimo de todos os produtos cujo saldo em estoque esteja menor que o mínimo.
(D) Listar código, nome, saldo em estoque e saldo mínimo dos produtos cujo saldo em estoque seja menor que o mínimo, e que tenha preço de venda maior que zero.
(E) Listar código, nome, saldo em estoque e saldomínimo dos produtos com saldo em estoque menor que o mínimo e preço de custo maior que zero.
(F) Listar código, nome, saldo em estoque e saldo mínimo dos produtos com saldo em  estoque menor que o mínimo e preço de venda maior que zero, em ordem alfabética por nome.
(G) Listar código e nome de todos os produtos que estão com preço de venda menor ou igual a zero.
(H) Informar quantos produtos estão cadastrados.
(I) Informar quantos produtos estão com saldo em estoque zerado.
(J) Informar quantos produtos estão com saldo em estoque menor que o mínimo.
(K) Informar o nome do produto, saldo em estoque, preço de venda e a previsão de rentabilidade com a venda de cada produto.\n(000) Voltar\n\n>> """).lower()
        
        if op == "a":
            a()
        elif op == "b":
            x = input("Código do produto: ")
            b(x)
        elif op == "c":
            c()
        elif op == "d":
            d()
        elif op == "e":
            e()
        elif op == "f":
            f()
        elif op == "g":
            g()
        elif op == "h":
            h()
        elif op == "i":
            i()
        elif op == "j":
            j()
        elif op == "k":
            k()
        elif op == "000":
            break
        else:
            print("\nOpção inválida. Tente novamente")

#--a SELECT dsprod, prvenda from Produto ORDER by dsprod; 
def a():
    
    try:  
        cursor.execute("SELECT dsprod, prvenda from Produto ORDER by dsprod;")
        resp = cursor.fetchall()
        conn.close
            
        for u in resp:
            print("====================================\nProduto:", u[0], "\nPreço de venda:", u[1])
                
    except:
        print("Erro na comunicação com o banco de dados.")
        
#--b SELECT codprod, dsprod, saldo, sldmin from Produto WHERE codprod = 264; 
def b(x):
    
    try: 
        cursor.execute("SELECT codprod, dsprod, saldo, sldmin from Produto WHERE codprod = "+str(x)+";")
        resp = cursor.fetchone()
        conn.close
        
        print("Código:", resp[0],"\nDescrição:", resp[1],"\nSaldo:", resp[2],"\nSaldo mínimo:", resp[3])

    except:
        print("Erro na comunicação com o banco de dados.\nTalvez seu código não seja válido.")

#--c SELECT codprod, dsprod, saldo, sldmin from Produto WHERE saldo < sldmin; 
def c():
    
    try:  
        cursor.execute("SELECT codprod, dsprod, saldo, sldmin from Produto WHERE saldo < sldmin;")
        resp = cursor.fetchall()
        conn.close
            
        for u in resp:
            print("====================================\nCódigo:", u[0],"\nDescrição:", u[1],"\nSaldo:", u[2],"\nSaldo mínimo:", u[3])
                
    except:
        print("Erro na comunicação com o banco de dados.")

#--d SELECT codprod, dsprod, saldo, sldmin from Produto WHERE saldo < sldmin AND prvenda > 0; 
def d():
    
    try:  
        cursor.execute("SELECT codprod, dsprod, saldo, sldmin from Produto WHERE saldo < sldmin AND prvenda > 0;")
        resp = cursor.fetchall()
        conn.close
            
        for u in resp:
            print("====================================\nCódigo:", u[0],"\nDescrição:", u[1],"\nSaldo:", u[2],"\nSaldo mínimo:", u[3])
                
    except:
        print("Erro na comunicação com o banco de dados.")

#--e SELECT codprod, dsprod, saldo, sldmin from Produto WHERE saldo < sldmin AND prvenda < 0; 
def e():
    
    try:  
        cursor.execute("SELECT codprod, dsprod, saldo, sldmin from Produto WHERE saldo < sldmin AND prvenda < 0;")
        resp = cursor.fetchall()
        conn.close
            
        for u in resp:
            print("====================================\nCódigo:", u[0],"\nDescrição:", u[1],"\nSaldo:", u[2],"\nSaldo mínimo:", u[3])
                
    except:
        print("Erro na comunicação com o banco de dados.")

#--f SELECT codprod, dsprod, saldo, sldmin from Produto WHERE saldo < sldmin AND prvenda < 0 ORDER by dsprod; 
def f():
    
    try:  
        cursor.execute("SELECT codprod, dsprod, saldo, sldmin from Produto WHERE saldo < sldmin AND prvenda < 0 ORDER by dsprod;")
        resp = cursor.fetchall()
        conn.close
            
        for u in resp:
            print("====================================\nCódigo:", u[0],"\nDescrição:", u[1],"\nSaldo:", u[2],"\nSaldo mínimo:", u[3])
                
    except:
        print("Erro na comunicação com o banco de dados.")

#--g SELECT codprod, dsprod,prvenda FROM Produto WHERE prvenda <= 0; 
def g():
    
    try:  
        cursor.execute("SELECT codprod, dsprod,prvenda FROM Produto WHERE prvenda <= 0;")
        resp = cursor.fetchall()
        conn.close
            
        for u in resp:
            print("====================================\nCódigo:", u[0],"\nDescrição:", u[1],"\nPreço de venda:", u[2])
                
    except:
        print("Erro na comunicação com o banco de dados.")

#--h SELECT count (*) AS Cadastrados FROM Produto; 
def h():
    
    try:  
        cursor.execute("SELECT count (*) FROM Produto;")
        resp = cursor.fetchone()
        conn.close
            
        print("Há", resp[0], "produtos cadastrados.")
                
    except:
        print("Erro na comunicação com o banco de dados.")

#--i SELECT count(*) FROM Produto WHERE saldo = 0; 
def i():
    
    try:  
        cursor.execute("SELECT count(*) FROM Produto WHERE saldo = 0;")
        resp = cursor.fetchone()
        conn.close
            
        print("Há", resp[0], "produtos cadastrados com estoque zerado.")
                
    except:
        print("Erro na comunicação com o banco de dados.")

#--j SELECT count(*) FROM Produto WHERE saldo < sldmin; 
def j():
    
    try:  
        cursor.execute("SELECT count(*) FROM Produto WHERE saldo < sldmin;")
        resp = cursor.fetchone()
        conn.close
            
        print("Há", resp[0], "produtos cadastrados com estoque abaixo do mínimo.")
                
    except:
        print("Erro na comunicação com o banco de dados.")

#--k SELECT dsprod, saldo, prvenda, (saldo * prvenda) AS Rentabilidade FROM produto; 
def k():
 
    try:
        cursor.execute("SELECT dsprod, saldo, prvenda, (saldo * prvenda) FROM produto;")
        resp = cursor.fetchall()
        conn.close
        
        for u in resp:
            print("====================================\nDescrição:", u[0],"\nSaldo:", u[1],"\nPreço de venda:", u[2], "\nRentabilidade:", u[3])
    
    except:
        print("Erro na comunicação com o banco de dados.")

