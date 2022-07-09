from classes.classe import Veiculo
from uuid import uuid4
from classes.data.data_array import lista_carros, lista_vendidos
from datetime import datetime


# Classe Carro
class Carro(Veiculo):
    def __init__(self, data_fabricacao, nome, placa, valor, 
                cpf_comprador, cor):
        super().__init__(data_fabricacao, nome, placa, valor, cpf_comprador, cor)

        idRandom = str(uuid4())
        self.chassi = idRandom
        self.portas = 4
        self.potencia = 350
        self.gasolina = "Gasolina"
        self.vendido = False


    
    @property
    def listar_info(self):
        print(f"""
        Chassi: {self.__chassi}
        Carro: {self.nome}
        Placa: {self.placa}
        Valor: R$ {self.valor:.2f}
        CPF Comprador: {self.cpf_comprador}
        Cor: {self.cor}
        Portas: {self.__portas}
        Potencia (Em Cavalos): {self.__potencia}
        Tipo Gasolina: {self.__gasolina}
        """)
    
    @staticmethod
    def alterar_info():

        placa = str(input("Digite a placa do carro: "))
        cor_nova = str(input(f"Digite a nova cor: "))
        valor_novo = float(input(f"Digite o valor novo R$: "))
        
        for x in lista_carros:

            if placa == x['placa']:
                print(f"""--------- VOCÊ ALTEROU O CARRO {x['nome']} --------- 
                Cor antiga: {x['cor']}
                Cor nova: {cor_nova}

                Valor antigo R$: {x['valor']:.2f} 
                Valor novo: R$ {valor_novo:.2f}

                """)
                x['cor'] = cor_nova
                x['valor'] = valor_novo
                return
        
        print("A placa não existe ou você não digitou nada. Tente novamente!")

        

    @staticmethod
    def vender_veiculo():
        data_compra = datetime.now().strftime("%d/%m/%Y")
        cpf_cliente = str(input("Antes de começarmos, digite o seu CPF (no max. 11 digitos): "))
        placa_escolhida = str(input("Digite a placa desejada: "))

        for x in lista_carros:
            
            if placa_escolhida == x['placa']:

                x['vendido'] = True
                x['cpf_comprador'] = cpf_cliente
                lista_vendidos.append(x)

                print(f"""
                ------------ OBRIGADO PELA COMPRA!!! ------------
                O veículo {x['nome']} foi comprado no valor de R$: {x['valor']:.2f} !
                Data de compra: {data_compra}
                """)

                return
                

        print("A placa não existe ou você não digitou nada. Tente novamente!")
