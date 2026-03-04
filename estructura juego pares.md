python -m pip install jupyterlab ipykernel pandas lxml html5lib**Crear un juego donde el programa piensa un número aleatorio entre 1 y 100, y el usuario debe adivinarlo recibiendo pistas.**

**Pasos a seguir**

1.- Introducir una número por el usario  
2.- Que el ordenador pueda interpretar si es un numero par o no  
3.- Volver a probar las veces que quieras 
  


**Lista de tareas**

1.- Generar un valor para decirle al usuario que ingrese un valor numerico 
2.- Guardar el número generado  
3.- Si el valor numerico no es un numero,  decir que es un error y volver a intentarlo
    3.1- Si el numero es par , decir es par
    3.2- Si el numero no es par, decir es impar  
    
4.- Permitir volver a probar   

**Extructuras**

1.- Bucles
    1.1- Intentos del usuario -> while true juan no trolee  
2.- Condicionales  
    2.1- Validar número: try / except  
    2.2- Intento correcto: if, elif, else  

**Que variables se necestian**

1.- ingresa un valor numerico ->  int()  
2.- si no ingresa decirle "esto no es un numero" -> try/except
    mientras sea un numero
3.- si ingresa y es par -> if + saber si es par  
4.- si no es paro -> decir es impar   
5.- imprimir . esto juan lo hace en 36 lineas print?

**Pseudo Codigo**

1  Presentar el juego ----> Print "bienvenido al juego de los pares o nones"
2  Pedir numero y que no te trolee juan WHILE TRUE
    2.1 si no ingresa un numero, decirle que lo vuelva pedir TRY/BREAK
    2.2 No me mientas ingresa un numero "  EXCEPT
3 El juego ,si es par decir par si es impar decir impar----> 
    3.1instruccion if + funcion impar e imprimir es par
    3.2 Si no es, ELSE imprimir es impar
   
  







