import time
import os

usuarios = []
contas = []

def menu():
    i = 0
    while i != 9:
        os.system("cls" if os.name == "nt" else "clear")
        print("\n===== MENU PRINCIPAL =====")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Transferir")
        print("4 - Cadastrar Usuário")
        print("5 - Remover Usuário")
        print("6 - Criar Conta")
        print("7 - Remover Conta")
        print("8 - Listar Contas")
        print("9 - Sair")
        print("==========================")
        

        if i == 1:
            depositar()
        elif i == 2:
            sacar()
        elif i == 3:
            transferir()
        elif i == 4:
            cadastrar_usuario()
        elif i == 5:
            remover_usuario()
        elif i == 6:
            criar_conta()
        elif i == 7:
            remover_conta()
        elif i == 8:
            listar_contas()
        elif i == 9:
            print("Saindo...")
        else:
            print("Opção inválida!")
            time.sleep(2)

def depositar():
    numero_conta = input("Digite o número da conta: ")
    conta_encontrada = None
    for c in contas:
        if c["numero"] == numero_conta:
            conta_encontrada = c
            break

    if conta_encontrada:
        valor = float(input("Digite o valor para depósito: "))
        if valor > 0:
            conta_encontrada["saldo"] += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido!")
    else:
        print("Conta não encontrada!")
    time.sleep(3)


def sacar():
    numero_conta = input("Digite o número da conta: ")
    conta_encontrada = None
    for c in contas:
        if c["numero"] == numero_conta:
            conta_encontrada = c
            break

    if conta_encontrada:
        valor = float(input("Digite o valor para saque: "))
        if 0 < valor <= conta_encontrada["saldo"]:
            conta_encontrada["saldo"] -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente ou valor inválido!")
    else:
        print("Conta não encontrada!")
    time.sleep(3)


def transferir():
    origem = input("Digite o número da conta de origem: ")
    destino = input("Digite o número da conta de destino: ")

    conta_origem = None
    conta_destino = None

    # Encontrar contas sem usar next()
    for c in contas:
        if c["numero"] == origem:
            conta_origem = c
        elif c["numero"] == destino:
            conta_destino = c

    if conta_origem and conta_destino:
        valor = float(input("Digite o valor da transferência: "))
        if 0 < valor <= conta_origem["saldo"]:
            conta_origem["saldo"] -= valor
            conta_destino["saldo"] += valor
            print(f"Transferência de R${valor:.2f} realizada com sucesso!")
        else:
            print("Saldo insuficiente ou valor inválido!")
    else:
        print("Conta de origem ou destino não encontrada!")
    time.sleep(3)


def cadastrar_usuario():
    cpf = str(input("Insira seu CPF: "))
    usuario_existente = False
    for it in usuarios:
        if cpf == it[0]:
            print("Esse usuário já existe.")
            usuario_existente = True
            time.sleep(3)
            break

    if not usuario_existente:
        nome = input("Insira seu nome: ")
        dt_nascimento = input("Insira a data do seu nascimento (dd/mm/aaaa): ")
        endereco = input("Insira seu endereço: ")
        usuarios.append([cpf, nome, dt_nascimento, endereco])
        print("Usuário cadastrado com sucesso!")
        time.sleep(3)


def remover_usuario():
    cpf = str(input("Insira o CPF do usuário a ser removido: "))
    removido = False
    for it in usuarios:
        if it[0] == cpf:
            usuarios.remove(it)
            removido = True
            break

    if removido:
        print("Usuário removido.")
    else:
        print("Usuário não encontrado.")
    time.sleep(3)


def criar_conta():
    cpf = input("Digite o CPF do usuário dono da conta: ")
    usuario = None
    for u in usuarios:
        if u[0] == cpf:
            usuario = u
            break

    if usuario:
        numero = str(len(contas) + 1).zfill(4)
        contas.append({"numero": numero, "cpf": cpf, "saldo": 0.0})
        print(f"Conta {numero} criada com sucesso para {usuario[1]}!")
    else:
        print("Usuário não encontrado. Cadastre o usuário primeiro.")
    time.sleep(3)


def remover_conta():
    numero = input("Digite o número da conta a ser removida: ")
    removido = False
    for c in contas:
        if c["numero"] == numero:
            contas.remove(c)
            removido = True
            break

    if removido:
        print("Conta removida com sucesso!")
    else:
        print("Conta não encontrada.")
    time.sleep(3)


def listar_contas():
    if not contas:
        print("Nenhuma conta cadastrada.")
    else:
        print("\n===== LISTA DE CONTAS =====")
        for c in contas:
            nome = "Desconhecido"
            for u in usuarios:
                if u[0] == c["cpf"]:
                    nome = u[1]
                    break
            print(f"Conta: {c['numero']} | Titular: {nome} | CPF: {c['cpf']} | Saldo: R${c['saldo']:.2f}")
    input("\nPressione Enter para continuar...")


# ---------------------------
if __name__ == "__main__":
    menu()