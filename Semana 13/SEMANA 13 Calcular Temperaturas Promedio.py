# Datos de temperaturas de 3 ciudades durante 4 semanas
temperaturas = [
    [  # Ciudad 1 - Ambato
        [  # Semana 1
            {"day": "Lunes", "Temp": 34},
            {"day": "Martes", "Temp": 35},
            {"day": "Miércoles", "Temp": 36},
            {"day": "Jueves", "Temp": 37},
            {"day": "Viernes", "Temp": 38},
            {"day": "Sábado", "Temp": 39},
            {"day": "Domingo", "Temp": 37}
        ],
        # Semana 2, 3 y 4 se omiten para abreviar el código
    ],
    [  # Ciudad 2 - Cuenca
        [  # Semana 1
            {"day": "Lunes", "Temp": 19},
            {"day": "Martes", "Temp": 18},
            {"day": "Miércoles", "Temp": 17},
            {"day": "Jueves", "Temp": 18},
            {"day": "Viernes", "Temp": 19},
            {"day": "Sábado", "Temp": 20},
            {"day": "Domingo", "Temp": 18}
        ],
        # Semanas adicionales se omiten
    ],
    [  # Ciudad 3 - Loja
        [  # Semana 1
            {"day": "Lunes", "Temp": 22},
            {"day": "Martes", "Temp": 23},
            {"day": "Miércoles", "Temp": 24},
            {"day": "Jueves", "Temp": 23},
            {"day": "Viernes", "Temp": 25},
            {"day": "Sábado", "Temp": 26},
            {"day": "Domingo", "Temp": 24}
        ],
        # Semanas adicionales se omiten
    ]
]

def calcular_promedio_temperaturas(temperaturas):
    # Lista para almacenar los promedios por ciudad
    promedios_por_ciudad = []

    # Iterar sobre cada ciudad
    for ciudad in temperaturas:
        promedio_semanal = []
        suma_total = 0
        cantidad_total = 0

        # Iterar sobre cada semana
        for semana in ciudad:
            suma_semanal = 0
            cantidad_semanal = 0

            # Iterar sobre cada día de la semana
            for dia in semana:
                suma_semanal += dia['Temp']
                cantidad_semanal += 1
                suma_total += dia['Temp']
                cantidad_total += 1

            # Calcular el promedio semanal
            promedio_semanal.append(suma_semanal / cantidad_semanal)

        # Calcular el promedio general de la ciudad
        promedio_ciudad = suma_total / cantidad_total
        promedios_por_ciudad.append((promedio_semanal, promedio_ciudad))

    return promedios_por_ciudad

# Calcular los promedios
promedios = calcular_promedio_temperaturas(temperaturas)

# Mostrar resultados
for i, (promedio_semanal, promedio_ciudad) in enumerate(promedios):
    print(f"\nCiudad {i + 1}:")
    print(f"Promedio general de la ciudad: {promedio_ciudad:.2f}°C")
    for j, promedio in enumerate(promedio_semanal):
        print(f"Promedio de la Semana {j + 1}: {promedio:.2f}°C")
