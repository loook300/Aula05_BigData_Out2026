nota1 = float (input('informe a sua nota 1 :'))
nota2 = float (input('informe a sua nota 2 :'))
nota3 = float (input('informe a sua nota 3 :'))
nota4 = float (input('informe a sua nota 4 :'))

nota_total = nota1 + nota2 + nota3 + nota4

media = nota_total / 4

if media >= 7 :
    print ('Aprovado ')

elif media >= 5 :
   print ('Em Recuperação')

else:
  
  print ('Reprovado')
