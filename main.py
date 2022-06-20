"""
Proyecto Python y MySQL:
-Abrir Asistente
-Login o registro
-Si elegimos registro creará un usuario en la base de datos 
-Si elegimos login, identificará al usuario y nos preguntará:
-Crear notas, mostrar notas, borrar notas.
"""

print(""" 
Acciones disponibles
    -Registro
    -Login
    -Salir
""")

from usuarios import acciones

haz_el = acciones.Acciones()

accion = input("¿Qué quieres hacer?\n")

if accion == "registro":
    haz_el.registro()

elif accion == "login":
    haz_el.login()
elif accion == "salir":
    print("¡Nos vemos luego!")
    exit()