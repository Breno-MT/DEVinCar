from classes.classe import Veiculo
from uuid import uuid4
from classes.data.data_array import lista_camionetes, lista_vendidos
from datetime import datetime


# Classe Camionete
class Camionete(Veiculo):
    def __init__(self, data_fabricacao, nome, placa, valor, cpf_comprador, cor = "Roxo"):
        super().__init__(data_fabricacao, nome, placa, valor, cpf_comprador, cor)
        idRandom = str(uuid4())
        self.chassi = idRandom
        self.portas = 2
        self.capacidade_cacamba = 1054
        self.potencia = 225
        self.gasolina = "Gasolina"
        self.vendido = False
        self.data_compra = ""
    
    @property
    def listar_info(self):
        print(f"""
        Chassi: {self.__chassi}
        Camionete: {self.nome}
        Placa: {self.placa}
        Valor: R$ {self.valor:.2f}
        CPF Comprador: {self.cpf_comprador}
        Cor: {self.cor}
        Portas: {self.__portas}
        Potencia (Em Cavalos): {self.__potencia}
        Capacidade da Caçamba: {self.__capacidade_cacamba}
        Tipo Gasolina: {self.gasolina}
        """)
    
    @staticmethod
    def alterar_info():

        placa = str(input("Digite a placa da camionete: "))
        cor_nova = str(input(f"Digite a nova cor: "))
        valor_novo = float(input(f"Digite o valor novo R$: "))

        if valor_novo <= 0:
            print("Digite um valor acima de R$0 !")
        
        elif valor_novo > 0.01:
            for x in lista_camionetes:

                if placa == x['placa']:
                    print(f"""--------- VOCÊ ALTEROU A CAMIONETE {x['nome']} --------- 
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
        
        cpf_cliente = str(input("Antes de começarmos, digite seu CPF (no max. 11 digitos): "))

        placa_escolhida = str(input("Digite a placa desejada: "))

        for x in lista_camionetes:
            
            if placa_escolhida == x['placa']:

                x['vendido'] = True
                x['cpf_comprador'] = cpf_cliente
                x['data_compra'] = data_compra
                lista_vendidos.append(x)

                print(f"""
                ------------ OBRIGADO PELA COMPRA!!! ------------
                O veículo {x['nome']} foi comprado no valor de R$: {x['valor']:.2f} !
                Data de compra: {data_compra}
                """)

                return
                

        print("A placa não existe ou você não digitou nada, ou você errou a opção. Tente novamente!")
