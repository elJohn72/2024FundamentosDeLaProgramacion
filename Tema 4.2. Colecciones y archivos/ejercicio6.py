# Escritura de Archivo de Texto

# Abrimos un archivo llamado 'my_notes.txt' en modo escritura ('w')
# Si el archivo no existe, Python lo creará.
with open('my_notes.txt', 'w') as file:
    # Escribimos tres líneas de notas personales en el archivo
    file.write("Esta es mi primera nota personal.\n")
    file.write("Estoy aprendiendo a manipular archivos en Python.\n")
    file.write("Escribir y leer archivos es una habilidad esencial.\n")

# Lectura de Archivo de Texto

# Abrimos el archivo 'my_notes.txt' en modo lectura ('r')
with open('my_notes.txt', 'r') as file:
    # Utilizamos readline() para leer el archivo línea por línea
    while True:
        line = file.readline()
        # Si readline() devuelve una cadena vacía, es el final del archivo
        if not line:
            break
        # Mostramos cada línea leída en la consola
        print(line.strip())  # strip() elimina saltos de línea adicionales

# El archivo se cierra automáticamente al usar 'with', pero
# en caso de usar open() sin with, se debería usar file.close() para cerrarlo manualmente.
