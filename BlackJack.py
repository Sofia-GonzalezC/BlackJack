import random

As = 1
J = 11
Q = 12
K = 13

cartas = {As: 'As', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', J: 'J', Q: 'Q', K: 'K'}

palos_jugador_cartas1 = random.choice(["♥", "♣️", "♠️", "♦️"])
palos_jugador_cartas2 = random.choice(["♥", "♣️", "♠️", "♦️"])

palos_crupier_cartas1 = random.choice(["♥", "♣️", "♠️", "♦️"])
palos_crupier_cartas2 = random.choice(["♥", "♣️", "♠️", "♦️"])


jugador_cartas1 = random.choice([As, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K])
crupier_cartas1 = random.choice([As, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K])

jugador_cartas2 = random.choice([As, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K])
crupier_cartas2 = random.choice([As, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K])

print("-"*34)
print("Jugador saca su primera carta:", cartas[jugador_cartas1] + palos_jugador_cartas1)
print("Crupier saca su primera carta:", cartas[crupier_cartas1] + palos_crupier_cartas1)
print("-"*34)

sacar_carta2 = input("Desea sacar la segunda carta?, ingrese 'Si' para sacar la carta, ingrese 'No' para no sacar: ")
sacar_cartalower = sacar_carta2.lower()

if sacar_cartalower == 'si':
    print("-"*34)
    print("Jugador saca su segunda carta:", cartas[jugador_cartas2] + palos_jugador_cartas2)
    print("\nCrupier saca su segunda carta:", cartas[crupier_cartas2] + palos_crupier_cartas2)
    print("-"*34)

    puntos_jugador = jugador_cartas1 + jugador_cartas2
    puntos_crupier = crupier_cartas1 + crupier_cartas2

    print("+"*34)
    print("Jugador sacó:", cartas[jugador_cartas1] + palos_jugador_cartas1, "y", cartas[jugador_cartas2] + palos_jugador_cartas2, "\npuntos en total:", puntos_jugador)
    print("+"*34)
    print("Crupier sacó:", cartas[crupier_cartas1] + palos_crupier_cartas2, "y", cartas[crupier_cartas2] + palos_crupier_cartas2, "\npuntos en total:", puntos_crupier)
    print("+"*34)

    print("_"*34)
    if puntos_jugador <= 21 and puntos_jugador > puntos_crupier or puntos_crupier > 21:
        print("Jugador gano, Crupier Perdió")
    elif puntos_crupier <= 21 and puntos_crupier > puntos_jugador or puntos_jugador > 21:
        print("Crupier gano, Jugador Perdió")
    elif puntos_jugador == puntos_crupier:
        print("Hubo un Empate")
    print("_"*34)

elif sacar_cartalower == 'no':
    print("-"*34)
    print("Crupier saca su segunda carta:", cartas[crupier_cartas2] + palos_crupier_cartas2)
    print("-"*34)

    puntos_jugador = jugador_cartas1
    puntos_crupier = crupier_cartas1 + crupier_cartas2

    print("+"*34)
    print("Jugador sacó:", cartas[jugador_cartas1] + palos_jugador_cartas1, "\npuntos en total:", puntos_jugador)
    print("+"*34)
    print("Crupier sacó:", cartas[crupier_cartas1] + palos_crupier_cartas2, "y", cartas[crupier_cartas2] + palos_crupier_cartas2, "\npuntos en total:", puntos_crupier)
    print("+"*34)

    print("_"*34)
    if puntos_jugador <= 21 and puntos_jugador > puntos_crupier or puntos_crupier > 21:
        print("Jugador gano, Crupier Perdió")
    elif puntos_crupier <= 21 and puntos_crupier > puntos_jugador or puntos_jugador > 21:
        print("Crupier gano, Jugador Perdió")
    elif puntos_jugador == puntos_crupier:
        print("Hubo un Empate")
    print("_"*34)

else:
    print("Debe ingresar 'Si' o 'No'")
    sacar_carta2 = ""
    while sacar_cartalower != 'si' or sacar_cartalower != 'no':
        sacar_carta2 = input("Desea sacar la segunda carta?, ingrese 'Si' para sacar la carta, ingrese 'No' para no sacar: ")
        sacar_cartalower = sacar_carta2.lower()
        if sacar_cartalower == 'si':
            print("-"*34)
            print("Jugador saca su segunda carta:", cartas[jugador_cartas2] + palos_jugador_cartas2)
            print("-"*34)
            print("Crupier saca su segunda carta:", cartas[crupier_cartas2] + palos_crupier_cartas2)
            print("-"*34)

            puntos_jugador = jugador_cartas1 + jugador_cartas2
            puntos_crupier = crupier_cartas1 + crupier_cartas2

            print("+"*34)
            print("Jugador sacó:", cartas[jugador_cartas1] + palos_jugador_cartas1, "y", cartas[jugador_cartas2] + palos_jugador_cartas2, "\npuntos en total:", puntos_jugador)
            print("+"*34)
            print("Crupier sacó:", cartas[crupier_cartas1] + palos_crupier_cartas2, "y", cartas[crupier_cartas2] + palos_crupier_cartas2, "\npuntos en total:", puntos_crupier)
            print("+"*34)

            print("_"*34)
            if puntos_jugador <= 21 and puntos_jugador > puntos_crupier or puntos_crupier > 21:
                print("Jugador gano, Crupier Perdió")
            elif puntos_crupier <= 21 and puntos_crupier > puntos_jugador or puntos_jugador > 21:
                print("Crupier gano, Jugador Perdió")
            elif puntos_jugador == puntos_crupier:
                print("Hubo un Empate")
            print("_"*34)
            break

        elif sacar_cartalower == 'no':
            print("-"*34)
            print("Crupier saca su segunda carta:", cartas[crupier_cartas2] + palos_crupier_cartas2)
            print("-"*34)

            puntos_jugador = jugador_cartas1
            puntos_crupier = crupier_cartas1 + crupier_cartas2

            print("+"*34)
            print("Jugador sacó:", cartas[jugador_cartas1] + palos_jugador_cartas1, "\npuntos en total:", puntos_jugador)
            print("+"*34)
            print("Crupier sacó:", cartas[crupier_cartas1] + palos_crupier_cartas2, "y", cartas[crupier_cartas2] + palos_crupier_cartas2, "\npuntos en total:", puntos_crupier)
            print("+"*34)

            print("_"*34)
            if puntos_jugador <= 21 and puntos_jugador > puntos_crupier or puntos_crupier > 21:
                print("Jugador gano, Crupier Perdió")
            elif puntos_crupier <= 21 and puntos_crupier > puntos_jugador or puntos_jugador > 21:
                print("Crupier gano, Jugador Perdió")
            elif puntos_jugador == puntos_crupier:
                print("Hubo un Empate")
            print("_"*34)
            break
