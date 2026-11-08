frase = input("Introduce una frase: ")
letra_buscada = input("Introduce la letra a buscar: ")

contador = 0

for letra in frase:
    if letra == letra_buscada:
        contador = contador + 1

print(f'La letra "{letra_buscada}" aparece {contador} veces.')
