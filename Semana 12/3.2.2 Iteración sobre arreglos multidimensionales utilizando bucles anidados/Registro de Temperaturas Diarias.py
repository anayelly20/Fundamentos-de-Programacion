# Definir una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Días de la semana (7 días)
# Tercera dimensión: Semanas (4 semanas)

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
        [  # Semana 2
            {"day": "Lunes", "Temp": 33},
            {"day": "Martes", "Temp": 34},
            {"day": "Miércoles", "Temp": 36},
            {"day": "Jueves", "Temp": 35},
            {"day": "Viernes", "Temp": 37},
            {"day": "Sábado", "Temp": 38},
            {"day": "Domingo", "Temp": 36}
        ],
        [  # Semana 3
            {"day": "Lunes", "Temp": 34},
            {"day": "Martes", "Temp": 35},
            {"day": "Miércoles", "Temp": 37},
            {"day": "Jueves", "Temp": 36},
            {"day": "Viernes", "Temp": 38},
            {"day": "Sábado", "Temp": 39},
            {"day": "Domingo", "Temp": 37}
        ],
        [  # Semana 4
            {"day": "Lunes", "Temp": 33},
            {"day": "Martes", "Temp": 34},
            {"day": "Miércoles", "Temp": 36},
            {"day": "Jueves", "Temp": 37},
            {"day": "Viernes", "Temp": 38},
            {"day": "Sábado", "Temp": 39},
            {"day": "Domingo", "Temp": 37}
        ]
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
        [  # Semana 2
            {"day": "Lunes", "Temp": 18},
            {"day": "Martes", "Temp": 17},
            {"day": "Miércoles", "Temp": 18},
            {"day": "Jueves", "Temp": 19},
            {"day": "Viernes", "Temp": 19},
            {"day": "Sábado", "Temp": 18},
            {"day": "Domingo", "Temp": 17}
        ],
        [  # Semana 3
            {"day": "Lunes", "Temp": 19},
            {"day": "Martes", "Temp": 18},
            {"day": "Miércoles", "Temp": 17},
            {"day": "Jueves", "Temp": 18},
            {"day": "Viernes", "Temp": 19},
            {"day": "Sábado", "Temp": 20},
            {"day": "Domingo", "Temp": 18}
        ],
        [  # Semana 4
            {"day": "Lunes", "Temp": 19},
            {"day": "Martes", "Temp": 18},
            {"day": "Miércoles", "Temp": 17},
            {"day": "Jueves", "Temp": 18},
            {"day": "Viernes", "Temp": 19},
            {"day": "Sábado", "Temp": 20},
            {"day": "Domingo", "Temp": 18}
        ]
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
        [  # Semana 2
            {"day": "Lunes", "Temp": 23},
            {"day": "Martes", "Temp": 24},
            {"day": "Miércoles", "Temp": 25},
            {"day": "Jueves", "Temp": 23},
            {"day": "Viernes", "Temp": 26},
            {"day": "Sábado", "Temp": 27},
            {"day": "Domingo", "Temp": 25}
        ],
        [  # Semana 3
            {"day": "Lunes", "Temp": 24},
            {"day": "Martes", "Temp": 25},
            {"day": "Miércoles", "Temp": 26},
            {"day": "Jueves", "Temp": 25},
            {"day": "Viernes", "Temp": 27},
            {"day": "Sábado", "Temp": 28},
            {"day": "Domingo", "Temp": 26}
        ],
        [  # Semana 4
            {"day": "Lunes", "Temp": 23},
            {"day": "Martes", "Temp": 24},
            {"day": "Miércoles", "Temp": 25},
            {"day": "Jueves", "Temp": 24},
            {"day": "Viernes", "Temp": 26},
            {"day": "Sábado", "Temp": 27},
            {"day": "Domingo", "Temp": 25}
        ]
    ]
]

# Calcular el promedio de temperaturas por ciudad y semana
promedios_por_ciudad = []

# Iterar a través de las ciudades, semanas y días para calcular el promedio de temperaturas
for ciudad in temperaturas:  # Iterar sobre cada ciudad en temperaturas
    promedio_semanal = []
    suma_total = 0
    cantidad_total = 0
    for semana in ciudad:  # Iterar sobre cada semana en la ciudad
        suma_semanal = 0
        cantidad_semanal = 0
        for dia in semana:  # Iterar sobre cada día en la semana
            suma_semanal += dia['Temp']
            cantidad_semanal += 1
            suma_total += dia['Temp']
            cantidad_total += 1
        promedio = suma_semanal / cantidad_semanal  # Calcular el promedio de la semana
        promedio_semanal.append(promedio)
    promedio_ciudad = suma_total / cantidad_total  # Calcular el promedio de la ciudad
    promedios_por_ciudad.append((promedio_semanal, promedio_ciudad))

# Mostrar el promedio de temperaturas para cada ciudad y semana
for i, (promedio_semanal, promedio_ciudad) in enumerate(promedios_por_ciudad):
    print(f"\nCiudad {i + 1}:")
    print(f"Promedio general de la ciudad: {promedio_ciudad:.2f}" "°C")
    for j, promedio in enumerate(promedio_semanal):
        print(f"Promedio de la Semana {j + 1}: {promedio:.2f}" "°C")

