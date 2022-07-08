from classes.cls_carro import Carro
from classes.cls_moto import Moto
from classes.cls_triciclo import Triciclo
from classes.cls_camionete import Camionete
from classes.data.data_array import lista_carros, lista_motos, lista_camionetes, lista_triciclos

import time
import sys


carro_1 = Carro("05/05/1978", "Supra", "GDFG-5466", 15000, "0", "Preta")
carro_2 = Carro("01/01/1980", "RX-7", "KJDO-0981", 15600, "0", "Azul")
carro_3 = Carro("24/01/1998", "Mustang", "XVXC-4564", 35100, "0", "Vermelho")


moto_1 = Moto("11/05/1999", "Kawasaki Ninja", "POSD-3422", 32000, "0", "Verde")
moto_2 = Moto("06/01/2012", "Falcon", "WAQE-9871", 9000, "0", "Preta")
moto_3 = Moto("06/01/2012", "Yamaha 150", "CESR-1998", 10000, "0", "Azul")

camionete_1 = Camionete("12/05/2000", "Toyota", "KODF-0231", 32000, "0")
camionete_2 = Camionete("09/12/1999", "Nissan", "TREU-4957", 29000, "0")
camionete_3 = Camionete("07/05/2002", "Mercedes-Benz", "BREN-2002", 7052002, "0")

triciclo_1 = Triciclo("25/01/2021", "Caloi", "QWAS-5441", 1000, "0", "Vermelho")
triciclo_2 = Triciclo("20/03/1992", "Cannondale", "ZXZD-4232", 700, "0", "Branca")


lista_carros.append(carro_1.__dict__)
lista_carros.append(carro_2.__dict__)
lista_carros.append(carro_3.__dict__)

lista_motos.append(moto_1.__dict__)
lista_motos.append(moto_2.__dict__)
lista_motos.append(moto_3.__dict__)

lista_camionetes.append(camionete_1.__dict__)
lista_camionetes.append(camionete_2.__dict__)
lista_camionetes.append(camionete_3.__dict__)

lista_triciclos.append(triciclo_1.__dict__)
lista_triciclos.append(triciclo_2.__dict__)


nome_cliente = str(input("Digite o seu nome: "))


if nome_cliente == "":
    print("Não deixe seu nome em branco.")
    sys.exit()


while True:

    opcao = input(f"""
        _______________________________________________________________
       |         __   ___                       __        __           |
       |        |  \ |__  \  /      | |\ |     /  `  /\  |__)          |
       |        |__/ |___  \/       | | \|     \__, /~~\ |  \          |
       |                                                               |     
                            Bem-vindo(a) {nome_cliente} !                                  
       |                                                               |
       |                                                               |     
       |                                                               |
       |_______________________________________________________________|
       |                                                               | 
       | [1] Mostrar Motos/Triciclo                                    |             
       |                                                               | 
       | [2] Mostrar Carros                                            |     
       |                                                               | 
       | [3] Mostrar Camionetes                                        | 
       |                                                               | 
       | [4] Mostrar Todos                                             | 
       |                                                               | 
       | [5] Veículos Disponíveis                                      | 
       |                                                               | 
       | [6] Veículos Vendidos                                         | 
       |                                                               | 
       | [7] Veículos vendido com o menor preço                        | 
       |                                                               | 
       | [8] Veículos vendido com o maior preço                        | 
       |                                                               | 
       | [0] Sair                                                      | 
       |_______________________________________________________________| 
       |                                                               | 
       |                                                               | 
         Digite sua opção: """)

    if opcao == '1':

        for x in lista_motos:
            print(f"""
            Moto: {x['nome']}
            Placa: {x["placa"]}
            Valor: R$ {x["valor"]:.2f}
            Cor: {x["cor"]}
            Data de Fabricação: {x['data_fabricacao']}
            """)
        
        for x in lista_triciclos:
            print(f"""
            Triciclo: {x['nome']}
            Placa: {x["placa"]}
            Valor: R$ {x["valor"]:.2f}
            Cor: {x["cor"]}
            Data de Fabricação: {x['data_fabricacao']}
            """)

    elif opcao == '2':
        for x in lista_carros:
            print(f"""
            Carro: {x['nome']}
            Placa: {x["placa"]}
            Valor: R$ {x["valor"]:.2f}
            Cor: {x["cor"]}
            Data de Fabricação: {x['data_fabricacao']}
            """)

    elif opcao == '3':

        for x in lista_camionetes:
            print(f"""
                Camionetes: {x['nome']}
                Placa: {x["placa"]}
                Valor: R$ {x["valor"]:.2f}
                Cor: {x["cor"]}
                Data de Fabricação: {x['data_fabricacao']}
                """)

    elif opcao == '4':
        print('---'*10)

        for x in lista_carros:
            print(f"""
            Carro: {x['nome']}
            Placa: {x["placa"]}
            Valor: R$ {x["valor"]:.2f}
            Cor: {x["cor"]}
            Data de Fabricação: {x['data_fabricacao']}
            """)
        
        print('---'*10)

        for x in lista_motos:
            print(f"""
            Moto: {x['nome']}
            Placa: {x["placa"]}
            Valor: R$ {x["valor"]:.2f}
            Cor: {x["cor"]}
            Data de Fabricação: {x['data_fabricacao']}
            """)

        print('---'*10)

        for x in lista_camionetes:
            print(f"""
                Camionetes: {x['nome']}
                Placa: {x["placa"]}
                Valor: R$ {x["valor"]:.2f}
                Cor: {x["cor"]}
                Data de Fabricação: {x['data_fabricacao']}
                """)

        print('---'*10)

        for x in lista_triciclos:
            print(f"""
            Triciclo: {x['nome']}
            Placa: {x["placa"]}
            Valor: R$ {x["valor"]:.2f}
            Cor: {x["cor"]}
            Data de Fabricação: {x['data_fabricacao']}
            """)

        print('---'*10)
        time.sleep(5)

    elif opcao == '5':
        
        # Carros
        x = ["Carros Disponiveis: " + x['nome'] + " Placa: " + x['placa'] for x in lista_carros if x['vendido'] == False]

        if x != []:
            print(x)

        elif x == []:
            print("Não temos carros disponiveis. :(")
        

        # Motos
        y = ["Motos Disponiveis: " + y['nome'] + " Placa: " + y['placa'] for y in lista_motos if y['vendido'] == False]

        if y != []:
            print(y)

        elif y == []:
            print("Não temos motos disponiveis. :(")
        
        # Triciclos
        z = ["Triciclos Disponiveis: " + z['nome'] + " Placa: " + z['placa'] for z in lista_triciclos if z['vendido'] == False]

        if z != []:
            print(z)

        elif z == []:
            print("Não temos triciclos disponiveis. :(")
        

        # Camionetes
        h = ["Camionetes Disponiveis: " + h['nome'] + " Placa: " + h['placa'] for h in lista_camionetes if h['vendido'] == False]

        if h != []:
            print(h)

        elif h == []:
            print("Não temos camionetes disponiveis. :(")
        
        ################## 
        # Parte de comprar algum veículo disponível.
        ##################

        s_ou_n = str(input("Deseja comprar algum desses carros? (s/n): "))
        s_ou_n.lower()

        if s_ou_n == "n":
            print("Que pena :( , espero que aproveite a estadia! :D")
            time.sleep(1.5)
            continue
        
        elif s_ou_n == "s":
            
            num_opcao = input("""
        ------------ [1] Carro
        ------------ [2] Moto
        ------------ [3] Camionete
        ------------ [4] Triciclo
        ------------ [0] Sair


        ------------ Baseado nessas opções, digite de acordo com seu desejo:
        -> """)

            if num_opcao == '1':
                Carro.vender_veiculo()

            elif num_opcao == '2':
                Moto.vender_veiculo()

            elif num_opcao == '3':
                Camionete.vender_veiculo()

            elif num_opcao == '4':
                Triciclo.vender_veiculo()

            elif num_opcao == '0':
                pass

            else:
                print("Digite apenas uma das opções!")

    elif opcao == '6':
        # Carros
        x = ["Carros Vendidos: " + x['nome'] + " Placa: " + x['placa'] + "CPF Comprador: " + x['cpf_comprador'] for x in lista_carros if x['vendido'] == True]

        if x != []:
            print(x)

        elif x == []:
            print("Não temos carros vendidos. :(")
        

        # Motos
        y = ["Motos Vendidos: " + y['nome'] + " Placa: " + y['placa'] + "CPF Comprador: " + x['cpf_comprador'] for y in lista_motos if y['vendido'] == True]

        if y != []:
            print(y)

        elif y == []:
            print("Não temos motos vendidos. :(")
        
        # Triciclos
        z = ["Triciclos Vendidos: " + z['nome'] + " Placa: " + z['placa'] + "CPF Comprador: " + x['cpf_comprador'] for z in lista_triciclos if z['vendido'] == True]

        if z != []:
            print(z)

        elif z == []:
            print("Não temos triciclos vendidos. :(")
        

        # Camionetes
        h = ["Camionetes Vendidos: " + h['nome'] + " Placa: " + h['placa'] + "CPF Comprador: " + x['cpf_comprador'] for h in lista_camionetes if h['vendido'] == True]

        if h != []:
            print(h)

        elif h == []:
            print("Não temos camionetes vendidos. :(")

    elif opcao == '7':
        pass

    elif opcao == '8':
        pass

    elif opcao == '0':
        print()
        break
    
    else:
        print("---"*6)
        print("Digite apenas as opções listadas.")
        print("---"*6)
        time.sleep(1)
