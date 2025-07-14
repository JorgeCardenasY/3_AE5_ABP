matriz = [ [10, 15, 20], [3, 7, 14] ]
cantantes = [ {"nombre": "Ricky Martin", "pais": "Puerto Rico"}, {"nombre": "Chayanne", "pais": "Puerto Rico"} ]
ciudades = { "México": ["Ciudad de México", "Guadalajara", "Cancún"], "Chile": ["Santiago", "Concepción", "Viña del Mar"] }
coordenadas = [ {"latitud": 8.2588997, "longitud": -84.9399704} ]

# Cambia el valor 3 en matriz por 6.
matriz[1][0] = 6

# Cambia el nombre del primer cantante por "Enrique Martin Morales".
cantantes[0]["nombre"] = "Enrique Martin Morales"

# En el diccionario ciudades, reemplaza "Cancún" por "Monterrey".
ciudades["México"][2] = "Monterrey"

# En la lista coordenadas, cambia el valor de "latitud" por 9.9355431.
coordenadas[0]["latitud"] = 9.9355431

# VISUALIZACIÓN DE CAMBIOS SOLICITADOS:
print(matriz)
print(cantantes)
print(ciudades)


# 2- Obtener valores específicos desde una lista de diccionarios:
for cantante in cantantes:
    print(F"{cantante["nombre"]} - {cantante["pais"]} \n")

# 3.- 
for cantante in cantantes:
    print(cantante["nombre"])

for cantante in cantantes:
    print(cantante["pais"])


# Dado:
costa_rica = { "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"], "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"] }

# 4. Recorrer un diccionario con listas como valores:
for clave, valor in costa_rica.items():
    print(f"\nla cantidad de elementos en {clave} es:\n{len(valor)}")