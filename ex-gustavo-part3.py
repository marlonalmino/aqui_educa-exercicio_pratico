# Faça um programa, utilizando while, que permita o usuário fazer contas de adição enquanto quiser.

# print('Operação - Adição!')

# while True:
#     number_one = int(input('Digite um número: '))
#     number_two = int(input('Digite outro número: '))
#     print(f'{number_one} + {number_two} = {number_one + number_two}')
    
#     resposta = input('Deseja realizar mais uma soma? [S ou N]\n').upper()
#     print(f'Resposta: {resposta}')

#     if resposta == 'S':
#         continue
#     if resposta == 'N':
#         break


# Faça um programa, utilizando while e listas, que permita o usuário realizar o cadastro de um número 
# indeterminado de pessoas enquanto quiser e os mostre na tela ao finalizar

# print('\nCADASTRO - PYTHON JOBS\n')
# print('Digite 0 para terminar o cadastro!\n')

# index = 1
# funcionarios = []

# while index != 0:
    
#     funcionario = input(f'Funcionário {index}: ')
#     index = index + 1

#     if funcionario == '0':
#         break
#     else:
#         funcionarios.append(funcionario)

# print(f'\nFuncionários: {funcionarios}')


# Faça um programa que imprima a quantidade de números pares entre dois números da sua escolha.

# count = int(input('\nPrimeiro número: '))
# count_resposta = count
# fim = int(input('Segundo número: '))
# list = []
# count_pares = 0

# if fim < count:
#     print('\nComeço maior que fim, tente novamente!')

# while count <= fim:
    
#     if count % 2 == 0:
#         list.append(count)
#         count_pares += 1
#     count += 1

# print(f'\nTotal de números pares entre {count_resposta} e {fim} é: {count_pares}\n')
# print(f'Números pares: {list}')


# Faça um programa que imprima a soma de todos os números pares entre dois números da sua escolha.

# count = int(input('\nPrimeiro número: '))
# count_resposta = count
# fim = int(input('Segundo número: '))
# list = []

# if fim < count:
#     print('\nComeço maior que fim, tente novamente!')

# while count <= fim:
    
#     if count % 2 == 0:
#         list.append(count)
#     count += 1

# soma = sum(list)

# print(f'\nNúmeros pares: {list}\n')
# print(f'Soma total dos números pares entre {count_resposta} e {fim} é: {soma}')