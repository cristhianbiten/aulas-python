
while True:
    numero_1 = input('Digite o primeiro número: ')
    numero_2 = input('Digite o segundo número: ')
    operador = input('Digite o operador [+-*/]: ')

    numeros_validos = None
    numero_1_float = 0
    numero_2_float = 0

    try:
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou dois número errados, digite novamente')
        continue

    operadores_validos = '+-*/'

    if operador not in operadores_validos:
        print('Operador inválido')
        continue

    if len(operador) > 1:
        print('Digite somente um operador')
        continue

    if operador == '+':
        print(numero_1_float + numero_2_float)
    elif operador == '-':
        print(numero_1_float - numero_2_float)
    elif operador == '*':
        print(numero_1_float * numero_2_float)
    elif operador == '/':
        print(numero_1_float / numero_2_float)
    else:
        print('Nunca deveria ter chego aqui')

    sair = input('Quer sair? ').lower().startswith('s')
    if sair is True:
        break
