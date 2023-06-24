import random
import string

def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

def guardar_contrasena(contrasena):
    with open('contrasenas.txt', 'a') as archivo:
        archivo.write(contrasena + '\n')

def main():
    print("¡Bienvenido al generador de contraseñas seguras!")
    longitud = int(input("Ingresa la longitud deseada para la contraseña: "))
    contrasena = generar_contrasena(longitud)
    print("Contraseña generada:", contrasena)
    guardar_contrasena(contrasena)
    print("La contraseña ha sido guardada en el archivo contrasenas.txt")

if __name__ == '__main__':
    main()
