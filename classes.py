#Criando as classes de introdução para o código

# arquivo classes.py

class Funcionario:
    def __init__(self, nome, idade, cargo, sexo, data_nascimento, setor, salario):
        self.nome = nome
        self.idade = idade
        self.cargo = cargo
        self.sexo = sexo
        self.data_nascimento = data_nascimento
        self.setor = setor
        self.salario = salario

class GerenciadorFuncionarios:
    def __init__(self):
        self.funcionarios = []

    def inserir_funcionario(self, nome, idade, cargo, sexo, data_nascimento, setor, salario):
        funcionario = Funcionario(nome, idade, cargo, sexo, data_nascimento, setor, salario)
        self.funcionarios.append(funcionario)
        print(f"Funcionário {nome} inserido com sucesso!")
        return True  # Retorna True para indicar sucesso

    def listar_funcionarios(self):
        if not self.funcionarios:
            print("Não há funcionários cadastrados.")
        else:
            print("Lista de funcionários:")
            for i, func in enumerate(self.funcionarios):
                print(f''' {i + 1}. 
    Nome: {func.nome} 
    Idade: {func.idade} 
    Cargo: {func.cargo}
    Sexo: {func.sexo}
    Data de Nascimento: {func.data_nascimento} 
    Setor: {func.setor} 
    Salário: {func.salario}''')
        return True  # Retorna True se listar funcionários com sucesso

    def editar_funcionario(self, indice, nome, idade, cargo, sexo, data_nascimento, setor, salario):
        if 0 <= indice < len(self.funcionarios):
            self.funcionarios[indice].nome = nome
            self.funcionarios[indice].idade = idade
            self.funcionarios[indice].cargo = cargo
            self.funcionarios[indice].sexo = sexo
            self.funcionarios[indice].data_nascimento = data_nascimento
            self.funcionarios[indice].setor = setor
            self.funcionarios[indice].salario = salario
            print(f"Funcionário {nome} editado com sucesso!")
            return True  # Retorna True se editar funcionário com sucesso
        else:
            print("Índice de funcionário inválido.")
            return False  # Retorna False se índice inválido

    def remover_funcionario(self, indice):
        if 0 <= indice < len(self.funcionarios):
            nome = self.funcionarios[indice].nome
            del self.funcionarios[indice]
            print(f"Funcionário {nome} removido com sucesso!")
            return True  # Retorna True se remover funcionário com sucesso
        else:
            print("Índice de funcionário inválido.")
            return False  # Retorna False se índice inválido


