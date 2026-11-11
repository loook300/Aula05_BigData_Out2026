  #Estrutura Match Case
print(''' 
[1] - Marketing
[2] - financeiro
[3 a 5] - Administração
[6 a 9] - Ti
[10 a 20] - Serviços Gerais 

''')

opcao = int(input("Escolha uma opção: "))

#Estrutura Match Case

match opcao:
    case 1:
        print('Marketing')
    case 2:
            print('financeiro')
    case 3 |4 |5:
            print('Administração')
    case opcao if 6 <= opcao <= 9 :
            print ('Ti')
    case opcao if 10 <= opcao <= 20 :
            print('Serviços Gerais')
    case _:
              print('Opção Invalida')