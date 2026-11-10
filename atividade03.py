compra = float (input('Informe valor da compra: '))
fidelidade =  (input('É cliente fidelidade ? [S/N]'))

if compra >200 or fidelidade == 's' or fidelidade == 'S':
    print(f'Frete Gratis')
    print(f'Valor final {compra}')
else:
    frete = compra +25 
    print(f'valor final {frete} R$')
