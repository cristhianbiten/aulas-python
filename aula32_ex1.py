numero = input('Digite um número inteiro: ')

if numero.isdigit():

    numero_int = int(numero)
    if numero_int % 2 == 0:
        print('Este número é par')
    else:
        print('Este número é ímpar')

else:
    print('Você não digitou um número inteiro')
