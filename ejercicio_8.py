sueldo_base = float(input("Sueldo base: "))
venta1 = float(input("Importe venta 1: "))
venta2 = float(input("Importe venta 2: "))
venta3 = float(input("Importe venta 3: "))

comisiones = (venta1 + venta2 + venta3) * 0.10
total_mes = sueldo_base + comisiones

print (f'Ganancia por comisiones: {comisiones:.2f}')
print (f'Sueldo total del mes: {total_mes:.2f}')
