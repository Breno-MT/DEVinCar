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
    
    