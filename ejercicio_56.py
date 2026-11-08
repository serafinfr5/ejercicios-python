nombre_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
dias_meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

num_mes = int(input("Introduce el número de un mes (1 al 12): "))

posicion = num_mes - 1

print(f'El mes es {nombre_meses[posicion]} y tiene {dias_meses[posicion]} días.')
