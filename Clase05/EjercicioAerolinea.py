Vuelo ={
    'Aerolinea': 'Avianca',
    'Vuelo': 'AV3102',
    'Origen': 'CTG',
    'Destino': 'MDE',
    'Tipo_Maleta': ['Cabina', 'Mano', 'Bodega']
}
print ("Imprimiendo valores del diccionario: \n")
for key, value in Vuelo.items():
    print (value)
print ("Imprimiendo valores de los tipos de maleta: \n")
for maleta in Vuelo['Tipo_Maleta']:
    print(maleta)