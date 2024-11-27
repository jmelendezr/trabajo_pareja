Vacas = int(input("Ingrese el numero de vacas que cria: "))
corral= 40*30
print("El tamaño del corral es de ",corral, "metros cuadrados")
dia=1
l_leche= corral/30
while (dia<=7):
    print("La vaca produjo ",(Vacas*(l_leche*dia)), "el dia", dia)
    dia= dia+1

a = int (input("Ingrese la cantidad de aves de la granja: "))

gallinas = a / 3

gallinas_3_dias = gallinas / 2
gallinas_5_dias = gallinas / 2




huevo = (gallinas_3_dias * (10))
huevo_2 = (gallinas_5_dias * (6))

print ("Al mes se ponen", huevo + huevo_2,"huevos")
