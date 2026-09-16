# ==================================================
# Parte desenvolvida por: Máina
# Responsável pelas funções de cadastro
# e consulta dos funcionários.
# ==================================================

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