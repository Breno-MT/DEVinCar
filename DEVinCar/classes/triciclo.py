from classes.classes import Veiculo
from uuid import uuid4
from main import lista_triciclos

class Triciclo(Veiculo):
    def __init__(self, data_fabricacao, nome, placa, valor, 
    cpf_comprador, cor):
        super().__init__(data_fabricacao, nome, placa, valor, cpf_comprador, cor)
        idRandom = str(uuid4())
        self.__chassi = idRandom
        self.__potencia = 170
        self.__rodas = 3
        self.__gasolina = "Flex"
        self.vendido = False

    @property
    def listar_info(self):
        print(f"""
        Chassi: {self.__chassi}
        Triciclo: {self.nome}
        Placa: {self.placa}
        Valor: R$ {self.valor:.2f}
        CPF Comprador: {self.cpf_comprador}
        Cor: {self.cor}
        Rodas: {self.__rodas}
        Potencia (Em Cavalos): {self.__potencia}
        Tipo Gasolina: {self.__gasolina}
        """)
    
    def alterar_info(self):
        cor_nova = str(input(f"Digite a nova cor do triciclo {self.nome}: "))
        self.cor = cor_nova
