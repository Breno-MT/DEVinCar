from uuid import uuid4


class Veiculo:
    def __init__(self, data_fabricacao, nome, placa, valor: float, cpf_comprador, cor):
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
        Valor: R$ {self.valor:.2f}
        CPF Comprador: {self.cpf_comprador}
        Cor: {self.cor}
        Portas: {self.__portas}
        Potencia (Em Cavalos): {self.__potencia}
        Tipo Gasolina: {self.__gasolina}
        """)


class Camionete(Veiculo):
    def __init__(self, data_fabricacao, nome, placa, valor, cpf_comprador, cor = "Roxo"):
        super().__init__(data_fabricacao, nome, placa, valor, cpf_comprador, cor)
        idRandom = uuid4()
        self.__chassi = idRandom
        self.__portas = 2
        self.__capacidade_cacamba = 1054
        self.__potencia = 225
        self.__gasolina = "Gasolina"
    
    @property
    def listar_info(self):
        print(f"""
        Chass: {self.__chassi}
        Carro: {self.nome}
        Placa: {self.placa}
        Valor: R$ {self.valor:.2f}
        CPF Comprador: {self.cpf_comprador}
        Cor: {self.cor}
        Portas: {self.__portas}
        Potencia (Em Cavalos): {self.__potencia}
        Capacidade da Caçamba: {self.__capacidade_cacamba}
        Tipo Gasolina: {self.__gasolina}
        """)


class Moto(Veiculo):
    def __init__(self, data_fabricacao, nome, placa, valor, 
    cpf_comprador, cor):
        super().__init__(data_fabricacao, nome, placa, valor, cpf_comprador, cor)

        idRandom = uuid4()
        self.__chassi = idRandom
        self.__potencia = 170
        self.__rodas = 2
        self.__gasolina = "Gasolina"
    

    @property
    def listar_info(self):
        print(f"""
        Chass: {self.__chassi}
        Carro: {self.nome}
        Placa: {self.placa}
        Valor: R$ {self.valor:.2f}
        CPF Comprador: {self.cpf_comprador}
        Cor: {self.cor}
        Rodas: {self.__rodas}
        Potencia (Em Cavalos): {self.__potencia}
        Tipo Gasolina: {self.__gasolina}
        """)


class Triciclo(Veiculo):
    def __init__(self, data_fabricacao, nome, placa, valor, 
    cpf_comprador, cor):
        super().__init__(data_fabricacao, nome, placa, valor, cpf_comprador, cor)
        idRandom = uuid4()
        self.__chassi = idRandom
        self.__potencia = 170
        self.__rodas = 3

    @property
    def listar_info(self):
        print(f"""
        Chass: {self.__chassi}
        Carro: {self.nome}
        Placa: {self.placa}
        Valor: R$ {self.valor:.2f}
        CPF Comprador: {self.cpf_comprador}
        Cor: {self.cor}
        Rodas: {self.__rodas}
        Potencia (Em Cavalos): {self.__potencia}
        Tipo Gasolina: {self.__gasolina}
        """)


teste_1 = Carro("06/05/1999", "RX-7", "009", 153300, "0001", "Preta")
teste_1.listar_info

teste_2 = Camionete("12/12/1991", "Nissan", "002", 15440, "002")
teste_2.listar_info

teste_3 = Moto("01/02/2002", "Kawasaki Ninja", "ASDZ-123", 12645, "003", "Cinza")
teste_3.listar_info

teste_4 = Triciclo("25/09/2016", "Sport", "ZAQW-456", 7567, "004", "Amarela")
teste_4.listar_info
