
print('''
¡Estas en en Saman!
Para obtener el disco duro,
debes encontrar la logica
PRESIONA > PARA CONTINUAR
''')
si = input()
while si != '>':
   print('''
   ¡Estas en en Saman!
   Para obtener el disco duro,
   debes encontrar la logica
   PRESIONA > PARA CONTINUAR
   ''')
   si = input()
#⏰ vale 3 🍌 vale 4 🧡 vale 15
print('🧡+🧡+🧡=45 \n 🍌+🍌+🧡=23 \n 🍌+⏰+⏰=10 \n ⏰+🍌+🍌x🧡=?')
respuesta1 = input('cual sera el valor? ')
if respuesta1 == '67' or respuesta1 == 'sesenta y siete':
    print('Respuesta correcta, haz ganado el DISCO DURO')
else:
    print('Respuesta incorrecta, pierdes una vida')
#🐝 vale 5 🐧vale 9 🐦vale 4
print('🐧+🐧+🐧=27 \n 🐧+🐝+🐝=19 \n 🐝+🐦+🐦=13 \n 🐝x🐧-🐦=?')
respuesta2 = input('cual sera el valor? ')
if respuesta2 == '25' or respuesta2 == 'veinticinco':
    print('Respuesta correcta, haz ganado el DISCO DURO')
else:
    print('Respuesta incorrecta, pierdes una vida')