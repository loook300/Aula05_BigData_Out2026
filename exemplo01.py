pedido = float (input('Informe o Valor do pedido : '))
km = float (input('Informe a Distancia : '))
frete = 8 

if pedido > 50 and km <= 3 :
   valor_final = pedido
   print('Frente Gratis !')

else:
   valor_final = pedido + 8 
   print(f'Frete de R$ {frete}')
   print(f'Valor Final :  R$ {valor_final:.2f}')
   