mascota=["Perro", "Gato", "Pez", "Pajaro", "Avestruz", "Conejo"]; 
print(mascota); 
a=int(1); b=int(1); 
num=int()
string=(); 
rta=input(print("Agregar Si O No")); 
while(rta=="Si"):
    if(len(mascota)<10):
        objeto=input("Ingrese una mascota ")
        mascota.append(objeto); 
        print("Agregar mas mascotas Si o No"); 
        rta=input(); 
    else:
        print("Suficientes mascotas por hoy, no se agregaran mas")
        rta="No"; 
print("Le gustaria suprimir alguna mascota de la lista, Si o No"); 
rta=input(); 

while(rta=="No"):
    if(len(mascota)>1):
        objeto=input("Que mascota quiere quitar")
        mascota.remove(objeto); 
        print("Algun otro animal para quitar? Si o No")
        rta=input(); 
    else:
        print("No tenemos mas mascotas, no hay nada para quitar"); 
        rta=="No"; 
print("Se te perdio un animal?, quieres buscarlo?, Si o No"); 
rta=input(); 

while(rta=="s"):
    objeto=input("Otra mascota a encontrar?")
    num=mascota.index(objeto); 
    print(mascota[num+1]); 
    print(mascota[num-1]); 

    print("Algun otro a encontrar? Si o No")
    rta=input(); 

print("Hora de horientar a las mascotas, quiere ordenarlas? Si o No")
rta=input(); 

if (rta=="Si"):
    for a in range (1, len(mascota)+1):
        for b in range(1, len(mascota)):
            if(mascota[b-1]>mascota[b]):
                string=mascota[b-1]; 
                mascota[b-1]-mascota[b]; 
                mascota[b]=string; 


print(mascota); 