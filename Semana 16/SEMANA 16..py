# Escritura de Archivo de Texto
# Se crea el archivo 'my_notes.txt' y se escriben tres líneas de notas personales.

with open('my_notes.txt', 'w') as file:
    # Escribimos tres líneas en el archivo.
    file.write("Primera nota: Planificar mi día de manera eficiente.\n")
    file.write("Segunda nota: Mantener una alimentación saludable.\n")
    file.write("Tercera nota: Hacer ejercicio regularmente.\n")

# Lectura de Archivo de Texto
# Se abre el archivo 'my_notes.txt' para leer su contenido línea por línea.

with open('my_notes.txt', 'r') as file:
    # Leer cada línea del archivo y mostrarla en la consola.
    line = file.readline()
    while line:  # Continuar leyendo hasta que no haya más líneas.
        print(line.strip())  # Eliminar los saltos de línea adicionales al mostrar cada línea.
        line = file.readline()  # Leer la siguiente línea.

# Nota: El archivo se cierra automáticamente después de las operaciones de lectura y escritura
# al utilizar el bloque 'with'.