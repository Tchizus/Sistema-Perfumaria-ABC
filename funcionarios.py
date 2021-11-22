import sqlite3
# Conexão com SGDB
conn = sqlite3.connect("Perfumaria.db")
cursor = conn.cursor()

def funcionarios():
    while True:
        # Entrada de dados para serem cadastrados
        print("\nGerenciamento de funcionários\n================================")
        cpf = input("(000 para voltar)\nCPF: ")
        
        if cpf == "000":
            break
        
        try:
            cursor.execute("SELECT count(*), cpf, dsnome, login FROM funcionario WHERE cpf = " + cpf)
            rs = cursor.fetchone()
            conn.close
            
            if rs[0] > 0:
                print("\nFuncionario já cadastrado!\nCPF:", rs[1],"\nNome:", rs[2],"\nLogin:", rs[3])
                
                op = input("\nDeseja (alt)erar ou (exc)luir o usuário?\n(000) Para voltar sem alterar\n>> ").lower()
                
                if op == "alt":
                    user = input("Novo login:")
                    passw = input("Nova senha:")

                    try: 
                        cursor.execute("UPDATE funcionario SET login = '"+user+"', senha = '"+passw+"' WHERE cpf = "+cpf+";")
                        conn.commit()
                        conn.close
                        print("\nAlterações de cadastrado realizadas com sucesso!")
                        
                    except:
                        print("\n!!!\nErro na comunicação com o banco de dados. Verifique se os dados inseridos obedecem os parâmetros.\n!!!\n")
                    
                elif op == "exc":
                    print("Tem certeza que deseja excluir o funcionário", rs[2], "de CPF:", rs[1], "?")
                    opc = input("\n[Sim/N]>> ").lower()
                    
                    if opc == "sim":

                        try: 
                            cursor.execute("DELETE FROM funcionario WHERE cpf = "+cpf+";")
                            conn.commit()
                            conn.close
                            print("\nFuncionário excluido com sucesso!")
                            
                        except:
                            print("\n!!!\nErro na comunicação com o banco de dados. Verifique se os dados inseridos obedecem os parâmetros.\n!!!\n")
                    
                    elif opc == "n":
                        continue
                    else:
                        print("\nOpção inválida!")
                
                elif op == "000":
                    break
                else:
                    print("\nOpção inválida!")
                
                continue
            
            dsnome = input("Nome:")
            user = input("Login:")
            passw = input("Senha:")

            try: 
                cursor.execute("INSERT INTO funcionario (cpf, dsnome, login, senha) VALUES ("+cpf+","+"'"+dsnome+"'"+","+"'"+user+"'"+","+"'"+passw+"'"");")
                conn.commit()
                conn.close
                print("\nFuncionário cadastrado com sucesso!")
                
            except:
                print("\n!!!\nErro na comunicação com o banco de dados. Verifique se os dados inseridos obedecem os parâmetros.\n!!!\n")
        
        except:
            print("\n!!!\nErro na comunicação com o banco de dados.\nVerifique se os dados inseridos obedecem os parâmetros\nSe tudo estiver correto, verifique a disponibilidade e conexão com o banco de dados.\n!!!\n")
