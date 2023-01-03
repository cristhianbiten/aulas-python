"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x e X - hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou -
Ex.: 0>-100,.1f
Convertion flags - !r !s !a
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{1000.8946546198746:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')
