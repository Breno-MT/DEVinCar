from uuid import uuid4

# Classe Veiculo
class Veiculo:
    def __init__(self, data_fabricacao, nome, placa, valor: float, cpf_comprador, cor):
        self.data_fabricacao = data_fabricacao
        self.nome = nome
        self.placa = placa
        self.valor = valor
        self.cpf_comprador = cpf_comprador
        self.cor = cor

    # Método de vender veiculo
    def vender_veiculo(self):
        pass

    # Método de listar informações de um determinado veiculo
    def listar_info(self):
        pass

    # Método para alterar informações de cor e valor
    def alterar_info(self):
        pass
    

# Classe Carro
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
    
    def alterar_info(self):
        cor_nova = str(input(f"Digite a nova cor do carro {self.nome}: "))
        self.cor = cor_nova


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
    
    @property
    def listar_info(self):
        print(f"""
        Chass: {self.__chassi}
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
    

    @property
    def listar_info(self):
        print(f"""
        Chass: {self.__chassi}
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


# Classe Triciclo
class Triciclo(Veiculo):
    def __init__(self, data_fabricacao, nome, placa, valor, 
    cpf_comprador, cor):
        super().__init__(data_fabricacao, nome, placa, valor, cpf_comprador, cor)
        idRandom = uuid4()
        self.__chassi = idRandom
        self.__potencia = 170
        self.__rodas = 3
        self.__gasolina = "Flex"

    @property
    def listar_info(self):
        print(f"""
        Chass: {self.__chassi}
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


carro_1 = Carro("06/05/1999", "RX-7", "VHBX-076", 153300, "001", "Preta")
carro_1.alterar_info()
carro_1.listar_info

camionete_2 = Camionete("12/12/1991", "Nissan", "KSDF-095", 15440, "002")
camionete_2.alterar_info()
camionete_2.listar_info

moto_3 = Moto("01/02/2002", "Kawasaki Ninja", "ASDZ-123", 12645, "003", "Cinza")
moto_3.listar_info

triciclo_4 = Triciclo("25/09/2016", "Sport", "ZAQW-456", 7567, "004", "Amarela")
triciclo_4.listar_info
