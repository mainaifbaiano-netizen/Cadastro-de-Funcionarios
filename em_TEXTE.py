# ==================================================
# Parte desenvolvida por: Emile
# Responsável pela herança e pelo cálculo
# de benefícios específicos para cada cargo.
# ==================================================

class Gerente(Funcionario):
    def calcular_beneficio(self):
        # Gerentes recebem um benefício maior
        return self.salario * 0.20


class Estagiario(Funcionario):
    def calcular_beneficio(self):
        # Estagiários recebem um benefício reduzido
        return self.salario * 0.05