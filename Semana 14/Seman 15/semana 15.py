# Crear el diccionario informacion_personal
informacion_personal = {
    "nombre": "Ana Lopez",
    "edad": 20,
    "Provincia": "Pastaza",
    "profesion": "Estudiante"
}

# Acceder al valor de la clave "ciudad" y modificarlo
informacion_personal["canton"] = "Arajuno"

# Agregar una nueva clave-valor para la estatura
informacion_personal["estatura"] = "1,50"

# Agregar una nueva clave-valor para la profesión (si no existe ya)
informacion_personal["profesion"] = "Estudiante"

# Verificar si la clave "telefono" existe, si no, agregar
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0980928221"  # número ficticio

# Eliminar la clave "edad"
informacion_personal.pop("edad", None)

# Imprimir el diccionario final
print("Diccionario final:", informacion_personal)
