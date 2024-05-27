# Funções de Utilidade
def exibir_menu():
    return input("""
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Listar Contas
    [5] Listar Clientes
    [6] Desativar Conta
    [7] Cadastrar Cliente
    [8] Criar Conta Corrente
    [0] Sair
    => """)

def operacao_invalida():
    print("Operação inválida, por favor selecione novamente a operação desejada.")

def input_float(mensagem):
    return float(input(mensagem))

# Funções de Operações Bancárias
def depositar(saldo):
    valor = input_float("Informe o valor do depósito: ")
    if valor > 0:
        saldo += valor
        print("Depósito realizado com sucesso!")
        return saldo, f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
        return saldo, ""

def sacar(saldo, limite, numero_saques):
    valor = input_float("Informe o valor do saque: ")
    extrato = ""
    if valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite de R$ 1000.00.")
    elif numero_saques >= 5:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("========================================")

# Funções de Gerenciamento de Clientes e Contas
def cadastrar_cliente(clientes):
    cpf = input("Informe o CPF (somente números): ")
    if cpf in clientes:
        print("Cliente já cadastrado!")
        return clientes

    nome = input("Informe o nome: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/UF): ")

    clientes[cpf] = {"nome": nome, "data_nascimento": data_nascimento, "endereco": endereco}
    print("Cliente cadastrado com sucesso!")
    return clientes

def criar_conta_corrente(contas, clientes):
    cpf = input("Informe o CPF do cliente: ")
    if cpf not in clientes:
        print("Cliente não encontrado! Cadastre o cliente primeiro.")
        return contas

    numero_conta = len(contas) + 1
    contas[numero_conta] = {"agencia": "0001", "numero_conta": numero_conta, "cliente": cpf, "saldo": 5000, "limite": 1000, "extrato": "", "numero_saques": 0}
    print(f"Conta corrente {numero_conta} criada com sucesso para o cliente {clientes[cpf]['nome']}!")
    return contas

def listar_contas(contas):
    print("\n========== LISTA DE CONTAS ==========")
    for numero_conta, dados_conta in contas.items():
        print(f"Número da Conta: {numero_conta}")
        print(f"Agência: {dados_conta['agencia']}")
        print(f"Cliente (CPF): {dados_conta['cliente']}")
        print(f"Saldo: R$ {dados_conta['saldo']:.2f}")
        print("=====================================")

def listar_clientes(clientes):
    print("\n========== LISTA DE CLIENTES ==========")
    for cpf, dados_cliente in clientes.items():
        print(f"CPF: {cpf}")
        print(f"Nome: {dados_cliente['nome']}")
        print(f"Data de Nascimento: {dados_cliente['data_nascimento']}")
        print(f"Endereço: {dados_cliente['endereco']}")
        print("=======================================")

def desativar_conta(contas):
    numero_conta = int(input("Informe o número da conta que deseja desativar: "))
    if numero_conta in contas:
        del contas[numero_conta]
        print(f"Conta {numero_conta} desativada com sucesso!")
    else:
        print("Conta não encontrada!")

# Função Principal
def main():
    clientes = {}
    contas = {}
    LIMITE_SAQUES = 5

    while True:
        opcao = exibir_menu()

        if opcao == "1":
            numero_conta = int(input("Informe o número da conta: "))
            if numero_conta in contas:
                conta = contas[numero_conta]
                saldo, extrato = depositar(conta["saldo"])
                conta["saldo"] = saldo
                conta["extrato"] += extrato
            else:
                operacao_invalida()

        elif opcao == "2":
            numero_conta = int(input("Informe o número da conta: "))
            if numero_conta in contas:
                conta = contas[numero_conta]
                saldo, extrato, numero_saques = sacar(conta["saldo"], conta["limite"], conta["numero_saques"])
                conta["saldo"] = saldo
                conta["extrato"] += extrato
                conta["numero_saques"] = numero_saques
            else:
                operacao_invalida()

        elif opcao == "3":
            numero_conta = int(input("Informe o número da conta: "))
            if numero_conta in contas:
                conta = contas[numero_conta]
                exibir_extrato(conta["saldo"], conta["extrato"])
            else:
                operacao_invalida()

        elif opcao == "4":
            listar_contas(contas)

        elif opcao == "5":
            listar_clientes(clientes)

        elif opcao == "6":
            desativar_conta(contas)

        elif opcao == "7":
            clientes = cadastrar_cliente(clientes)

        elif opcao == "8":
            contas = criar_conta_corrente(contas, clientes)

        elif opcao == "0":
            break

        else:
            operacao_invalida()

if __name__ == "__main__":
    main()
