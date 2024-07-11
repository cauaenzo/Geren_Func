# arquivo completo.py

from classes import Funcionario, GerenciadorFuncionarios

def menu_interativo(gerenciador):
    while True:
        print("\n=== Menu ===")
        print("1. Inserir novo funcionário")
        print("2. Listar funcionários")
        print("3. Editar funcionário")
        print("4. Remover funcionário")
        print("5. Sair")

        escolha = input("\nDigite o número da opção desejada: ")

        if escolha == "1":
            nome = input("Nome do funcionário: ")
            idade = int(input("Idade: "))
            cargo = input("Cargo: ")
            sexo = input("Sexo: ")
            data_nascimento = input("Data de Nascimento (DD/MM/AAAA): ")
            setor = input("Setor: ")
            salario = float(input("Salário: "))
            gerenciador.inserir_funcionario(nome, idade, cargo, sexo, data_nascimento, setor, salario)
            continuar = input()

        elif escolha == "2":
            gerenciador.listar_funcionarios()
            continuar = input()

        elif escolha == "3":
            indice = int(input("Digite o índice do funcionário a ser editado: ")) - 1
            if 0 <= indice < len(gerenciador.funcionarios):
                nome = input("Novo nome: ")
                idade = int(input("Nova idade: "))
                cargo = input("Novo cargo: ")
                sexo = input("Novo sexo: ")
                data_nascimento = input("Nova data de Nascimento (DD/MM/AAAA): ")
                setor = input("Novo setor: ")
                salario = float(input("Novo salário: "))
                gerenciador.editar_funcionario(indice, nome, idade, cargo, sexo, data_nascimento, setor, salario)
                continuar = input()
            else:
                print("Índice de funcionário inválido.")
                continuar = input()
        elif escolha == "4":
            indice = int(input("Digite o índice do funcionário a ser removido: ")) - 1
            gerenciador.remover_funcionario(indice)
            continuar = input()

        elif escolha == "5":
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Por favor, digite um número de 1 a 5.")
            continuar = input()
    return

