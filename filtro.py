import json
def main():
    print("-------------- Menu --------------")
    print("\n1-Crear\n2-Modificar\n3-Eliminar\n4-Listar\n5-Generar informe de datos.txt\n0.SALIR\n")

def load_data():
    with open('pepe.json', 'r') as file:
        data = json.load(file)
    return data

data=load_data()

def save_data(data):
    with open('pepe.json', 'w') as file:
        json.dump(data, file, indent=4)

def vali_numericas(x):
    bandera=True
    while bandera:
        try:
            int_x = int(x)
            if int_x >= 0:
                bandera=False
        except ValueError:
            print("Dato inválido")
        if bandera:
            x=input("Ingresalo de nuevo: ").strip() 
    return int_x
    
def vali_alfabeticas(y):
    bandera=True
    while bandera:
        try:
            if y.replace(" ",""):
                bandera=False
        except ValueError:
            print("Dato inválido")
        if bandera:
            y=input("Ingresalo de nuevo: ").strip() 
    return y

def vali_manual_existente(manual):
    for m in data['manuales'].keys():
        if m==manual:
            print("USUARIO YA EXISTENTE")
        else: return manual



def create():
    data=load_data()
    manual = vali_alfabeticas(input("Ingresa el nombre del manual a crear: "))
    if vali_manual_existente(manual):
            autor= vali_alfabeticas(input("Nombre del autor: "))
            paginas= vali_numericas(input("Ingrese el numero de paginas: "))
            h=vali_numericas(input("Ingresa el numero de temas a ingresar: "))
            for i in range(h):
                print(f"Ingrese el titulo #{i}")
                titulo= vali_alfabeticas(input("Ingrese el titulo: "))
                clasificacion=vali_numericas(input("Ingrese la clasificacion: "))
                if clasificacion <1 or clasificacion>3:
                    print("CLASIFICACION INVALIDA")
                    clasificacion=vali_numericas(input("Ingrese la clasificacion: "))
                    
                else: 
                    op={
                        "Titulo": titulo,
                        "Clasificación": clasificacion
                        }
                    
                    temitas=[]
                    temitas.append(op)
                    data['manuales']= nuevo_lenguaje = {"author": autor, "paginas": paginas, "temas": temitas }
                    print("USUARIO CREADO CORRECTAMENTE")
                save_data(data)
    else:
        print("MANUAL YA EXISTENTE") 


def modificar1():
    data=load_data()
    manual = vali_alfabeticas(input("Ingresa el nombre del manual a modificar: "))
    if vali_manual_existente(manual):
        listar_1_usuario()

        print("Que desea editar del manual? \n1.Autor\n2.Paginas\n3.Temas\n")
        cambio=(vali_numericas(input("Ingresa la opcion: ")))
        for i in data['manuales']:
            if cambio == 1:
                autor = input("Ingrese el nuevo autor del libro:\n")
                data["manuales"][manual]["author"] = autor
                print("CAMBIO EXITOSO")
                save_data(data)
                return
            elif cambio == 2:
                paginas = input("Ingrese el nuevo numero de paginas:\n")
                data["manuales"][manual]["author"] = paginas
                print("CAMBIO EXITOSO")
                save_data(data)
                return
            elif cambio == 3:
                h=vali_numericas(input("Ingresa el numero de temas a ingresar: "))
                for i in range(1,h):
                    print(f"Ingrese el titulo #{i}")
                    titulo= vali_alfabeticas(input("Ingrese el titulo: "))
                    clasificacion=vali_numericas(input("Ingrese la clasificacion: "))
                    if clasificacion <1 or clasificacion>3:
                        print("CLASIFICACION INVALIDA")
                        clasificacion=vali_numericas(input("Ingrese la clasificacion: "))
                        
                    else: 
                        op={
                            "Titulo": titulo,
                            "Clasificación": clasificacion
                            }
                        
                        temitas=[]
                        temitas.append(op)
                        data['manuales'][manual]= nuevo_lenguaje = {"author": autor, "paginas": paginas, "temas": temitas }
                        print("CAMBIO EXITOSO")
                        save_data(data)
                        return
    else:
            print("MANUAL NO ENCONTRADO")
def txt():
    with open('filtro_pepe.json', 'w') as file:
        json.dump(data, file, indent=4)



def listar():
    data=load_data()
    for i, detalles in data['manuales'].items():
            manual=i
            autor = detalles['author']
            paginas = detalles['paginas']
            for temas in detalles['temas']:
                titulo=temas['Titulo']
                clasificacion=temas['Clasificación']
            print("-"*60)
            print(f"El lenguaje es: {manual} ")
            print("SUS DATOS SON: ")
            print(f"\n AUTOR: {autor}\n PAGINAS:{paginas}\n TEMAS: \n \ttitulo: {titulo}\n \tclasificacion: {clasificacion}")

def listar_1_usuario():
    data=load_data()
    i=vali_alfabeticas(input("Ingrese el nombre del manual: "))
    for i, detalles in data['manuales'].items():
            manual=i
            autor = detalles['author']
            paginas = detalles['paginas']
            for temas in detalles['temas']:
                titulo=temas['Titulo']
                clasificacion=temas['Clasificación']
            print("-"*60)
            print(f"El lenguaje es: {manual} ")
            print("SUS DATOS SON: ")
            print(f"\n AUTOR:{autor}\n PAGINAS:{paginas}\n TEMAS: \n \ttitulo: {titulo}\n \tclasificacion: {clasificacion}")

def eliminar():
    data=load_data()
    manual = vali_alfabeticas(input("Ingresa el nombre del manual a crear: "))
    for manuall in data["manuales"]:
        if manuall == manual:
            data.pop(manual)
            print("ELIMINADO CORRECTAMENTE")
            save_data(data)
        else:
            print("MANUAL NO ENCONTRADO")
            return
def txt():
    with open('filtro_pepe.json', 'w') as file:
        json.dump(data, file, indent=4)

def txt_contenido():
    t_basicos=t_intermedios=t_avanzados=0
    for i in data['manuales']['temas']:
        if i['clasificacion']== 1:
            t_basicos+=1
        elif i['clasificacion']== 2:
            t_intermedios+=1
        elif i['clasificacion']== 3:
            t_avanzados+=1

    txt(txt_contenido)

flag  = True

while  flag:
    main()
    opcion = vali_numericas(input("Ingrese una opcion: "))
    if opcion == 1:
        create() 
    elif opcion == 2:
        modificar1()
    elif opcion == 3:
        eliminar()
    elif opcion == 4:
        listar()
    elif opcion == 5:
        txt()
    elif opcion == 0:
        flag = False
    else:
        print("Opcion no valida")
    
print("Fin del proceso")

main()