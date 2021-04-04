from util import leer_instrucciones
from logica import *
from criptograma import *
from ahorcado import *
from adivinanza import *
from jugador import *
from palabras import *
from quizzi import *
from python import *
from booleana import *
#import sopa
from objetos import Objetos
#objetos = objeto
import imagenes
import escoge_numero
import time
import booleana
import os
import json

mochila = []


def empezar_juego(): #Iniciar sesion y elegir nivel de dificultad

    usuario =input('Intruzca su usuario: ')
    jugadores = obtener_usuarios()
    usuarios = [u['usuario'] for u in jugadores]
    usuario_valido = False
    jugador = None
    while not usuario_valido:
        if usuario in usuarios:
            print('Usuario valido')
            jugador = obtener_jugador(usuario, jugadores)
            usuario_valido = True
        else:
            print('Este usuario no existe, presione 1 para registrarse')
            main()
    clave = input('Intruzca la clave: ')
    clave_valida = False
    while not clave_valida:
        if jugador.clave == clave:
            print('Clave correcta')
            clave_valida = True
        else:
            print('Clave Incorrecta')
            respuesta =input('''
            PRESIONE:
            1. Para ir al menu
            2.Para ingresar la clave nuevamente
            ''')
            if respuesta == 1:
                main()
            else:
                clave = input('Intruzca la clave: ')
                
    print('Ingrese nivel de dificultad a jugar: ')
    nivel = input('''
    1.Fácil: 5 vidas y 5 pistas. 45 minutos
    2.Medio: 3 vidas y 3 pistas. 35 minutos
    3.Difícil: 1 vida y 2 pistas. 25 minutos
    ''')
    while nivel != '1' and nivel != '2' and nivel != '3':
        nivel = input('''
        Ingrese un nivel valido:
        1.Fácil: 5 vidas y 5 pistas. 45 minutos
        2.Medio: 3 vidas y 3 pistas. 35 minutos
        3.Difícil: 1 vida y 2 pistas. 25 minutos
        ''')
    
    if nivel == '1':
        tiempo_inicial = time.time()
        fin_juego = tiempo_inicial + (60*45)
        while time.time() < fin_juego:
            nivel_uno(jugador, tiempo_inicial)
        print('Tiempo agotado')
        main()


    elif nivel == '2':
        tiempo_inicial = time.time()
        fin_juego = tiempo_inicial + (60*35)
        while time.time() < fin_juego:
            nivel_dos(jugador, tiempo_inicial)
        print('Tiempo agotado')
        main()

       
    else:
        tiempo_inicial = time.time()
        fin_juego = tiempo_inicial + (60*25)
        while time.time() < fin_juego:
            nivel_tres(jugador, tiempo_inicial)
        print('Tiempo agotado')  
        main()

def nivel_uno(jugador, tiempo_inicial): #Inicio del juego mas facil
    vidas = 5
    if vidas <= 0:
        print('Te quedaste sin vidas')
    print('''
      Hoy 5 de marzo de 2021, la Universidad sigue en cuarentena (esto no es novedad), 
     lo que sí es novedad es que se robaron un Disco Duro de la Universidad del cuarto
     de redes que tiene toda la información de SAP de estudiantes, pagos y  asignaturas. 
     Necesitamos que nos ayudes a recuperar el disco, para eso tienes 45 minutos, antes 
        de que el servidor se caiga y no se pueda hacer más nada.                 
    ''')
    print(imagenes.plano)
    empezar = input('¿Aceptas el reto? (PRESIONA ">" PARA CONTINUAR)')
    while empezar.upper() != '>':
        empezar = input('¿Aceptas el reto? (PRESIONA ">" PARA CONTINUAR)' )
    print(f'¡EMPECEMOS¡')


    print(imagenes.biblioteca) #plano de la biblioteca
    print('''
    Bienvenido ({jugador.avatar}), gracias por tu disposición a ayudarnos a resolver este inconveniente, 
     te encuentras actualmente ubicado en la biblioteca, revisa el menú de opciones para ver qué
                                acciones puedes realizar. 
           Recuerda que el tiempo corre más rápido que un trimestre en este reto.
    ''')
    print(imagenes.plano)
    dirigirse = input('''
    ¿A donde quieres dirigirte?:
    1. Si desea quedarse en la Biblioteca, PRESIONE 1
    2. Si desea ir al Rectorado, PRESIONE 2
    3. Si desea ir al laboratorio, PRESIONE 3
    ''').upper()

    while dirigirse.upper() != '1' and dirigirse.upper() != '2' and dirigirse.upper() != '3':
        dirigirse = input('''
    ¿A donde quieres dirigirte?:
    1. Si desea quedarse en la Biblioteca, PRESIONE 1
    2. Si desea ir al Rectorado, PRESIONE 2
    3. Si desea ir al laboratorio, PRESIONE 3
    ''').upper()
     
    if dirigirse == '1':
        biblioteca() #ir a la biblioteca
    elif dirigirse == '2':
        rectorado() #ir a plaza rectorado
    else:
        puerta() #ir a la puerta    

def nivel_dos(Jugador): #Inicio del juego medio
    vidas = 3
    print('''
      Hoy 5 de marzo de 2021, la Universidad sigue en cuarentena (esto no es novedad), 
     lo que sí es novedad es que se robaron un Disco Duro de la Universidad del cuarto
     de redes que tiene toda la información de SAP de estudiantes, pagos y  asignaturas. 
     Necesitamos que nos ayudes a recuperar el disco, para eso tienes 35 minutos, antes 
        de que el servidor se caiga y no se pueda hacer más nada.                 
    ''')
    print(imagenes.plano)
    empezar = input('¿Aceptas el reto? (PRESIONA ">" PARA CONTINUAR)')
    while empezar.upper() != '>':
        empezar = input('¿Aceptas el reto? (PRESIONA ">" PARA CONTINUAR)' )
    print(f'¡EMPECEMOS¡')
    print(imagenes.biblioteca) #plano de la biblioteca
    print('''
    Bienvenido ({avatar}), gracias por tu disposición a ayudarnos a resolver este inconveniente, 
     te encuentras actualmente ubicado en la biblioteca, revisa el menú de opciones para ver qué
                                acciones puedes realizar. 
           Recuerda que el tiempo corre más rápido que un trimestre en este reto.
    ''')
    print(imagenes.plano)
    dirigirse = input('''
    ¿A donde quieres dirigirte?:
    1. Si desea quedarse en la Biblioteca, PRESIONE 1
    2. Si desea ir al Rectorado, PRESIONE 2
    3. Si desea ir al Puerta, PRESIONE 3
    ''').upper()
    while dirigirse.upper() != '1' and dirigirse.upper() != '2' and dirigirse.upper() != '3':
        dirigirse = input('''
    ¿A donde quieres dirigirte?:
    1. Si desea quedarse en la Biblioteca, PRESIONE 1
    2. Si desea ir al Rectorado, PRESIONE 2
    3. Si desea ir al Puerta, PRESIONE 3
    ''').upper()
    if dirigirse == '1':
        biblioteca() #ir a la biblioteca
    elif dirigirse == '2':
        rectorado() #ir a plaza rectorado
    else:
        puerta() #ir a la puerta    
 

def nivel_tres(Jugador): #Inicio del juego dificil
    vidas = 1
    print('''
      Hoy 5 de marzo de 2021, la Universidad sigue en cuarentena (esto no es novedad), 
     lo que sí es novedad es que se robaron un Disco Duro de la Universidad del cuarto
     de redes que tiene toda la información de SAP de estudiantes, pagos y  asignaturas. 
     Necesitamos que nos ayudes a recuperar el disco, para eso tienes 25 minutos, antes 
        de que el servidor se caiga y no se pueda hacer más nada.                 
    ''')
    print(imagenes.plano)
    empezar = input('¿Aceptas el reto? (PRESIONA ">" PARA CONTINUAR)')
    while empezar.upper() != '>':
        empezar = input('¿Aceptas el reto? (PRESIONA ">" PARA CONTINUAR)' )
    print(f'¡EMPECEMOS¡')


    print(imagenes.biblioteca) #plano de la biblioteca
    print('''
    Bienvenido (['avatar']), gracias por tu disposición a ayudarnos a resolver este inconveniente, 
     te encuentras actualmente ubicado en la biblioteca, revisa el menú de opciones para ver qué
                                acciones puedes realizar. 
           Recuerda que el tiempo corre más rápido que un trimestre en este reto.
    ''')
    print(imagenes.plano)
    dirigirse = input('''
    ¿A donde quieres dirigirte?:
    1. Si desea quedarse en la Biblioteca, PRESIONE 1
    2. Si desea ir al Rectorado, PRESIONE 2
    3. Si desea ir al Puerta, PRESIONE 3
    ''').upper()

    while dirigirse.upper() != '1' and dirigirse.upper() != '2' and dirigirse.upper() != '3':
        dirigirse = input('''
    ¿A donde quieres dirigirte?:
    1. Si desea quedarse en la Biblioteca, PRESIONE 1
    2. Si desea ir al Rectorado, PRESIONE 2
    3. Si desea ir al Puerta, PRESIONE 3
    ''').upper()
     
    if dirigirse == '1':
        biblioteca() #ir a la biblioteca
    elif dirigirse == '2':
        rectorado() #ir a plaza rectorado
    else:
        puerta() #ir a la puerta  

def biblioteca():
    print(imagenes.biblioteca)
    print('¡Estas en la biblioteca!')
    dirigirse = input('''
    PRESIONA:
    1. Para ir al sillon (izquierda).
    2.Para ir al estante de libros (centro)
    3. Para ir al gavetero (derecha)
    4. Ir al plano
    ''').upper()
    while dirigirse.upper() != '1' and dirigirse.upper() != '2' and dirigirse.upper() != '3' and dirigirse.upper() != '4':
            dirigirse = input('''
            PRESIONA:
            1. Para ir al sillon (izquierda).
            2.Para ir al estante de libros (centro)
            3. Para ir al gavetero (derecha)
            4. Ir al plano
            ''').upper()
    if dirigirse == '1':
        pass #ir al sillon
    elif dirigirse == '2':
        ahorcado() #ir al estante
    elif dirigirse == '3':
        criptograma() #ir al gavetero
    else:
        print(imagenes.plano)
        dirigirse = input('''
        ¿A donde quieres dirigirte?:
        1. Si desea ir a la Biblioteca, PRESIONE 1
        2. Si desea ir al Rectorado, PRESIONE 2
        3. Si desea ir al laboratorio, PRESIONE 3
        ''').upper()

        while dirigirse.upper() != '1' and dirigirse.upper() != '2' and dirigirse.upper() != '3':
            dirigirse = input('''
        ¿A donde quieres dirigirte?:
        1. Si desea ir a la Biblioteca, PRESIONE 1
        2. Si desea ir al Rectorado, PRESIONE 2
        3. Si desea ir al laboratorio, PRESIONE 3
        ''').upper()
        if dirigirse == '1':
            biblioteca() #ir a la biblioteca
        elif dirigirse == '2':
            rectorado() #ir a plaza rectorado
        else:
            puerta() #ir a la puerta 

def rectorado():
    print(imagenes.saman)
    print('¡Estas en el Saman!')
    dirigirse = input('''
    PRESIONA:
    1. Para ir al banco 1 (izquierda).
    2.Para ir al saman (centro)
    3. Para ir al banco 2 (derecha)
    4. Ir al plano
    ''').upper()
    while dirigirse.upper() != '1' and dirigirse.upper() != '2' and dirigirse.upper() != '3' and dirigirse.upper() != '4':
            dirigirse = input('''
            PRESIONA:
            1. Para ir al banco 1 (izquierda).
            2.Para ir al saman (centro)
            3. Para ir al banco 2 (derecha)
            4. Ir al plano
            ''').upper()
    if dirigirse == '1':
        quizzi() #ir al banco 1
    elif dirigirse == '2':
        logica() #ir al saman
    elif dirigirse == '3':
        banco_2() #ir al banco 2
    else:
        print(imagenes.plano)
        dirigirse = input('''
        ¿A donde quieres dirigirte?:
        1. Si desea ir a la Biblioteca, PRESIONE 1
        2. Si desea ir al Rectorado, PRESIONE 2
        3. Si desea ir al laboratorio, PRESIONE 3
        ''').upper()

        while dirigirse.upper() != '1' and dirigirse.upper() != '2' and dirigirse.upper() != '3':
            dirigirse = input('''
        ¿A donde quieres dirigirte?:
        1. Si desea ir a la Biblioteca, PRESIONE 1
        2. Si desea ir al Rectorado, PRESIONE 2
        3. Si desea ir al laboratorio, PRESIONE 3
        ''').upper()
        if dirigirse == '1':
            biblioteca() #ir a la biblioteca
        elif dirigirse == '2':
            rectorado() #ir a plaza rectorado
        else:
            puerta() #ir a la puerta 

def puerta():
    print(imagenes.puerta)
    print('¡Estas en la puerta!')
    dirigirse = input('''
    PRESIONA:
    1. Para seguir (laboratorios).
    2.Para regresar a la biblioteca
    3.Ir al plano
    ''').upper()
    while dirigirse.upper() != '1' and dirigirse.upper() != '2' and dirigirse.upper() != '3' :
            dirigirse = input('''
            PRESIONA:
            1. Para seguir (laboratorios).
            2.Para regresar (biblioteca)
            3.Ir al plano
            ''').upper()
    if dirigirse == '1':
        booleana() #ir a la puerta
    elif dirigirse == '2':
        biblioteca() #ir a la biblioteca
    else:
        print(imagenes.plano)
        dirigirse = input('''
        ¿A donde quieres dirigirte?:
        1. Si desea ir a la Biblioteca, PRESIONE 1
        2. Si desea ir al Rectorado, PRESIONE 2
        3. Si desea ir al laboratorio, PRESIONE 3
        4. Si desea ir al Cuarto de servidores, PRESIONE 4
        ''').upper()

        while dirigirse.upper() != '1' and dirigirse.upper() != '2' and dirigirse.upper() != '3' and dirigirse.upper() != '4':
            dirigirse = input('''
        ¿A donde quieres dirigirte?:
        1. Si desea ir a la Biblioteca, PRESIONE 1
        2. Si desea ir al Rectorado, PRESIONE 2
        3. Si desea ir al laboratorio, PRESIONE 3
        4. Si desea ir al Cuarto de servidores, PRESIONE 4
        ''').upper()
        if dirigirse == '1':
            biblioteca() #ir a la biblioteca
        elif dirigirse == '2':
            rectorado() #ir a plaza rectorado
        elif dirigirse == '3':
            puerta() #ir a la puerta 
        else:
            cuarto_servidores() #ir al cuarto de servidores

def cuarto_servidores():
    print(imagenes.cuarto_servidores)
    print('¡Estas en el Cuarto de servidores!')
    dirigirse = input('''
    PRESIONA:
    1. Para ir al rack (izquierda).
    2.Para ir a la puerta (centro)
    3. Para ir a la papelera (derecha)
    4. Ir al plano
    ''').upper()
    while dirigirse.upper() != '1' and dirigirse.upper() != '2' and dirigirse.upper() != '3':
            dirigirse = input('''
            PRESIONA:
            1. Para ir al rack (izquierda).
            2.Para ir a la puerta (centro)
            3. Para ir a la papelera (derecha)
            4. Ir al plano
            ''').upper()
    if dirigirse == '1':
        palabra_mezclada() #ir al rack
    elif dirigirse == '2':
        pass #ir a la puerta 
    elif dirigirse == '3':
        escoge_numero() #ir a la papelera
    else:
        print(imagenes.plano)
        dirigirse = input('''
        ¿A donde quieres dirigirte?:
        1. Si desea ir a la Biblioteca, PRESIONE 1
        2. Si desea ir al Rectorado, PRESIONE 2
        3. Si desea ir al laboratorio, PRESIONE 3
        4. Si desea ir al Cuarto de servidores, PRESIONE 4
        ''').upper()

        while dirigirse.upper() != '1' and dirigirse.upper() != '2' and dirigirse.upper() != '3' and dirigirse.upper() != '4':
            dirigirse = input('''
        ¿A donde quieres dirigirte?:
        1. Si desea ir a la Biblioteca, PRESIONE 1
        2. Si desea ir al Rectorado, PRESIONE 2
        3. Si desea ir al laboratorio, PRESIONE 3
        4. Si desea ir al Cuarto de servidores, PRESIONE 4
        ''').upper()
        if dirigirse == '1':
            biblioteca() #ir a la biblioteca
        elif dirigirse == '2':
            rectorado() #ir a plaza rectorado
        elif dirigirse == '3':
            puerta() #ir a la puerta 
        else:
            cuarto_servidores() #ir al cuarto de servidores

def laboratorio():
    print(imagenes.laboratorio)
    print('¡Estas en el laboratorio!')
    dirigirse = input('''
    PRESIONA:
    1. Para ir a la computadora 1 (izquierda).
    2.Para ir a la pizarra (centro)
    3. Para ir a computadora 2 (derecha)
    4. Ir al plano
    ''').upper()
    while dirigirse.upper() != '1' and dirigirse.upper() != '2' and dirigirse.upper() != '3':
            dirigirse = input('''
            PRESIONA:
            1. Para ir a la computadora 1 (izquierda).
            2.Para ir a la pizarra (centro)
            3. Para ir a computadora 2 (derecha)
            4. Ir al plano
            ''').upper()
    if dirigirse == '1':
        python() #ir a computadora 1
    elif dirigirse == '2':
        pizarra() #ir a la pizarra
    elif dirigirse == '3':
        adivinanzas() #ir a la computadora 2
    else:
        print(imagenes.plano)
        dirigirse = input('''
        ¿A donde quieres dirigirte?:
        1. Si desea ir a la Biblioteca, PRESIONE 1
        2. Si desea ir al Rectorado, PRESIONE 2
        3. Si desea ir al laboratorio, PRESIONE 3
        4. Si desea ir al Cuarto de servidores, PRESIONE 4
        ''').upper()

        while dirigirse.upper() != '1' and dirigirse.upper() != '2' and dirigirse.upper() != '3' and dirigirse.upper() != '4':
            dirigirse = input('''
        ¿A donde quieres dirigirte?:
        1. Si desea ir a la Biblioteca, PRESIONE 1
        2. Si desea ir al Rectorado, PRESIONE 2
        3. Si desea ir al laboratorio, PRESIONE 3
        4. Si desea ir al Cuarto de servidores, PRESIONE 4
        ''').upper()
        if dirigirse == '1':
            biblioteca() #ir a la biblioteca
        elif dirigirse == '2':
            rectorado() #ir a plaza rectorado
        elif dirigirse == '3':
            puerta() #ir a la puerta 
        else:
            cuarto_servidores() #ir al cuarto de servidores

def estadisticas():
    pass

def main():
    print('BIENVENDO A ESCAPAMET')
    menu = True 
    while menu:
        print('''
        1. Registrar usuario
        2. Empezar el juego
        3. Ver instrucciones de juego
        4. Estadisticas de juego
        ''')
        opcion = int(input('Seleccione una opcion 1, 2 o 3: '))
        if opcion == 1:
           # registro() 
            jugador = Jugador()
            jugador.registro()
            print(jugador.nombre)
            menu = False
          
        elif opcion == 2:
            empezar_juego()
 
        elif opcion == 3:
            leer_instrucciones()
        elif opcion == 4:
            estadisticas()
        else:
            print('Seleccione una opccion correcta')
  
main()  
