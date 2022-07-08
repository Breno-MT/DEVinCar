from classes.cls_carro import Carro
from classes.cls_moto import Moto
from classes.cls_triciclo import Triciclo
from classes.cls_camionete import Camionete
from classes.data.data_array import lista_carros, lista_motos, lista_camionetes, lista_triciclos


import time
import sys

carro_1 = Carro("05/05/1978", "Supra", "GDFG-5466", 15000, "0", "Preta")
carro_2 = Carro("01/01/1980", "RX-7", "GFD-0123", 15600, "0", "Azul")

moto_1 = Moto("11/05/1999", "Kawasaki Ninja", "POSD-3422", 30000, "0", "Verde")

camionete_1 = Camionete("09/09/2022", "Toyota", "KODF-0231", 32000, "0")

triciclo_1 = Triciclo("07/12/2000", "Caloi", "QWAS-5441", 12000, "0", "Vermelho")


lista_carros.append(carro_1.__dict__)
lista_carros.append(carro_2.__dict__)

lista_motos.append(moto_1.__dict__)

lista_camionetes.append(camionete_1.__dict__)

lista_triciclos.append(triciclo_1.__dict__)


nome_cliente = str(input("Digite o seu nome: "))
cpf_cliente = str(input("Digite o seu CPF: "))


if nome_cliente == "":
    print("Não deixe seu nome em branco.")
    sys.exit()

elif cpf_cliente == "":
    print("Não deixe seu CPF em branco.")
    sys.exit()

elif nome_cliente and cpf_cliente == "":
    print("Digite seu nome e CPF por gentileza.")
    sys.exit()

while True:

    opcao = input(f"""
        _______________________________________________________________
       |         __   ___                       __        __           |
       |        |  \ |__  \  /      | |\ |     /  `  /\  |__)          |
       |        |__/ |___  \/       | | \|     \__, /~~\ |  \          |
       |                                                               |     
                            Bem-vindo(a) {nome_cliente} !                                  
                            CPF: {cpf_cliente} !                                 
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
            # Dai aqui vai a lógica de uscar placa e descobrir o carro que ele quer, chamando as funções em suas respectivas classes.
            s_ou_n = Carro.vender_veiculo()

    elif opcao == '6':
        # Carros
        x = ["Carros Vendidos: " + x['nome'] + " Placa: " + x['placa'] for x in lista_carros if x['vendido'] == True]

        if x != []:
            print(x)

        elif x == []:
            print("Não temos carros vendidos. :(")
        

        # Motos
        y = ["Motos Vendidos: " + y['nome'] + " Placa: " + y['placa'] for y in lista_motos if y['vendido'] == True]

        if y != []:
            print(y)

        elif y == []:
            print("Não temos motos vendidos. :(")
        
        # Triciclos
        z = ["Triciclos Vendidos: " + z['nome'] + " Placa: " + z['placa'] for z in lista_triciclos if z['vendido'] == True]

        if z != []:
            print(z)

        elif z == []:
            print("Não temos triciclos vendidos. :(")
        

        # Camionetes
        h = ["Camionetes Vendidos: " + h['nome'] + " Placa: " + h['placa'] for h in lista_camionetes if h['vendido'] == True]

        if h != []:
            print(h)

        elif h == []:
            print("Não temos camionetes vendidos. :(")

    elif opcao == '7':
        pass

    elif opcao == '8':
        pass

    elif opcao == '0':
        break
    
    else:
        print("---"*6)
        print("Digite apenas as opções listadas.")
        print("---"*6)
        time.sleep(1)
