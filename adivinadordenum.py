import random
numero_secreto = random.randint(1, 20)
adivinado = False
while not adivinado:
    intento = int(input("adivina en numero (1-20): "))
    if intento <numero_secreto:
        print("demasiado bajo")
    elif intento > numero_secreto:
        print("demasiado alto")
    else:
        print("muy bien. eso es correcto")
        adivinado = True
                