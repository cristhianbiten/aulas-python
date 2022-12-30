entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitda = '1234'

if entrada == 'E' and senha_digitada == senha_permitda:
    print('Entrar')
else:
    print('Sair')