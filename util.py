import json

def leer_data():
    with open('data.json', 'r') as data:
        return json.load(data) 
     
def escribir_data(datos):
    with open('data.json', 'w') as data:
        json.dump(datos, data, indent=4)
    
def leer_instrucciones():
    archivo = open('instrucciones.txt', 'r')
    abrir = archivo.read()
    archivo.close()
    print(abrir)

    #archivo = open("instrucciones.txt", 'r')
    #archivo.read()
    #print ('instrcciones.txt')
    #archivo.close() 

#def leer_data():
#    with open('requerimiento.json', 'r') as r:
#        return json.load(requerimieto) 
     
#def escribir_data(requerimiento):
#    with open('requerimiento.json', 'w') as r:
#        json.dump(requerimiento)
        # json.dump(r, indent=4)