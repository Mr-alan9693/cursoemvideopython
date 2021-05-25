import emoji
print(emoji.emojize('Olá mundo,\033[34m:earth_americas:\033[m',use_aliases=True))
nome = input('Qual é o seu nome? ')
print('\033[35mÉ um grande prazer em te conhecer', nome)

