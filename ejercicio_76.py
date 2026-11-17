def EsMultiplo(num1, num2):
  if num2 != 0 and num1 % num2 == 0:
    return True
  else:
    retur False

numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))

if EsMultiplo(numero1, numero2):
  print("El primer número es multiplo del segundo.")
else:
  print("El primer número NO es multiplo del segundo.")
