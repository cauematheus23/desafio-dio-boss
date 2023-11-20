"""Crie uma variável para armazenar o nome e a quantidade de experiência (XP) de um herói, depois utilize uma estrutura de decisão para apresentar alguma das mensagens abaixo:

Se XP for menor do que 1.000 = Ferro
Se XP for entre 1.001 e 2.000 = Bronze
Se XP for entre 2.001 e 5.000 = Prata
Se XP for entre 6.001 e 7.000 = Ouro
Se XP for entre 7.001 e 8.000 = Platina
Se XP for entre 8.001 e 9.000 = Ascendente
Se XP for entre 9.001 e 10.000= Imortal
Se XP for maior ou igual a 10.001 = Radiante

## Saída

Ao final deve se exibir uma mensagem:
"O Herói de nome **{nome}** está no nível de **{nivel}**"""
def rank():
    if xp <= 1000:
        return 'Ferro'
    elif 1000 <  xp <= 2000:
        return 'Bronze'
    elif 2000 <  xp <= 5000:
        return 'Prata'
    elif 5000 <  xp <= 7000:
         return 'Ouro'
    elif 7000 <  xp <= 8000:
        return 'Platina'
    elif 8000 <  xp <= 9000:
        return 'Ascendente'
    elif 9000 <  xp <= 10000:
        return 'Imortal'
    elif xp > 10000:
        return 'Radiante' 
def prt():
    print(f"O Herói de nome \033[34m{nome}\033[m está no nivel de \033[34m{rank()}\033[m")

while True: 
    nome = str(input("Qual o nome do personagem? "))
    xp = int(input(f"Quantos de xp tem o \033[34m{nome}\033[m: "))
    prt()
    resp = str(input("Quer adicionar outro personagem? [S/N] ")).strip()
    if resp[0] not in 'Nn' :
        continue
        
    else:
        break
    

    
    