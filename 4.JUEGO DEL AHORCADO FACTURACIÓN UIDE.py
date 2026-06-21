# JUEGO DEL AHORCADO FACTURACIÓN UIDE
# Autor: Miguel Ángel Suárez Prada
# Objetivo: Reforzar los conocimientos impartidos en las diferentes capacitaciones

import random

# Diccionario que almacena las pistas y palabras
palabras = {
    "Documento emitido para cobrar un servicio": "FACTURA",
    "Escuela del estudiante": "CENTRODECOSTO",
    "Comprobante de pago realizado": "RECIBODECOBRO",
    "Documento para corregir una factura": "NOTACREDITO",
    "Formas de pago aceptadas": "TRANSFERENCIA"
}

# Selecciona aleatoriamente una pista y una palabra
pista, palabra = random.choice(list(palabras.items()))

# Lista donde se almacenan las letras correctas ingresadas
letras_adivinadas = []

print("====================================")
print(" AHORCADO DE FACTURACIÓN UIDE ")
print("====================================")
print("Pista:", pista)

# Bucle principal del juego (6 intentos)
for intentos in range(6, 0, -1):

    progreso = ""

    # Recorre cada letra de la palabra seleccionada
    for letra in palabra:

        # Verifica si la letra ya fue adivinada
        if letra in letras_adivinadas:
            progreso += letra + " "
        else:
            progreso += "_ "

    print("\nPalabra:", progreso)

    # Si ya no existen guiones bajos, el jugador ganó
    if "_" not in progreso:
        print("\n¡FELICITACIONES! HAS GANADO")
        break

    # Solicita una letra al usuario
    letra_usuario = input("Ingrese una letra: ").upper()

    # Validación: solo se permite una letra
    if len(letra_usuario) != 1:
        print("Error: Debe ingresar una sola letra.")
        continue

    # Validación: evita letras repetidas
    if letra_usuario in letras_adivinadas:
        print("Ya utilizó esa letra.")
        continue

    # Estructura condicional para verificar acierto o error
    if letra_usuario in palabra:

        # Guarda la letra correcta
        letras_adivinadas.append(letra_usuario)

        print("Correcto. La letra pertenece a la palabra.")

    else:

        print("Incorrecto.")
        print("Intentos restantes:", intentos - 1)

# Se ejecuta si el ciclo termina sin encontrar la palabra
else:
    print("\nHAS PERDIDO")
    print("La palabra correcta era:", palabra)

# Validación para jugar nuevamente
respuesta = input("\n¿Desea jugar nuevamente? (S/N): ").upper()

# Bucle while para validar la respuesta
while respuesta not in ["S", "N"]:
    respuesta = input("Ingrese únicamente S o N: ").upper()

if respuesta == "S":
    print("Reiniciando juego...")
else:
    print("Gracias por jugar.")
