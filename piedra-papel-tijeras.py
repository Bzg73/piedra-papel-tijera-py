nombre1 = input("¿nombre del jugador 1?: ")
nombre2 = input("¿nombre del jugador 2?: ")

jugador1 = input(f"{nombre1}, ¿Qué eliges?¿Piedra,papel, o tijera?: ").lower()
jugador2 = input(f"{nombre2}, ¿Qué eliges?¿Piedra,papel, o tijera?: ").lower()

condicion1 = jugador1 == "piedra" and jugador2 == "tijera"
condicion2 = jugador1 == "papel" and jugador2 == "piedra"
condicion3 = jugador1 == "tijera" and jugador2 == "papel"

if jugador1 == jugador2:
    print("EMPATE!")
elif condicion1 or condicion2 or condicion3:
    print(f"GANO {nombre1}")

else:
    print (f"GANO {nombre2}") 
