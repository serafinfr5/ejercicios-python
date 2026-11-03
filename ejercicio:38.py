import time 

horas, minutos, segundos = 0, 0, 0
segundos_desde_inicio = 0

while True:
  time.sleep (1)
  segundos_desde_inicio += 1
  horas = segundos_desde_inicio // 3600
  minutos = segundos_desde_inicio % 3600 // 60
  segundos = segundos_desde_inicio %  60
print(f'Timer: {horas},{minutos},{segundos}')
