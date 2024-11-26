print("Bienvenido a la dulcería!")
print("Este es nuestro catálogo")
print("1. Chocolatina 2000")
print("2. Gomitas 2500")
print("3. Almendras 5000")
precio_choc = int(2000)
precio_gom = int(2500)
precio_alm = int(5000)
opcion = str(input("Selecciona uno o más productos: "))
if (opcion == "1") or (opcion == "2") or (opcion == "3"):
   print("Seguir")
else:
   print("Gracias por vistarnos! Hasta luego")