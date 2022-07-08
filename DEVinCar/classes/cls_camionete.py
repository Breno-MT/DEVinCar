from classes.classe import Veiculo
from uuid import uuid4
from classes.data.data_array import lista_camionetes
from datetime import datetime


# Classe Camionete
class Camionete(Veiculo):
    def __init__(self, data_fabricacao, nome, placa, valor, cpf_comprador, cor = "Roxo"):
        super().__init__(data_fabricacao, nome, placa, valor, cpf_comprador, cor)
        idRandom = str(uuid4())
        self.__chassi = idRandom
        self.__portas = 2
        self.__capacidade_cacamba = 1054
        self.__potencia = 225
        self.__gasolina = "Gasolina"
        self.vendido = False
    
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
        Tipo Gasolina: {self.__gasolina}
        """)
    
    def alterar_info(self):
        cor_nova = str(input(f"Digite a nova cor do carro {self.nome}: "))
        self.cor = cor_nova

    @staticmethod
    def vender_veiculo():
        
        data_compra = datetime.now().strftime("%d/%m/%Y")
        
        cpf_cliente = str(input("Antes de começarmos, digite seu CPF (no max. 11 digitos): "))

        placa_escolhida = str(input("Digite a placa desejada: "))

        for x in lista_camionetes:
            
            if placa_escolhida == x['placa']:

                x['vendido'] = True
                x['cpf_comprador'] = cpf_cliente

                return print(f"""
                ------------ OBRIGADO PELA COMPRA!!! ------------
                O veículo {x['nome']} foi comprado no valor de R$: {x['valor']:.2f} !
                Data de compra: {data_compra}
                """)
                

        print("A placa não existe ou você não digitou nada, ou você errou a opção. Tente novamente!")
