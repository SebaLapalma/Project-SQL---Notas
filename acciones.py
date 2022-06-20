"""
Este archivo deberá encontrarse dentro de una carpeta llamada notas, para su utilización posterior
"""

import notas.nota as modelo

class Acciones:
    def crear (self, usuario):
        print(f"Ok, {usuario[1]}, vamos a crear una nueva nota.")
        
        titulo = input("Introduce el título de tu nota\n")
        descripcion = input ("Contenido de tu nota:\n  ")

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar [0] >= 1:
            print(f"\nPerfecto, has guardado la nota: {nota.titulo}")
        else:
            print(f"\nNo se pudo guardar la nota, {usuario[1]}. Inténtalo más tarde.")

    def mostrar (self, usuario):
        print (f"\nOk, {usuario[1]}. Aquí están tus notas: \n")

        nota = modelo.Nota(usuario[0])
        notas = nota.listar()

        for i in notas:
            print(" ")
            print(i[2])
            print(i[3])
            print(i[4])
            print("-----------------------------------------")
    
    def borrar(self, usuario):
        print(f"\nOk,{usuario[1]} vamos a borrar una nota")

        titulo = input("Introduce el título de la nota a borrar: ")
        nota = modelo.Nota(usuario[0], titulo)
        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print(f"Hemos borrado la nota: {nota.titulo}")
        else:
            print("No se ha borrado la nota. Inténtalo después.")
