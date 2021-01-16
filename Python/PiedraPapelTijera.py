import random  
ob = ["Piedra", "Papel", "Tijera"]
c = 0
p = 0
print("Puntaje: Computadora " + str(c) + " Jugador " + str(p) + "\n")

run = True
while run:
    b = False
    computadora = random.choice(ob)
    jugador = input("Elija entre piedra , papel , tijera o S/s para salir: ")
    jugador = jugador.lower()
    if computadora == jugador:
        print("Empate!")
        b = True        
    elif jugador == "piedra":
        if computadora == "Tijera":
            print("Gano El Jugador!")
            p += 1
        else:
            print("Gano La Computadora!")
            c += 1
        b = True
    elif jugador == "papel":
        if computadora == "Piedra":
            print("Gano El Jugador!")
            p += 1
        else:
            print("Gano La Computadora!")
            c += 1
        b = True
    elif jugador == "tijera":
        if computadora == "Papel":
            print("Gano El Jugador!")
            p += 1
        else:
            print("Gano La Computadora!")
            c += 1
        b = True
    elif jugador == "s":
        break
    else:
        print("¡Opcion Ingresada Invalida!")
    if b:
        print("Jugador: " , jugador)
        print("Computador: " , computadora)
        print("\n Puntaje: Computadora " + str(c) + " Jugador " + str(p) + "\n")

