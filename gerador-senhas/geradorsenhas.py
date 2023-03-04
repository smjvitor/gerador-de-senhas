import random
import string
import pickle
import os

ARQSENHA = 'senhas.pkl'

def gerarSenha(tamanho, maiusculas=True, minusculas=True, numeros=True, simbolos=True):
    caracteres = ''
    if maiusculas:
        caracteres += string.ascii_uppercase
    if minusculas:
        caracteres += string.ascii_lowercase
    if numeros:
        caracteres += string.digits
    if simbolos:
        caracteres += string.punctuation

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))

    try:
        with open(ARQSENHA, 'rb') as f:
            senhas = pickle.load(f)
    except FileNotFoundError:
        senhas = []

    senhas.append(senha)

    with open(ARQSENHA, 'wb') as f:
        pickle.dump(senhas, f)

    print(f'Senha gerada é: {senha}')

def verSenhas():
    try:
        with open(ARQSENHA, 'rb') as f:
            senhas = pickle.load(f)
    except FileNotFoundError:
        print('Não existe senha gerada.')
        return

    if not senhas:
        print('Não existe senha gerada.')
        return

    print('Senhas geradas anteriormente:')
    for senha in senhas:
        print(senha)

def apagarSenhas():
    try:
        os.remove(ARQSENHA)
    except FileNotFoundError:
        pass

    print('Senhas anteriores apagadas com sucesso.')

while True:
    print('-----Menu-----')
    print('1 - Gerar nova senha')
    print('2 - Mostrar senhas geradas')
    print('3 - Apagar TODAS as senhas geradas')
    print('4 - Sair')

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        tamanho = int(input('Qual tamanho da senha: '))
        maiusculas = input('Deseja letras maiúsculas? (s/n): ') == 's'
        minusculas = input('Deseja letras minúsculas? (s/n): ') == 's'
        numeros = input('Deseja números? (s/n): ') == 's'
        simbolos = input('Deseja símbolos? (s/n): ') == 's'
        gerarSenha(tamanho, maiusculas, minusculas, numeros, simbolos)
    elif opcao == '2':
        verSenhas()
    elif opcao == '3':
        apagarSenhas()
    elif opcao == '4':
        break
    else:
        print('Opção inválida.')