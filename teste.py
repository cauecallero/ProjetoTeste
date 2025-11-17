
#Ex1

def saudar_visitante():
    print("Bem-vindo(a) à TechSolutions! Como posso ajudar?")
saudar_visitante()
saudar_visitante()
saudar_visitante()

print("\n")

#Ex2

def emitir_som_alarme():
    print("BEEP! BEEP! BEEP! O bolo está pronto!")

bolo_pronto = str(input("Digite se o bolo está pronto\n"))
if(bolo_pronto == "ficou pronto"):
    emitir_som_alarme()
else:
    print("Erro")

print("\n")

#Ex3

def cartao_boas_festas():
    print("Feliz Natal e um próspero Ano Novo! Que todos os seus desejos se realizem!")

enviar_cartao = str(input("Deseja enviar o cartão?\n"))
if(enviar_cartao == "enviar"):
    cartao_boas_festas()
else:
    print("Erro")

print("\n")

#Ex4

def executar_danca_robo():
    print("Passo para frente! Giro para a esquerda! Balança os braços!")
executar_danca_robo()
executar_danca_robo()

print("\n")

#Ex5

def iniciar_nova_rodada():
    print("--- INÍCIO DA NOVA RODADA ---")
    print("Preparem-se!")
iniciar_nova_rodada()

print("\n")

#Ex6

def preparar_bebida(bebida_escolhida):
    print(f"Preparando seu(ua) {bebida_escolhida}")
preparar_bebida(bebida_escolhida = "Café")
preparar_bebida(bebida_escolhida = "Chá")
preparar_bebida(bebida_escolhida = "Chocolate quente")

print("\n")

#Ex7

def saudar_visitante_personalizado(nome_do_visitante):
    print(f"Bem-vindo(a) {nome_do_visitante} Estamos felizes em vê-lo(a)!")
saudar_visitante_personalizado("Ana")
saudar_visitante_personalizado("Bruno")
saudar_visitante_personalizado("Carlos")

print("\n")

#Ex8

def enviar_sms(numero_destino, mensagem):
    print(f"Enviando para {numero_destino}: {mensagem}")
enviar_sms(numero_destino = "6137654", mensagem = "Favor comparecer ao RH")
enviar_sms(numero_destino = "5556777", mensagem = "Sua CNH está pronta")

print("\n")

#Ex9

def dobrar_ingrediente(ingrediente, quantidade_original):
    print(f"Para {ingrediente}, use {quantidade_original * 2} unidades")
dobrar_ingrediente(ingrediente = "Farinha", quantidade_original = 2)
dobrar_ingrediente(ingrediente = "Açúcar", quantidade_original = 0.5)

print("\n")

#Ex11

fruta = str(input("Qual é a fruta ?\n"))
def fazer_suco(fruta):
    meu_suco = f"Suco de {fruta} fresco!"
    print(meu_suco)

fazer_suco(fruta)

print("\n")

#Ex12

def verificar_idade(idade_pessoa, idade_minima):
    if idade_pessoa >= idade_minima:
        print("Pode entrar!")

        # condição de parada: só chama de novo se a idade for menor que 20
        if idade_pessoa < 20:
            verificar_idade(idade_pessoa=idade_pessoa+1, idade_minima=idade_minima)
        return True

    else:
        print("Entrada negada!")

        # condição de parada: só chama de novo se a idade for maior que 15
        if idade_pessoa > 15:
            verificar_idade(idade_pessoa=idade_pessoa-1, idade_minima=idade_minima)
        return False

# executa a primeira chamada
verificar_idade(idade_pessoa=17, idade_minima=18)

print("\n")

#Ex13

def calcular_media(nota1, nota2, nota3):
    media = float(nota1 + nota2 + nota3) / 3
    print(media)
calcular_media(nota1 = 6.0, nota2 = 7.0, nota3 = 8.0)

print("\n")

#Ex14

def reais_para_dolar(valor_reais, cotacao_dolar):
    valor_dolares = valor_reais / cotacao_dolar
    return valor_dolares
resultado = reais_para_dolar(500, 5.0)

print(f"O valor convertido é R${resultado:.2f} dolares")

print("\n")

#Ex15

def classificar_numero(numero):
    if numero > 0:
        return "Positivo"
    elif numero < 0:
        return "Negativo"
    elif numero == 0:
        return "Zero"
print(classificar_numero (5))
print(classificar_numero (-2))
print(classificar_numero (0))

print("\n")

#Ex16

def pedir_e_somar():
    numero1 = int(input("Digite o primeiro número\n"))
    numero2 = int(input("Digite o segundo número\n"))
    soma = numero1 + numero2
    print(f"O resultado da soma dos número é: {soma:.2f}")
pedir_e_somar()

print("\n")

#Ex17

def cadastrar_usuario():
    nome = str(input("Qual é o seu nome ?\n"))
    idade = int(input("Qual é a sua idade ?\n"))
    Lista = [nome,idade]
    print(f"Os seus dados são: {Lista}")
cadastrar_usuario()

print("\n")

#Ex18

def calcular_imc():
    peso = float(input("Qual é o seu peso ?\n"))
    altura = float(input("Qual é a sua altura ?\n"))
    imc = (peso / (altura * altura))
    print(f"O valor do IMC é: {imc:.2f}")
calcular_imc()

print("\n")

#Ex19

def verificar_login(usuario_correto = "Matheus", senha_correta = "123456"):

    nome_usuario = str(input("Digite o nome de usuário correto\n"))
    senha = str(input("Digite a senha correta\n"))
    if nome_usuario == usuario_correto and senha == senha_correta:
        return True
    else:
        return False

if verificar_login():
    print("Login bem-sucedido!\n")
else:
    print("Usuário ou senha incorretos!\n")

print("\n")

#Ex21

def gerar_mensagens_diarias(lista_nomes = ["Matheus" "Fernanda" "Henrique"]):
    for nome in lista_nomes:
        print(f"Bom dia, {nome}! Tenha um ótimo dia!\n")
        print(f"Bom dia, {nome}! Tenha um ótimo dia!\n")
        print(f"Bom dia, {nome}! Tenha um ótimo dia!\n")
meus_nomes = ["Matheus", "Fernanda", "Henrique"]
gerar_mensagens_diarias(meus_nomes)

print("\n")

#Ex22

def adicionar_lembrete(lista_lembretes = ["Amanhã tem aula!","não esqueça!"]):
    novo_lembrete = str(input("Digite um novo lembrete\n"))
    lista_lembretes.append(novo_lembrete)
    print(lista_lembretes)
adicionar_lembrete()

print("\n")

#Ex23

def jogar_adivinhacao(numero_secreto = 76543):
    tentativa = int(input("Digite o número secreto\n"))
    if tentativa < numero_secreto:
        print("Você errou! digitou um número menor\n")
    elif tentativa > numero_secreto:
        print("Você errou! digitou um número maior\n")
    else:
        print("Parabéns você acertou o número secreto!\n",numero_secreto)
jogar_adivinhacao()

print("\n")

#Ex26

import random
# biblioteca random que gera números aleatorios
def gerar_senha(tamanho):
    # "" gera uma string vazia, .join junta todos os caracteres gerados sem separação, random.choice escolhe aleatoriamente cada caractere pra formar uma senha aleatoria
    senha = "".join(random.choice("abcdefghijklmnopqrstuvwxyz123456789") for _ in range(tamanho))
    return senha

tamanho = int(input("Digite a quantidade de caracteres da senha que você deseja criar: "))

print(gerar_senha(tamanho))

print("\n")

#Ex27

def mostrar_tarefas(lista):
    if not lista:
        print("\nNenhuma tarefa na lista.")
    else:
        print("\nSuas tarefas:")
        for i, tarefa in enumerate(lista, start=1):
            print(f"{i}. {tarefa}")

def adicionar_tarefa(lista):
    nova_tarefa = input("\nDigite a nova tarefa: ")
    lista.append(nova_tarefa)
    print(f"Tarefa '{nova_tarefa}' adicionada com sucesso!")

def remover_tarefa(lista):
    mostrar_tarefas(lista)
    if not lista:
        return
    try:
        numero = int(input("\nDigite o número da tarefa que deseja remover: "))
        if 1 <= numero <= len(lista):
            removida = lista.pop(numero - 1)  # -1 porque índices começam em 0
            print(f"Tarefa '{removida}' removida com sucesso!")
        else:
            print("Número inválido!")
    except ValueError:
        print("Digite um número válido!")

minha_lista = []

while True:
    print("\n--- MENU ---")
    print("[1] Mostrar tarefas")
    print("[2] Adicionar tarefa")
    print("[3] Remover tarefa")
    print("[4] Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        mostrar_tarefas(minha_lista)
    elif opcao == "2":
        adicionar_tarefa(minha_lista)
    elif opcao == "3":
        remover_tarefa(minha_lista)
    elif opcao == "4":
        print("\nSaindo do programa... até logo!")
        break
    else:
        print("Opção inválida! Tente novamente.")

print("\n")

#Ex28

def ver_saldo(saldo_atual):
    print(f"O saldo atual é de:R$ {saldo_atual}\n")
    return saldo_atual

def depositar(saldo_atual, valor):
    novo_saldo = saldo_atual + valor
    print(f"O novo saldo é de:R$ {novo_saldo}\n")
    return novo_saldo

def sacar(saldo_atual, valor, saque):
    if saldo_atual < saque:
        print("Saldo atual insuficiente!\n")
        return saldo_atual
    novo_saldo_saque = saldo_atual - saque
    print(f"Saldo atual após saque:R$ {novo_saldo_saque}\n")
    return novo_saldo_saque

saldo = 500

while True:
    print("[1] -----> Ver saldo <----- ")
    print("[2] -----> Depositar <----- ")
    print("[3]   -----> Sacar <-----   ")
    print("[4]   -----> Sair  <-----   ")

    opcao = (input("Escolha a sua opção\n"))

    if opcao == "1":
        saldo = ver_saldo(saldo)
    elif opcao == "2":
        valor = float(input("Digite um valor para depósito\n"))
        saldo = depositar(saldo, valor)
    elif opcao == "3":
        saque = float(input("Digite um valor para saque\n"))
        saldo = sacar(saldo, valor, saque)
    elif opcao == "4":
        print("Encerrando o programa\n")
        break
    else:
        print("Opção inválida, tente novamente\n")

print("\n")

#Ex29

import random

def jogar_par_ou_impar(escolha_jogador):
    numero_computador = random.randint(1, 10)

    while True:
        try:
            numero_jogador = int(input("Escolha um número de 1 a 10: "))
            if 1 <= numero_jogador <= 10:
                break
            else:
                print("Número fora do intervalo! Tente novamente.")
        except ValueError:
            print("Digite um número válido!")

    soma = numero_jogador + numero_computador
    print(f"Você escolheu {numero_jogador}, o computador escolheu {numero_computador}. Soma = {soma}")

    resultado = "par" if soma % 2 == 0 else "ímpar"

    if resultado == escolha_jogador.lower():
        return "Ganhou!"
    else:
        return "Perdeu!"

def menu():
    while True:
        print("\n=== Jogo Par ou Ímpar ===")
        print("1 - Jogar")
        print("2 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            while True:
                escolha_jogador = input("Escolha 'par' ou 'ímpar': ").lower()
                if escolha_jogador in ["par", "ímpar"]:
                    break
                else:
                    print("Escolha inválida! Digite 'par' ou 'ímpar'.")
            resultado = jogar_par_ou_impar(escolha_jogador)
            print(f"Resultado: {resultado}")
        elif opcao == "2":
            print("Saindo do jogo. Até mais!")
            break
        else:
            print("Opção inválida! Tente novamente.")
menu()

print("\n")

#Ex30

def cadastrar_aluno():
    nome = input("Qual é o nome do aluno?\n")
    nota1 = float(input("Qual é a primeira nota do aluno?\n"))
    nota2 = float(input("Qual é a segunda nota do aluno?\n"))
    nota3 = float(input("Qual é a terceira nota do aluno?\n"))
    lista_aluno = [nome, nota1, nota2, nota3]
    return lista_aluno

def calcular_media_aluno(lista_aluno):
    media = (lista_aluno[1] + lista_aluno[2] + lista_aluno[3]) / 3
    return media

def mostrar_boletim(lista_aluno, media):
    print("\n=== Boletim do Aluno ===")
    print(f"Nome: {lista_aluno[0]}")
    print(f"Notas: {lista_aluno[1:]}")
    print(f"Média: {media:.2f}")
    print("========================\n")

todos_os_alunos = []

while True:
    aluno = cadastrar_aluno()
    todos_os_alunos.append(aluno)

    media = calcular_media_aluno(aluno)
    mostrar_boletim(aluno, media)

    continuar = input("Deseja cadastrar outro aluno? (s/n): ").lower()
    if continuar != 's':
        break

print("\n=== Resumo de Todos os Alunos ===")
for aluno in todos_os_alunos:
    media = calcular_media_aluno(aluno)
    mostrar_boletim(aluno, media)