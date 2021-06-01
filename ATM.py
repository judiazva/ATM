saldo = 0

print("\t.:MENU:.")
print("1.  Ingresar el dinero en la cuenta")
print("2.  Retirar el dinero en la cuenta")
print("3.  Mostrar el saldo de la cuenta")
print("4.  Salir")
opcion = int(input("Digite una opción: "))

print()

if opcion == 1:
    extra = float(input("¿Cuánto dinero desea ingresar? "))
    saldo += extra
    print("fDinero en la cuenta es de: ", saldo)
elif opcion == 2:
    retirar = float(input("¿Cuánto dinero desea ingresar? "))
    if retirar > saldo:
        print(f"Saldo insuficiente")
    else:
        saldo -= retirar
        print("Su saldo es de: ", saldo)
elif opcion == 3:
    print(f"Su saldo es de: ", saldo)
elif opcion == 4:
    print("Gracias por utilizar el cajero automático")
else:
    print("Opción inválida")



