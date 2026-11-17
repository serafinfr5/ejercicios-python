def EscribirCentrado(texto):
  espacios = " " * (40 - len(texto) // 2)
  subrayado = "=" * len(texto)

  print(espacios + texto)
  print(espacios + subrayado)


mensaje = input("Introduce un texto para centrar: ")
EscribirCentrado(mensaje)
