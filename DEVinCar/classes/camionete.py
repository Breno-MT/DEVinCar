from classes.classes import Veiculo
from uuid import uuid4

# Classe Camionete
class Camionete(Veiculo):
    def __init__(self, data_fabricacao, nome, placa, valor, cpf_comprador, cor = "Roxo"):
        super().__init__(data_fabricacao, nome, placa, valor, cpf_comprador, cor)
        idRandom = uuid4()
        self.__chassi = idRandom
        self.__portas = 2
        self.__capacidade_cacamba = 1054
        self.__potencia = 225
        self.__gasolina = "Gasolina"
        self.__vendido = False
    
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

    @property
    def __str__(self):
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
