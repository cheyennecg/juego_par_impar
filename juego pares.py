# Presentar el juego
print("Bienvenido al juego de pares o nones")
# Iniciamos bucle para asegurar que tenemos un número válido
#Extra porque no entendia bien los bucles
while True: #BUCLE PARA QUE JUAN MALEFICO NO ME TROLEE EL JUEGO
     try: #una tabulación porque esta dentro del bucle
        # Si el jugador  intenta ingresar un valor numerico
        ingresa_numero = int(input("Ingresa un número: "))
        # Si es un número, paramos el bucle y salimos
        break
     except: # si no es un numero y es un texto
        # dentro del bucle porque va con try 
        print("No me mientas, ingresa un numero")

#"adivinar si es par o impar " EL JUEGO
if ingresa_numero % 2 == 0:
 print("Es un número par!")
else:
 print("Es un número impar!")
