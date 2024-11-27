Vacas = int(input("Ingrese el numero de vacas que cria: "))
corral= 40*30
print("El tamaño del corral es de ",corral, "metros cuadrados")
dia=1
l_leche= corral/30
while (dia<=7):
    print("La vaca produjo ",(Vacas*(l_leche*dia)), "el dia", dia)
    dia= dia+1