from classes import carro, moto, camionete, triciclo
import time
import sys

lista_carros = []

lista_motos = []

lista_camionetes = []

lista_triciclos = []


carro_1 = carro.Carro("05/05/2002", "Supra", "GDFG-5466", 15000, "0", "Preta")
lista_carros.append(carro_1)

carro_2 = carro.Carro("01/01/1111", "RX-7", "GFD-0123", 15600, "0", "Azul")
lista_carros.append(carro_2)

moto_1 = moto.Moto("11/05/1999", "Kawasaki Ninja", "POSD-3422", 30000, "0", "Verde")
lista_motos.append(moto_1)

camionete_1 = camionete.Camionete("09/09/2022", "Toyota", "KODF-0231", 32000, "0")
lista_camionetes.append(camionete_1)

triciclo_1 = triciclo.Triciclo("07/12/2000", "Caloi", "QWAS-5441", 12000, "0", "")
lista_triciclos.append(triciclo_1)

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
    time.sleep(1.5)

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
       | [5] Carros Disponíveis                                        | 
       |                                                               | 
       | [6] Carros Vendidos                                           | 
       |                                                               | 
       | [7] Carro vendido com o menor preço                           | 
       |                                                               | 
       | [8] Carro vendido com o maior preço                           | 
       |                                                               | 
       | [0] Sair                                                      | 
       |_______________________________________________________________| 
       |                                                               | 
       |                                                               | 
         Digite sua opção: """)

    if opcao == '1':
        moto_1.listar_info
        triciclo_1.listar_info

    elif opcao == '2':
        carro_1.listar_info
        carro_2.listar_info

    elif opcao == '3':
        camionete_1.listar_info

    elif opcao == '4':
        print('---'*10)
        carro_1.listar_info
        print('---'*10)
        carro_2.listar_info
        print('---'*10)
        moto_1.listar_info
        print('---'*10)
        camionete_1.listar_info
        print('---'*10)
        triciclo_1.listar_info
        print('---'*10)
        time.sleep(5)

    elif opcao == '5':
        pass

    elif opcao == '6':
        pass

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
