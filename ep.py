print('''Sabor Express
''')

print('1- cadastro restauranre')
print('2- listar restaurante')
print('3- cadastrar restaurante')
print('4- sair\n')

# convertendo string em int
opcao_escolhida = int(input('Escolha uma opcao:'))
print('vc escolheu', opcao_escolhida)
# print(f'voce escolheu a opcao {opcao_escolhida}')

if opcao_escolhida == 1 :
    print('cadastrar restaurante')
    elif opcao_escolhida == 2:
        print('listar restaurante')
        elif opcao_escolhida == 3:
            print('ativar restaurante')
            else:
                print('sair')
