import sqlite3
from funcionalidades import *
from funcionarios import *
from produtos import *

# Conexão com SGDB
conn = sqlite3.connect("Perfumaria.db")
cursor = conn.cursor()

print("""===============================================
=== Sistema de banco de dados da Perfumaria ===
======= Realize o Login para ter acesso =======
===============================================""")

while True:
    
    login = input("\n(000) para sair\nLogin: ")
    if login == "000":
        break
    senha = input("Senha: ")
    
    try: 
        cursor.execute("SELECT senha FROM funcionario WHERE login='"+login+"'")
        senha_db = cursor.fetchone()
        conn.close
    
        if senha == senha_db[0]:
            print("\nLogin bem sucedido como:", login)
            n = 0
            
            while True:
                esc = input("\n==============================\nO que deseja usar?\n(1) Listagens/consultas de estoque\n(2) Gerência de estoque\n(3) Gerência de funcionários [apenas admin]\n(000) Fazer logout\n\n>> ")
                
                if esc == "1":
                    func()
                    
                elif esc == "2":
                    produtos()
                
                elif (login == "ADMIN") and (esc == "3"):
                    funcionarios()
                
                elif esc == "000":
                    break
                
                else:
                    print("\n!!!Opção inválida!!!")

        else:
            print("\n\nConjunto login e senha inexistente.\nContate o admin do sistema para se cadastrar ou confira os dados e tente novamente.\n")
                
    except: 
        print("\n\nConjunto login e senha inexistente.\nContate o admin do sistema para se cadastrar ou confira os dados e tente novamente.\n")
    
