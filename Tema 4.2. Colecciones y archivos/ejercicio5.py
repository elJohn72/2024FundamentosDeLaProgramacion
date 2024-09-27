# Crear el diccionario y realizar todas las operaciones en una sola ejecución
informacion_personal = {
    "nombre": "Juan Pérez",
    "edad": 28,
    "ciudad": "Quito",
    "profesion": "Ingeniero"
}

informacion_personal["ciudad"] = "Guayaquil"  # Modificar la ciudad
informacion_personal["profesion"] = "Desarrollador de Software"  # Modificar la profesión

# Verificar si "telefono" existe y agregarlo si no está
informacion_personal["telefono"] = informacion_personal.get("telefono", "0987654321")

# Eliminar la clave "edad"
informacion_personal.pop("edad", None)

# Imprimir el diccionario final
print(informacion_personal)
