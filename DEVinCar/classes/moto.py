from classes.classes import Veiculo
from uuid import uuid4


# Classe Moto
class Moto(Veiculo):
    def __init__(self, data_fabricacao, nome, placa, valor, 
    cpf_comprador, cor):
        super().__init__(data_fabricacao, nome, placa, valor, cpf_comprador, cor)

        idRandom = uuid4()
        self.__chassi = idRandom
        self.__potencia = 170
        self.__rodas = 2
        self.__gasolina = "Gasolina"
        self.__vendido = False
    

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

    @property
    def __str__(self):
        print(f"""
        Chassi: {self.__chassi}
        Moto: {self.nome}
        Placa: {self.placa}
        Valor: R$ {self.valor:.2f}
        CPF Comprador: {self.cpf_comprador}
        Cor: {self.cor}
        Rodas: {self.__rodas}
        Potencia (Em Cavalos): {self.__potencia}
        Tipo Gasolina: {self.__gasolina} """)