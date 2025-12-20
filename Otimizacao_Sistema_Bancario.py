menu = """
=========MENU===========

[u] Cadastrar Usuário
[c] Criar conta
[d] Depositar
[s] Sacar
[e] Extrato
[lc] Listas Contas
[q] Sair

========================
=> """


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
agencia = "0001"
usuarios = []
contas = []


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite 

    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("")
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("")
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("")
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\t R$ {valor:.2f}\n"
        numero_saques += 1
        print("")
        print("Saque realizado com sucesso!")
    else:
        print("")
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques

 
def depositar(saldo, valor, extrato,/):

    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\t R$ {valor:.2f}\n"
        print("")
        print("Depósito realizado com sucesso!")
    else:
        print("")
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

 
def mostrar_extrato(saldo,/,*,extrato):

    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\t R$ {saldo:.2f}")
    print("==========================================")

 
def cadastro_usuario(usuarios):

    print("=" * 60)
    print("Cadastro de Usuários".center(60))
    print("=" * 60)

    nome = input("Digite o nome do solicitante usuário a ser cadastrado: ")
    data_nascimento = input("Digite sua data de nascimento: ")
    cpf = input("Digite seu CPF:").replace(".","").replace("-","")

    #Validação básica do CPF
    if len(cpf) != 11:
        print("O CPF digitado não possui a quantidade de números correta. Verifique novamente")
        return 

    for usuario in usuarios:

        if usuario["cpf"] == cpf:
            print("O usuário já está cadastrado no sistema")
            return

    endereco_logradouro = input("Digite o nome do seu logradouro/rua: ")
    endereco_numero = input("Digite o número da sua casa: ")
    endereco_bairro = input("Digite o nome do seu bairro: ")
    endereco_cidade = input("Digite o nome da sua cidade: ")
    endereco_estado = input("Digite a sigla do seu estado: ").upper()

    if len(endereco_estado) != 2:
        print("UF inválida! Digite uma sigla válida. (Ex. MG)")
        return

    endereco = f"{endereco_logradouro},{endereco_numero} - {endereco_bairro} - {endereco_cidade}/{endereco_estado}"

    usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }

    usuarios.append(usuario)

    print("")
    print(f"Usuário {usuario['nome']} cadastrado com sucesso!")


def criar_conta(agencia, usuarios, contas):

    print("=" * 60)
    print("Cadastro de Conta".center(60))
    print("=" * 60)

    usuario_cpf = input("Digite seu CPF:").replace(".","").replace("-","")

    usuario_encontrado = None

    for usuario in usuarios:

        if usuario["cpf"] == usuario_cpf:
            usuario_encontrado = usuario
            break

    if usuario_encontrado is None:
        print("O usuário não está cadastrado no sistema. Volte e siga o processo de criação de usuário.")
        return
    
    numero_conta = len(contas) + 1

    conta = {
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuario_encontrado
    }

    contas.append(conta)

    print("")
    print("Conta criada com sucesso!")


def listar_contas(contas):

    for conta in contas:
        print("=" * 100)
        print(f"""
            Agência:\t{conta['agencia']}
            C/C:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """)


def main():
    while True:

        opcao = input(menu)

        if opcao == "d":

            print("=" * 60)
            print("Área de Depósito".center(60))
            print("=" * 60)

            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":

            print("=" * 60)
            print("Área de Saque".center(60))
            print("=" * 60)

            valor = float(input("Informe o valor do saque: "))

            saldo, extrato, numero_saques = sacar(
                saldo=saldo, 
                valor=valor, 
                extrato=extrato, 
                limite=limite, 
                numero_saques=numero_saques, 
                limite_saques=LIMITE_SAQUES
                )

        elif opcao == "e":

            mostrar_extrato(saldo, extrato=extrato)

        elif opcao == "u":

            cadastro_usuario(usuarios)

        elif opcao == "c":

            criar_conta(agencia, usuarios, contas)

        elif opcao == "lc":

            listar_contas(contas)

        elif opcao == "q":

            break

        else:

            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()