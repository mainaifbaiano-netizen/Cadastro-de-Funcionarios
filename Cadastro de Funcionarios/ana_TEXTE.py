# ==================================================
# Parte desenvolvida por: Ana Luiza
# Responsável pelas funções de alteração,
# exclusão e menu principal do sistema.
# ==================================================

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