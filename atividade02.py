nota_final = float (input('informe sua Nota: '))
frequencia = float (input('Frequencia: '))
mensalidade = float (input('Informe valor da mensalidade: '))


if nota_final >= 7 or frequencia >=75 :
    bolsa = mensalidade * 0.20 
    print(f'voce possui bolsa {bolsa}')
else :
    print('Voce nao possui bolsa ')
