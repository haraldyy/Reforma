altura = int(input('Digite a altura da sala: '))
comprimento = int(input('Digite o comprimento da sala: '))
largura = int(input('Digite a largura: '))

ap = largura * comprimento
vs = largura * comprimento * altura
aps = 2 * altura * largura + 2 * altura * comprimento

print(f'A área do piso equivale a {aps}, o volume a {vs} e a área das paredes a {aps}')
