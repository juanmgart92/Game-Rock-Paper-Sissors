import random

def obtener_opcion_oponente():
    opciones = {"piedra": 1, "papel": 2, "tijeras": 3}
    return random.choice(list(opciones.keys()))

def determinar_ganador(jugador, oponente):
    if jugador == oponente:
        return "Empate"
    elif (
        (jugador == "piedra" and oponente == "tijeras") or
        (jugador == "papel" and oponente == "piedra") or
        (jugador == "tijeras" and oponente == "papel")
    ):
        return "Ganaste"
    else:
        return "Perdiste"
    
# funcion para validar que el texto ingresado sea numerico
def validar_numero(texto):
    while True:
        try:
            numero = int(input(texto))
            return numero
        except ValueError:
            print("El valor ingresado no es un número. Por favor, intenta nuevamente.")

def jugar():
    puntaje = {"Ganaste": 0, "Perdiste": 0, "Empate": 0}

    while True:
        print("\nSelecciona una opción: ")
        print("1. Piedra")
        print("2. Papel")
        print("3. Tijeras")
        print("4. Salir")
        jugador = validar_numero("Tu elección: ")

        if jugador not in [1, 2, 3, 4]:
            print("Opción no válida. Por favor, elige entre piedra, papel o tijeras.")
            continue
        elif jugador == 4:
            print("Gracias por jugar. ¡Hasta luego!")
            break
    
        oponente = obtener_opcion_oponente()
        resultado = determinar_ganador(jugador, oponente)

        print(f"\nTu elección: {jugador}")
        print(f"Elección del oponente: {oponente}")
        print(f"Resultado: {resultado}")

        puntaje[resultado] += 1

        print(f"| \nPuntaje actual - Ganaste: {puntaje['Ganaste']} | Perdiste: {puntaje['Perdiste']} | Empate: {puntaje['Empate']}\n |")

        jugar_nuevamente = input("¿Quieres jugar de nuevo? (s/n): ").lower()

        if jugar_nuevamente != 's':
            print("Gracias por jugar. ¡Hasta luego!")
            break

        
if __name__ == "__main__":
    print("""
__________               __            __________                                        _________      .__                            
\______   \ ____   ____ |  | __        \______   \_____  ______   ___________           /   _____/ ____ |__| ______ _________________  
 |       _//  _ \_/ ___\|  |/ /  ______ |     ___/\__  \ \____ \_/ __ \_  __ \  ______  \_____  \_/ ___\|  |/  ___//  ___/  _ \_  __ \ 
 |    |   (  <_> )  \___|    <  /_____/ |    |     / __ \|  |_> >  ___/|  | \/ /_____/  /        \  \___|  |\___ \ \___ (  <_> )  | \/ 
 |____|_  /\____/ \___  >__|_ \         |____|    (____  /   __/ \___  >__|            /_______  /\___  >__/____  >____  >____/|__|    
        \/            \/     \/                        \/|__|        \/                        \/     \/        \/     \/              
    """)
    print("¡Bienvenido al juego de piedra, papel o tijeras!")
    jugar()