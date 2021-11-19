clientes={}
print("1 : registrar ")
print("2 : mostrar ")
print("3 : buscar ")
op=int(input("ingrese alternativa "))
if op==1:
    emp=input("ingrese empresa ")
    ruc=input("ingrese ruc ")
    clientes={ruc:emp}
    print("1 : registrar ")
    print("2 : mostrar ")
    print("3 : buscar ")
    op = int(input("ingrese alterntiva "))
if op==2:
    print(clientes)

if op==3:
    dato=input("ingrese ruc a buscar ")
    x=clientes.get(dato)
    print("empresa encontrada dato: "  )