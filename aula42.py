frase = 'Tonho é um gatinho muito lindo'

i = 0
qnt_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qnt_atual = frase.count(letra_atual)

    if qnt_apareceu_mais_vezes < qnt_atual:
        qnt_apareceu_mais_vezes = qnt_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{qnt_apareceu_mais_vezes}x'
)
