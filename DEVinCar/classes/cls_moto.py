from classes.classe import Veiculo
from uuid import uuid4
from classes.data.data_array import lista_motos
from datetime import datetime

# Classe Moto
class Moto(Veiculo):
    def __init__(self, data_fabricacao, nome, placa, valor, 
    cpf_comprador, cor):
        super().__init__(data_fabricacao, nome, placa, valor, cpf_comprador, cor)

        idRandom = str(uuid4())
        self.__chassi = idRandom
        self.__potencia = 170
        self.__rodas = 2
        self.__gasolina = "Gasolina"
        self.vendido = False
    

    @property
    def listar_info(self):
        print(f"""
        Chassi: {self.__chassi}
        Moto: {self.nome}
        Placa: {self.placa}
        Valor: R$ {self.valor:.2f}
        CPF Comprador: {self.cpf_comprador}
        Cor: {self.cor}
        Rodas: {self.__rodas}
        Potencia (Em Cavalos): {self.__potencia}
        Tipo Gasolina: {self.__gasolina}
        """)
    
    def alterar_info(self):
        cor_nova = str(input(f"Digite a nova cor da moto {self.nome}: "))
        self.cor = cor_nova

    @staticmethod
    def vender_veiculo():
        cpf_cliente = str(input("Antes de começarmos, digite o seu CPF (no max. 11 digitos): "))
        placa_escolhida = str(input("Digite a placa desejada: "))
        data_compra = datetime.now().strftime("%d/%m/%Y")

        for x in lista_motos:
            
            if placa_escolhida == x['placa']:

                x['vendido'] = True
                x['cpf_comprador'] = cpf_cliente
                return print(f"""
                ------------ OBRIGADO PELA COMPRA!!! ------------
                O veículo {x['nome']} foi comprado no valor de R$: {x['valor']:.2f} !
                Data de compra: {data_compra}
                """)
                

        print("A placa não existe ou você não digitou nada. Tente novamente!")
