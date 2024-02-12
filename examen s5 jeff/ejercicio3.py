def sum_dig(numero): 
    numero = str(numero)
    suma = 0
    for i in numero:
        suma += int(i)
    return suma

numero = int(input("ingrese un numero de más de dos digitos: "))

sum_2_dig = sum_dig(numero)

suma_final = int(sum_2_dig)

print(sum_2_dig) 
