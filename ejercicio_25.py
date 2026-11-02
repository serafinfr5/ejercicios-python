while True:
    caracter = input("Introduce un carácter: ")
    if caracter == " ":
        break
        
    if caracter.upper() in "AEIOU":
        print("VOCAL")
    else:
        print("NO VOCAL")
print("Fin.")
