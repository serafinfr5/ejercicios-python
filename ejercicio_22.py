import random

numero_secreto = random.randint(1,100)

print("Intenta adivinar un número al azar entre el 1 y al 100: ")

for intento_actual in range (1,11):

   print(f'\nIntento {intento_actual}/10')
   intento = int(input("Introduce tu número: "))

   if intento == numero_secreto:
       print(f'Has acertado en {intento_actual} intentos.')
       break
   elif intento < numero_secreto:
       print("Es mayor.")
   else:
       print("Es menor")
else:
    print(f'\nTe quedaste sin intentos. El número era {numero_secreto}')
