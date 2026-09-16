# ==================================================
# Parte desenvolvida por: Ludmilla
# Responsável pela criação da classe principal
# dos funcionários e seus métodos básicos.
# ==================================================

class Funcionario:
    def __init__(self, nome, matricula, cargo, salario):
        self.nome = nome
        self.matricula = matricula
        self.cargo = cargo
        self.__salario = salario

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, novo_salario):
        if novo_salario >= 0:
            self.__salario = novo_salario
        else:
            print("O salário não pode ser negativo.")

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Matrícula: {self.matricula}")
        print(f"Cargo: {self.cargo}")
        print(f"Salário: R$ {self.salario:.2f}")

    def calcular_beneficio(self):
        return self.salario * 0.10