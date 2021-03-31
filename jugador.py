
class Jugador:

    def __init__(self, nombre, edad, usuario, clave, avatar):
        self.nombre = nombre
        self.edad = edad
        self.usuario = usuario
        self.clave = clave
        self.avatar= avatar
    def mostrar_jugador(self):
        return {f'Nombre: {self.nombre}\lnEdad: {self.edad}\lnUsuario: {self.usuario}\lnClave: {self.clave}\lnAvatar: {self.avatar}'}

