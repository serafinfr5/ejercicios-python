def Login(usuario,contraseña,intentos):
  if usuario == "usuario1" and contraseña == "asdasd":
    return True, intentos
  else:
    intentos = intentos + 1
    return False, intentos

intentos = 0
acceso = False

while intentos < 3 and acceso == False:
  usuario = input("Introduce el usuario: ")
  contrasena = input("Introduce la contraseña: ")
  
  #Sin esto no me cuenta los intentos, pero no la veo.¡DUDA!
  acceso, intentos = Login(usuario, contrasena, intentos) 
  
  if acceso == True:
     print ("Acceso Permitido.")
  else:
     print("Usuario o Contraseña incorrectas.")
     print("Intentos restantes: ", 3-intentos)
if acceso == False:
  print("Has agotado los intentos.")
