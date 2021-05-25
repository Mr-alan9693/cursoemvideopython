A = int(input('Digite o primeiro numero: '))
B = int(input('Digite o segundo numero: '))
C = int(input('Digite o terceiro numero: '))
if A>B and A>C:
    maior = A
if B>C and B>A:
    maior = B
if C>A and C>B:
    maior = C
print('O maior valor digitado foi {}'.format(maior))
