print("Bienvenido a la dulcería!")
print("\n")
print("Este es nuestro catálogo")
print("1. Chocolatina 2000")
print("2. Gomitas 2500")
print("3. Almendras 5000")
print("4. Salir")
precio_choc = int(2000)
precio_gom = int(2500)
precio_alm = int(5000)
chocolatina = "1"
gomitas = "2"
almendras = "3"
salir = "4"
print("\n")
opcion = str(input("Selecciona el número del producto que deseas llevar: "))
while (opcion == "1") or (opcion == "2") or (opcion == "3") or (opcion == "4"):
    if(opcion == chocolatina):
            cantidad = int(input("Cuantos productos de ese tipo desea llevar? "))
            if (cantidad > 0) and (cantidad <= 5):
                def sin_descuento(cantidad,precio_choc):
                    return int(cantidad*precio_choc)
                print("Su valor a pagar es de",sin_descuento(cantidad,precio_choc))
            elif (cantidad >5) and (cantidad <=10):
                def primer_descuento(cantidad,precio_choc):
                    valor_1 = int((cantidad*precio_choc)*0.05)
                    valor_2 = int((cantidad*precio_choc)- valor_1)
                    return valor_2
                print("Su valor a pagar es de",primer_descuento(cantidad,precio_choc))
            elif(cantidad > 10) and (cantidad <= 20):
                def segundo_descuento(cantidad,precio_choc):
                    valor_1 = int((cantidad*precio_choc)*(0.10))
                    valor_2 = int((cantidad*precio_choc)- valor_1)
                    return valor_2
                print("Su valor a pagar es de",segundo_descuento(cantidad,precio_choc))
            elif(cantidad > 20):
                def tercer_descuento(cantidad,precio_choc):
                    valor_1 = int((cantidad*precio_choc)*0.20)
                    valor_2 = int((cantidad*precio_choc)- valor_1)
                    return valor_2
                print("Su valor a pagar es de",tercer_descuento(cantidad,precio_choc))
    elif(opcion == gomitas):
            cantidadg = int(input("Cuantos productos de ese tipo desea llevar?"))
            if (cantidadg > 0) and (cantidadg <= 5):
                def sin_descuentog(cantidadg,precio_gom):
                    return int(cantidadg*precio_gom)
                print("Su valor a pagar es de",sin_descuentog(cantidadg,precio_gom))
            elif (cantidadg >5) and (cantidadg <=10):
                def primer_descuentog(cantidadg,precio_gom):
                    valorg_1 = int((cantidadg*precio_gom)*0.05)
                    valorg_2 = int((cantidadg*precio_gom)- valorg_1)
                    return valorg_2
                print("Su valor a pagar es de",primer_descuentog(cantidadg,precio_gom))
            elif(cantidadg > 10) and (cantidadg <= 20):
                def segundo_descuentog(cantidadg,precio_gom):
                    valorg_1 = int((cantidadg*precio_gom)*0.10)
                    valorg_2 = int((cantidadg*precio_gom)- valorg_1)
                    return valorg_2
                print("Su valor a pagar es de",segundo_descuentog(cantidadg,precio_gom))
            elif(cantidadg > 20):
                def tercer_descuentog(cantidadg,precio_gom):
                    valorg_1 = int((cantidadg*precio_gom)*0.20)
                    valorg_2 = int((cantidadg*precio_gom)- valorg_1)
                    return valorg_2
                print("Su valor a pagar es de",tercer_descuentog(cantidadg,precio_gom))
    elif(opcion == almendras):
            cantidada = int(input("Cuantos productos de ese tipo desea llevar? "))
            if (cantidada > 0) and (cantidada <= 5):
                def sin_descuentoa(cantidada,precio_alm):
                    return int(cantidada*precio_alm)
                print("Su valor a pagar es de",sin_descuentoa(cantidada,precio_alm))
            elif (cantidada >5) and (cantidada <=10):
                def primer_descuentoa(cantidada,precio_alm):
                    valora_1 = int((cantidada*precio_alm)*0.05)
                    valora_2 = int((cantidada*precio_alm)- valora_1)
                    return valora_2
                print("Su valor a pagar es de",primer_descuentoa(cantidada,precio_alm))
            elif(cantidada > 10) and (cantidada <= 20):
                def segundo_descuentoa(cantidada,precio_alm):
                    valora_1 = int((cantidada*precio_alm)*0.10)
                    valora_2 = int((cantidada*precio_alm)- valora_1)
                    return valora_2
                print("Su valor a pagar es de",segundo_descuentoa(cantidada,precio_alm))
            elif(cantidada > 20):
                def tercer_descuentoa(cantidada,precio_alm):
                    valora_1 = int((cantidada*precio_alm)*0.20)
                    valora_2 = int((cantidada*precio_alm)- valora_1)
                    return valora_2
                print("Su valor a pagar es de",tercer_descuentoa(cantidada,precio_alm))
    elif(opcion == salir):
        print ("Muchas gracias por su compra")
        break
    else:
            print("Digite un valor válido") 
    print("\n")
    print("Este es nuestro catálogo")
    print("1. Chocolatina 2000")
    print("2. Gomitas 2500")
    print("3. Almendras 5000")
    print("4. Salir")
    opcion = str(input("Selecciona el número del producto que deseas llevar: "))    
else:
    print("Digita una opción válida")