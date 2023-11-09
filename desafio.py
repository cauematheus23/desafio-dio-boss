nome = str(input("Qual o nome do personagem? "))
xp = int(input(f"Quantos de xp tem o {nome}"))
rank = ''
while True:
    if xp <= 1000:
        rank = 'Ferro'
