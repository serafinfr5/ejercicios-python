notas = []

for i in range(1, 6):
    nota = float(input(f"Introduce la nota {i} (de 0 a 10): "))
    notas.append(nota)

suma_total = sum(notas)
media = suma_total / 5
nota_maxima = max(notas)
nota_minima = min(notas)

print(f'\nTodas las notas introducidas: {notas}')
print(f'Nota media: {media}')
print(f'Nota más alta: {nota_maxima}')
print(f'Nota más baja: {nota_minima}')
