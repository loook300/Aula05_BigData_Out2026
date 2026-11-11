
numero = float(input("Escolha uma opção: "))


match numero:
 case numero if numero > 1 :
        print('Positivo ')
 case numero  if numero <0 :
        print('negativo ')
 case numero if  numero == 0  :
        print('Zero ')