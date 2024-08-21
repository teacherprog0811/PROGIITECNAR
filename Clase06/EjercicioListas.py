# Declarar una lista vacía
lista1 = []

# Declarar una lista con más de 5 elementos
lista2 = ["Moto","Automovil","Avion","Barco", "Yate"]

#Encuentre la longitud de su lista
print (len(lista1))
print (len(lista2))

#Obtener el primer elemento, el elemento central y el último elemento de la lista
print("Ultimo elemento " +lista2[-1])
print("Medio elemento " +lista2[-3])
print("Primer elemento " +lista2[-5])

# Declara una lista llamada tipos_datos_mezclados, pon tu(nombre, edad, altura, estado civil, dirección)
tipos_datos_mezclados =[]
tipos_datos_mezclados.append("Ivan Narvaez")
tipos_datos_mezclados.append("34")
tipos_datos_mezclados.append("180")
tipos_datos_mezclados.append("Casado")
tipos_datos_mezclados.append("13 de junio")

print (f'Su nombre es: {tipos_datos_mezclados[0]} \n tiene {tipos_datos_mezclados[1]} años de edad \n su estatura es {tipos_datos_mezclados[2]}\n su estado civil es {tipos_datos_mezclados[3]} \n vive en {tipos_datos_mezclados[4]}')

#Declare una variable de lista llamada it_companies y asígnele los valores iniciales Facebook, Google, Microsoft, Apple, IBM, Oracle y Amazon.

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print (f'Imprimiendo lista de IT Companies:  {it_companies}')

#Añadir una empresa de TI a it_companies utilizando los metodos de insercion.
it_companies.insert(1, "ITPeople")
print (f'La nueva lista es:  {it_companies}')

#Comprobar si una determinada empresa existe en la lista it_companies.

existe = 'Linux' in it_companies
print(f'Verificando items de una lista {existe}')  

existe2 =it_companies.index("Google")
print(f'Verificando items de una lista 2 {existe2}') 
#Ordena la lista con el método sort()

it_companies.sort()
print (f'Ordenando lista de IT Companies:  {it_companies}')

#Invierte la lista en orden descendente utilizando el método reverse()

it_companies.reverse()
print (f'Invertiendo lista de IT Companies:  {it_companies}')

#Elimine la primera empresa informática de la lista.

it_companies.pop(0)
print (f'Eliminando primera empresa de IT Companies:  {it_companies}')

#Eliminar todas las empresas de TI de la lista

it_companies.clear()
print (f'Eliminando todas las empresas de IT Companies:  {it_companies}')


