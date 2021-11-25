import sqlite3
# Conexão com SGDB
conn = sqlite3.connect("Perfumaria.db")
cursor = conn.cursor()

erro_p = "\n!!!ERRO!!!\nVerifique se os dados inseridos obedecem os parâmetros:\n-Código do produto deve ser único\n-Nome do produto não pode estar vazio ou em branco\n-Não pode ser cadastrado produto com saldo negativo\n-Não pode ser cadastrado produto com saldo mínimo negativo.\n"

def produtos():
    while True:
        # Entrada de dados para serem cadastrados
        print("\nCadastro de produtos\n==============================")
        codprod = input("(000 para voltar)\nCódigo: ")
        
        if codprod == "000":
            break
        
        try:
            cursor.execute("SELECT count(*), dsprod, saldo, sldmin, prvenda, prcusto FROM produto WHERE codprod = " + codprod)
            rs = cursor.fetchone()
            conn.close
            
            if rs[0] > 0:
                print("\nCódigo de produto já cadastrado!\nDescrição:", rs[1],"\nSaldo:", rs[2],"\nSaldo mínimo:", rs[3],"\nPreço de custo:", rs[5],"\nPreço de venda:", rs[4])
                
                op = input("\nDeseja (alt)erar ou (exc)luir o produto?\n(000) Para voltar sem alterar\n>> ").lower()
            
                if op == "alt":
                    
                    while True:
                        
                        try: 
                            n_dsprod = input("\nNova descrição:")
                            n_saldo = float(input("Novo saldo:"))
                            n_sldmin = float(input("Novo saldo mínimo:"))
                            n_prcusto = float(input("Novo preço de custo:"))
                            n_prvenda = float(input("Novo preço de venda:"))
                            
                            if not((n_dsprod == "") or (n_saldo < 0) or (n_sldmin < 0)):
                                break
                            
                            else:
                                print(erro_p)
                                
                        except:
                            print(erro_p)
                    
                    try: 
                        cursor.execute("UPDATE produto SET dsprod = '"+n_dsprod+"', saldo = "+str(n_saldo)+", sldmin = "+str(n_sldmin)+", prvenda = "+str(n_prvenda)+", prcusto = "+str(n_prcusto)+" WHERE codprod = "+codprod+";")
                        conn.commit()
                        conn.close
                        print("\nAlterações de produto realizadas com sucesso!")
                        
                    except:
                        print("\n!!!\nErro na comunicação com o banco de dados. Verifique se os dados inseridos obedecem os parâmetros.\n!!!\n")
                    
                elif op == "exc":
                    print("Tem certeza que deseja excluir o Produto '", rs[1],"' de código:", codprod, "?")
                    opc = input("\n[Sim/N]>> ").lower()
                    
                    if opc == "sim":

                        try: 
                            cursor.execute("DELETE FROM produto WHERE codprod = "+codprod+";")
                            conn.commit()
                            conn.close
                            print("\nProduto excluido com sucesso!")
                            
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
            
            while True:
                try:
                    dsprod = input("Descrição:")
                    saldo = float(input("Saldo:"))
                    sldmin = float(input("Saldo mínimo:"))
                    prcusto = float(input("Preço de custo:"))
                    prvenda = float(input("Preço de venda:"))
                    
                    if not((dsprod == "") or (saldo < 0) or (sldmin < 0)):
                        break
                    else:
                        print(erro_p)
                        
                except:
                    print(erro_p)
                            
            try: 
                cursor.execute("INSERT INTO produto (codprod, dsprod, saldo, sldmin, prvenda, prcusto) VALUES ("+codprod+","+"'"+dsprod+"'"+","+str(saldo)+","+str(sldmin)+","+str(prcusto)+","+str(prvenda)+");")
                conn.commit()
                conn.close
                print("\nProduto cadastrado com sucesso!")
            
            except:
                print(erro_p, "\nOu possível erro na comunicação com o banco de dados.")
                        
                
        except:
            print("\n!!!\nErro na comunicação com o banco de dados.\nVerifique se o código do produto digitado é um número válido.\nSe tudo estiver correto, verifique a disponibilidade e conexão com o banco de dados.\n!!!\n")
