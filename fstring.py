# teste = 'Ari ari'
# # print(teste.capitalize())#capitalize: põe a primeira letra em maiúscula
# # print(teste.upper())#upper: põe o conteúdo da variável todo em maiuscula
# # print(teste.casefold())#casefold: põe o conteúdo da variável todo em minúscula
# # print(len(teste))#len: verifica a quantidade de caracteres
# # print(teste[:3])#índice inicial e final
# # print(teste[::-1])#nome de trás para frente
# # print(teste[0:3])#índice inicial e índice final
# # print(teste.zfill(20))
# # print(f'{teste:-^40}')
# print('a' in teste)
# print('A' in teste)#in: verifica se o item ou letra está contido
# # print(teste.startswith('t'))
# # print(teste.startswith('a'))#startswith: começa com
# print(teste.endswith('i'))#endswith: termina com
#import os -- os.system('cls'): para limpar a tela à cada iteração do programa
#if operacao not in operadores_permitidos:
        # print('Operador inválido!')
        # continue: in ou not in para analisar se determinado caracter está ou não contido da variável
#import time:
    # time.sleep(5): determina o tempo para executar a próxima ação
# print(teste.count('carro'))#conta quantas vezes a palavra apareceu no texto

# texto = 'Python' para exibir na tela letra e número correspondente

# i = 0
# tamanho_string = len(texto)

# while i < tamanho_string:
#     print(texto[i], i)
#     i += 1
    
# texto = 'fim do programa'

# novo_texto = ''

# for letra in texto:
#     novo_texto += f'*{letra}'
#     print(letra)
# print(novo_texto)

#import random = random.randint(1,60) para retornar um número inteiro aleatório entre 1 e 100

# #função RANGE (start, stop, step) ou (onde começa, onde termina e intervalos)
# numeros = range(0,11, 1)

# for numero in numeros:#lê-se: para cada NUMERO em NÚMEROS faça:
#     print(numero, end=' * ')#end altera o valor padrão do end(\n) que é quebra de linha

# import random #usado para sortear algo
# import string #usado para sortear algo do objeto string

# letra = random.choice(string.ascii_uppercase) #string.ascii usa o alfabeto de a à z
#                                             #uppercase = maiúsculas e lowercase = minúsculas
# print("Letra sorteada:", letra)


# for i in range(1,11):
#     if i %2==0:
#         print(f'{i} é par!') #para exibir apenas os números pares da sequência

#PARA GARANTIR APENAS LETRAS E ESPAÇOS:
# while not all(parte.isalpha() for parte in aluno.split()):#parte.isalpha garante apenas letras 
#                                                         #.split garante letras com espaços
#         print("Entrada inválida! Digite apenas letras, sem números ou símbolos.")
#         aluno = input("Tente novamente: ")


#EXEMPLO ANINHAMENTO DE FOR:
# for i in range(1,6):
#     for j in range(1,6):
#         if (i + j) % 2==0:
#             print(f'{i} + {j} é PAR!')
#         else:
#             print(f'{i} + {j} é ÍMPAR!')

#manipulação de strings

# frase = input("Digite uma frase: ")

# print("Maiúsculas:", frase.upper())
# print("Minúsculas:", frase.lower())
# print("Capitalizado:", frase.title())

#função SUM para somar os itens de uma lista, tupla, etc

gastos_joao = [300, 500, 200, 800]
gastos_pedro = [200, 400, 500, 700]

total_joao = sum(gastos_joao)
total_pedro = sum(gastos_pedro)
print(total_pedro)
print(total_joao)