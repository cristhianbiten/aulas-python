hora = input('Digite a hora em números inteiros: ')

try:
    hora_int = int(hora)

    bom_dia = hora_int >= 0 and hora_int <= 11
    boa_tarde = hora_int >= 12 and hora_int <= 17
    boa_noite = hora_int >= 18 and hora_int <= 23

    if bom_dia:
        print('Bom dia')
    elif boa_tarde:
        print('Boa tarde')
    elif boa_noite:
        print('Boa noite')
    else:
        print('Não conheço essa hora')
except:
    print('você não digitou um número inteiro')