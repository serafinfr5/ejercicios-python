p1 = float(input("Nota primer parcial: "))
p2 = float(input("Nota segundo parcial: "))
p3 = float(input("Nota tercer parcial: "))
examen_final = float(input("Nota examen final: "))
trabajo_final = float(input("Nota trabajo final: "))

media_parciales = (p1 + p2 + p2) / 3
nota_final = ({media_parciales} * 0.55) + {examen_final} * 0.3 + {trabajo_final} * 0.15

print(f'La nota final de Algoritmos es: {nota_final:.2f}')
