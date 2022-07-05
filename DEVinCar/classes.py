class Veiculo:
    def __init__(self, chassi, data_fabricacao, nome, placa, valor, cpf_comprador, cor):
        self.chassi = chassi
        self.data_fabricacao = data_fabricacao
        self.nome = nome
        self.placa = placa
        self.valor = valor
        self.cpf_comprador = cpf_comprador
        self.cor = cor

    def vender_veiculo(self):
        pass

    def listar_info(self):
        pass

    def alterar_info(self):
        pass

    def cor_e_valor(self):
        pass


class Carro(Veiculo):
    def __init__(self, chassi, data_fabricacao, nome, placa, valor, 
                cpf_comprador, cor):
        super().__init__(chassi, data_fabricacao, nome, placa, valor, cpf_comprador, cor)
        self.__portas = 4
        self.__potencia = 350
        self.__gasolina = "Gasolina"


class Camionete(Veiculo):
    def __init__(self, chassi, data_fabricacao, nome, placa, valor, cpf_comprador, cor):
        super().__init__(chassi, data_fabricacao, nome, placa, valor, cpf_comprador, cor)

        self.__portas = 2
        self.__capacidade_cacamba = 1054
        self.__potencia = 225
        self.__gasolina = "Gasolina"
        self.__cor = "roxo"


class Moto(Veiculo):
    def __init__(self, chassi, data_fabricacao, nome, placa, valor, 
    cpf_comprador, cor):
        super().__init__(chassi, data_fabricacao, nome, placa, valor, cpf_comprador, cor)
        self.__potencia = 170
        self.__rodas = 2


class Tricilo(Veiculo):
    def __init__(self, chassi, data_fabricacao, nome, placa, valor, 
    cpf_comprador, cor):
        super().__init__(chassi, data_fabricacao, nome, placa, valor, cpf_comprador, cor)
        self.__potencia = 170
        self.__rodas = 3


