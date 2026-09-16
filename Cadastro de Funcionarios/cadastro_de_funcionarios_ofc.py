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


class Gerente(Funcionario):
    def calcular_beneficio(self):
        return self.salario * 0.20


class Estagiario(Funcionario):
    def calcular_beneficio(self):
        return self.salario * 0.05


class SistemaFuncionarios:
    def __init__(self):
        self.funcionarios = []

    def cadastrar(self):
        print("\n--- CADASTRO DE FUNCIONÁRIO ---")

        nome = input("Nome: ")
        matricula = input("Matrícula: ")

        for funcionario in self.funcionarios:
            if funcionario.matricula == matricula:
                print("Essa matrícula já está cadastrada!")
                return

        cargo = input("Cargo: ")

        try:
            salario = float(input("Salário: R$ "))
        except ValueError:
            print("Digite um valor válido para o salário.")
            return

        print("\nTipo de funcionário:")
        print("1 - Funcionário comum")
        print("2 - Gerente")
        print("3 - Estagiário")

        tipo = input("Escolha: ")

        if tipo == "2":
            funcionario = Gerente(nome, matricula, cargo, salario)
        elif tipo == "3":
            funcionario = Estagiario(nome, matricula, cargo, salario)
        else:
            funcionario = Funcionario(nome, matricula, cargo, salario)

        self.funcionarios.append(funcionario)

        print("Funcionário cadastrado com sucesso!")

    def consultar(self):
        print("\n--- FUNCIONÁRIOS CADASTRADOS ---")

        if not self.funcionarios:
            print("Nenhum funcionário cadastrado.")
            return

        for funcionario in self.funcionarios:
            print("\n-------------------------")
            funcionario.exibir_dados()
            print(f"Benefício: R$ {funcionario.calcular_beneficio():.2f}")

    def alterar(self):
        print("\n--- ALTERAR FUNCIONÁRIO ---")

        matricula = input("Digite a matrícula do funcionário: ")

        for funcionario in self.funcionarios:
            if funcionario.matricula == matricula:
                print("Deixe o campo vazio para não alterar.")

                nome = input(f"Novo nome ({funcionario.nome}): ")
                cargo = input(f"Novo cargo ({funcionario.cargo}): ")
                salario = input(f"Novo salário ({funcionario.salario}): ")

                if nome:
                    funcionario.nome = nome

                if cargo:
                    funcionario.cargo = cargo

                if salario:
                    try:
                        funcionario.salario = float(salario)
                    except ValueError:
                        print("Salário inválido.")

                print("Funcionário alterado com sucesso!")
                return

        print("Funcionário não encontrado.")

    def excluir(self):
        print("\n--- EXCLUIR FUNCIONÁRIO ---")

        matricula = input("Digite a matrícula do funcionário: ")

        for funcionario in self.funcionarios:
            if funcionario.matricula == matricula:
                self.funcionarios.remove(funcionario)
                print("Funcionário excluído com sucesso!")
                return

        print("Funcionário não encontrado.")


def main():
    sistema = SistemaFuncionarios()

    while True:
        print("\n================================")
        print("   SISTEMA DE FUNCIONÁRIOS")
        print("================================")
        print("1 - Cadastrar funcionário")
        print("2 - Consultar funcionários")
        print("3 - Alterar funcionário")
        print("4 - Excluir funcionário")
        print("5 - Sair")
        print("================================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            sistema.cadastrar()
        elif opcao == "2":
            sistema.consultar()
        elif opcao == "3":
            sistema.alterar()
        elif opcao == "4":
            sistema.excluir()
        elif opcao == "5":
            print("Sistema encerrado. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()