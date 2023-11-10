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
    

    
    