from uuid import uuid4


class Veiculo:
    def __init__(self, data_fabricacao, nome, placa, valor, cpf_comprador, cor):
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
    def __init__(self, data_fabricacao, nome, placa, valor, 
                cpf_comprador, cor):
        super().__init__(data_fabricacao, nome, placa, valor, cpf_comprador, cor)

        idRandom = uuid4()
        self.__chassi = idRandom
        self.__portas = 4
        self.__potencia = 350
        self.__gasolina = "Gasolina"
    
    @property
    def listar_info(self):
        print(f"""
        Chass: {self.__chassi}
        Carro: {self.nome}
        Placa: {self.placa}
        Valor: {self.valor}
        CPF Comprador: {self.cpf_comprador}
        Cor: {self.cor}
        Portas: {self.__portas}
        Potencia (Em Cavalos): {self.__potencia}
        Tipo Gasolina: {self.__gasolina}
        """)


class Camionete(Veiculo):
    def __init__(self, data_fabricacao, nome, placa, valor, cpf_comprador, cor):
        super().__init__(data_fabricacao, nome, placa, valor, cpf_comprador, cor)
        idRandom = uuid4()
        self.__chassi = idRandom
        self.__portas = 2
        self.__capacidade_cacamba = 1054
        self.__potencia = 225
        self.__gasolina = "Gasolina"
        self.__cor = "roxo"


class Moto(Veiculo):
    def __init__(self, data_fabricacao, nome, placa, valor, 
    cpf_comprador, cor):
        super().__init__(data_fabricacao, nome, placa, valor, cpf_comprador, cor)
        idRandom = uuid4()
        self.__chassi = idRandom
        self.__potencia = 170
        self.__rodas = 2


class Triciclo(Veiculo):
    def __init__(self, data_fabricacao, nome, placa, valor, 
    cpf_comprador, cor):
        super().__init__(data_fabricacao, nome, placa, valor, cpf_comprador, cor)
        idRandom = uuid4()
        self.__chassi = idRandom
        self.__potencia = 170
        self.__rodas = 3



teste_1 = Carro("06/05/1999", "RX-7", "009", "1500", "0001", "Preta")
teste_1.listar_info
