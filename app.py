print("Sabor Express\n")

print('1. Cadastrar restaurante')
print('2. Listar restaurante')
print('3. Ativar restaurante')
print('4. Sair restaurante\n')

opcao_escolhida = int(input('Escolha uma opção: '))

if  opcao_escolhida == 1:
    print('Cadastrar restaurante: ')
elif opcao_escolhida == 2:
    print('Listar restaurantes: ')
elif opcao_escolhida == 3:
    print('Ativar restaurante: ')
else:
    print('Encerrando o programa')