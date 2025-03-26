öntözővíz_adag = float(input('add meg az öntözővíz adagot mm-ben: '))
ET = float(input("add meg az ET értéket mm/nap-ban: "))


öntözési_forduló = öntözővíz_adag / ET


print(f"Az öntözési forduló: {öntözési_forduló:.2f} nap.")

#Másik verzió

def szamit_ontozesi_ido(viz_adag, intenzitas):
    
    ontotzesi_ido = viz_adag / intenzitas
    return ontotzesi_ido
viz_adag = float(input("Add meg az öntözővíz adagot (mm): "))

intenzitas = float(input("Add meg az intenzitást (mm/óra): "))

ontozesi_ido = szamit_ontozesi_ido(viz_adag, intenzitas)

print(f"Az öntözési idő: {ontozesi_ido:.2f} óra.")