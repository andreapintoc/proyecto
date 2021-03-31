# from imagenes import *
from jugador import Jugador
# from juegos import *
usuarios = []

def registro(): #Se piden los siguientes datos al usuario para registrarlo
    nombre = input('Introduzca nombre del jugador: ') #Su nombre
    while not nombre.isalpha():
        nombre = input('Nombre incorrecto, introduzca su nombre:')
    edad = input('Introduzca su edad:')
    while not edad.isnumeric() and not edad <= 0 :
        edad = input('Edad incorrecta, introduzca edad del jugador: ') #Su edad
    usuario = input('Indroduzca un nombre de usuario:')
    while not usuario.isalpha():
        usuario = input('Introduzca un nombre de usuario correcto: ') #Su usuario, debe ser distinto a los que ya existen
    for i in usuarios:
        if usuario in usuarios:
            print('Usuario existente')
            usuario = input('Indroduzca un nombre de usuario: ')
        else:
            usuarios.append(usuario)
    clave = input('Ingrese su contraseña: ') #Su clave, debe contener al menos 8 caracteres, no debe tener espacios en blanco y deben ser solo numeros
    while len(clave) < 8:
        clave = input('La contrasena debe tener al menos 8 caracteres, Introduzca una contraseña valida: ')
    while clave.count(" ")> 0:
        clave = input('La contrasena no puede contener espacios en blanco, Introduzca contraseña valida: ')
    while not clave.isnumeric():
        clave = input('La contrasena no puede contener letras, Introduzca una contraseña valida: ')
    #Su avatar
    avatar = input('''
    Seleccione el avatar de su preferencia:      
    1.Scharifker
    2.Eugenio Mendoza
    3.Pelusa
    4.Gandhi 
    5.Pepe
    ''')
    while not avatar.isnumeric():
        avatar = input('''
        Ingrese el numero del avatar de su preferencia:
        1.Scharifker
        2.Eugenio Mendoza
        3.Pelusa
        4.Gandhi 
        5.Pepe
        ''')
    while avatar != '1' and avatar != '2' and avatar != '3' and avatar != '4' and avatar != '5':
           avatar = input('''
           Avatar invalido. Introduzca el avatar de su preferencia:
           1.Scharifker
           2.Eugenio Mendoza
           3.Pelusa
           4.Gandhi 
           5.Pepe
           ''')
        
    print('JUGADOR REGISTRADO')
    #print('usuario', usuario, 'avatar',avatar) #Se agregan los datos a la lista
    usuarios.append(Jugador)  
    print(usuarios)

def nivel_uno(registro): #Inicio del juego mas facil
    #for h in range(1):
    #  for m in range(40):
    #        for s in range (60):
    #              os.system('clear')
    #              print(f'{h}:{m}:{s}')
    #              time.sleep(1)
    print('''
      Hoy 5 de marzo de 2021, la Universidad sigue en cuarentena (esto no es novedad), 
     lo que sí es novedad es que se robaron un Disco Duro de la Universidad del cuarto
     de redes que tiene toda la información de SAP de estudiantes, pagos y  asignaturas. 
     Necesitamos que nos ayudes a recuperar el disco, para eso tienes 45 minutos, antes 
        de que el servidor se caiga y no se pueda hacer más nada.                 
    ''')
    #print(imagenes.plano) #plano del campus
    empezar = input('¿Aceptas el reto? (PRESIONA ">" PARA CONTINUAR)')
    while empezar.upper() != '>':
        empezar = input('¿Aceptas el reto? (PRESIONA ">" PARA CONTINUAR)' )
    print(f'¡EMPECEMOS¡')
    #print(imagenes.biblioteca) #plano de la biblioteca
    print('''
    Bienvenido {avatar}, gracias por tu disposición a ayudarnos a resolver este inconveniente, 
     te encuentras actualmente ubicado en la biblioteca, revisa el menú de opciones para ver qué
                                acciones puedes realizar. 
           Recuerda que el tiempo corre más rápido que un trimestre en este reto.
    ''')

    dirigirse = input('''
    ¿A donde quieres dirigirte?:
    1. Si desea quedarse en la Biblioteca, PRESIONE 1
    2. Si desea ir al Rectorado, PRESIONE 2
    3. Si desea ir al Puerta, PRESIONE 3
    ''').upper()
    #dirigirse = input('''
    #¿A donde quieres dirigirte?:
    #(B) para la biblioteca
    #(S) para el saman
    #(L) para los Laboratorios SL001 
    #''').upper()
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

def nivel_dos(registro): #Inicio del juego medio
        #for h in range(1):
    #  for m in range(40):
    #        for s in range (60):
    #              os.system('clear')
    #              print(f'{h}:{m}:{s}')
    #              time.sleep(1)
    print('''
      Hoy 5 de marzo de 2021, la Universidad sigue en cuarentena (esto no es novedad), 
     lo que sí es novedad es que se robaron un Disco Duro de la Universidad del cuarto
     de redes que tiene toda la información de SAP de estudiantes, pagos y  asignaturas. 
     Necesitamos que nos ayudes a recuperar el disco, para eso tienes 35 minutos, antes 
        de que el servidor se caiga y no se pueda hacer más nada.                 
    ''')
    #print(imagenes.plano) #plano del campus
    empezar = input('¿Aceptas el reto? (PRESIONA ">" PARA CONTINUAR)')
    while empezar.upper() != '>':
        empezar = input('¿Aceptas el reto? (PRESIONA ">" PARA CONTINUAR)' )
    print(f'¡EMPECEMOS¡')
    #print(imagenes.biblioteca) #plano de la biblioteca
    print('''
    Bienvenido {avatar}, gracias por tu disposición a ayudarnos a resolver este inconveniente, 
     te encuentras actualmente ubicado en la biblioteca, revisa el menú de opciones para ver qué
                                acciones puedes realizar. 
           Recuerda que el tiempo corre más rápido que un trimestre en este reto.
    ''')

    dirigirse = input('''
    ¿A donde quieres dirigirte?:
    1. Si desea quedarse en la Biblioteca, PRESIONE 1
    2. Si desea ir al Rectorado, PRESIONE 2
    3. Si desea ir al Puerta, PRESIONE 3
    ''').upper()
    #dirigirse = input('''
    #¿A donde quieres dirigirte?:
    #(B) para la biblioteca
    #(S) para el saman
    #(L) para los Laboratorios SL001 
    #''').upper()
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
        rectorado() #ir al Rectorado
    else:
        puerta() #ir a la puerta

def nivel_tres(registro): #Inicio del juego dificil
        #for h in range(1):
    #  for m in range(40):
    #        for s in range (60):
    #              os.system('clear')
    #              print(f'{h}:{m}:{s}')
    #              time.sleep(1)
    print('''
      Hoy 5 de marzo de 2021, la Universidad sigue en cuarentena (esto no es novedad), 
     lo que sí es novedad es que se robaron un Disco Duro de la Universidad del cuarto
     de redes que tiene toda la información de SAP de estudiantes, pagos y  asignaturas. 
     Necesitamos que nos ayudes a recuperar el disco, para eso tienes 25 minutos, antes 
        de que el servidor se caiga y no se pueda hacer más nada.                 
    ''')
    #print(imagenes.plano) #plano del campus
    empezar = input('¿Aceptas el reto? (PRESIONA ">" PARA CONTINUAR)')
    while empezar.upper() != '>':
        empezar = input('¿Aceptas el reto? (PRESIONA ">" PARA CONTINUAR)' )
    print(f'¡EMPECEMOS¡')
    #print(imagenes.biblioteca) #plano de la biblioteca
    print('''
    Bienvenido {avatar}, gracias por tu disposición a ayudarnos a resolver este inconveniente, 
     te encuentras actualmente ubicado en la biblioteca, revisa el menú de opciones para ver qué
                                acciones puedes realizar. 
           Recuerda que el tiempo corre más rápido que un trimestre en este reto.
    ''')

    dirigirse = input('''
    ¿A donde quieres dirigirte?:
    1. Si desea quedarse en la Biblioteca, PRESIONE 1
    2. Si desea ir al Rectorado, PRESIONE 2
    3. Si desea ir al Puerta, PRESIONE 3
    ''').upper()
    #dirigirse = input('''
    #¿A donde quieres dirigirte?:
    #(B) para la biblioteca
    #(S) para el saman
    #(L) para los Laboratorios SL001 
    #''').upper()
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
        rectorado() #ir al Rectorado
    else:
        puerta() #ir a la puerta



def biblioteca():
    #print(imagenes.biblioteca)
    print('¡Estas en la biblioteca!')
    dirigirse = input('''
    PRESIONA:
    1. Para ir al sillon (izquierda).
    2.Para ir al estante de libros (centro)
    3. Para ir al gavetero (derecha)
    ''').upper()
    while dirigirse.upper() != '1' and dirigirse.upper() != '2' and dirigirse.upper() != '3':
            dirigirse = input('''
            PRESIONA:
            1. Para ir al sillon (izquierda).
            2.Para ir al estante de libros (centro)
            3. Para ir al gavetero (derecha)
            ''').upper()
    if dirigirse == '1':
        sillon() #ir al sillon
    elif dirigirse == '2':
        estante() #ir al estante
    else:
        gavetero() #ir al gavetero


def rectorado():
    print('¡Estas en el Saman!')
    dirigirse = input('''
    PRESIONA:
    1. Para ir al banco 1 (izquierda).
    2.Para ir al saman (centro)
    3. Para ir al banco 2 (derecha)
    ''').upper()
    while dirigirse.upper() != '1' and dirigirse.upper() != '2' and dirigirse.upper() != '3':
            dirigirse = input('''
            PRESIONA:
            1. Para ir al banco 1 (izquierda).
            2.Para ir al saman (centro)
            3. Para ir al banco 2 (derecha)
            ''').upper()
    if dirigirse == '1':
        banco_1() #ir al banco 1
    elif dirigirse == '2':
        saman_1() #ir al saman
    else:
        banco_2() #ir al banco 2

def puerta():
    print('¡Estas en la puerta!')
    dirigirse = input('''
    PRESIONA:
    1. Para seguir (laboratorios).
    2.Para regresar a la biblioteca
    ''').upper()
    while dirigirse.upper() != '1' and dirigirse.upper():
            dirigirse = input('''
            PRESIONA:
            1. Para seguir (laboratorios).
            2.Para regresar (biblioteca)
            ''').upper()
    if dirigirse == '1':
        pass #juego
    else:
        biblioteca() #ir a la biblioteca

def laboratorio():
    pass
      
def estadisticas():
    pass

def main():
    print('BIENVENDO A ESCAPAMET')
    z = True 
    while z == True:
      print('''
      1. Registrar usuario
      2. Empezar el juego
      3. Ver instrucciones de juego
      4. Estadisticas de juego
      ''')
      x = int(input('Seleccione una opcion 1, 2 o 3: '))
      if x == 1:
          registro()
          z == False
        
      elif x == 2:
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
                  nivel_uno(registro)
              elif nivel == '2':
                  nivel_dos()
              else:
                  nivel_tres()
      elif x == 3:
          pass
      elif x == 4:
          estadisticas()
      else:
          print('Seleccione una opccion correcta')

main()