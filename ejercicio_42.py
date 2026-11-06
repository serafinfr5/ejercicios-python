cadena = input ('Introduce el texto principal: ')
subcadena = input('Introduce el texto por el cual crees que empieza: ')

if cadena.startswith(subcadena):
   print(f'El texto comienza por esa subcadena.')
else:
   print(f'El texto no empieza por esa subcadena.')
