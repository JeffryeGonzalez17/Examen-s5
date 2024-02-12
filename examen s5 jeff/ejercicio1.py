import random

numero_secreto = random.randint(1, 100)
intentos = 0

while True:
    intento = int(input("Adivina el número entre 1 y 100: "))
    intentos += 1

    if intento == numero_secreto:
        print("¡Muy bien, haz acertadooo! Lo has adivinado en: ", intentos, "intentos.")
        break
    elif intento < numero_secreto:
        print("El número es mayor.")
    else:
        print("El número es menor.")