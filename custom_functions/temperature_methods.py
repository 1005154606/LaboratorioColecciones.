#Nariño
#Tuve que crear tres funciones que hicieran lo mismo pues con una sola me salia un error que no supe solucionar

def base1():
    try:
        for x in range(0, 12):
            try:
                n = int(input("Introduce las temperaturas del mes {}: ".format(x+1)))
                lista.append(n)
            except ValueError:
                raise NameError("Tienes que volver a introducir todas las temperaturas")

        for i in lista:
            for z in meses:
                if z == "Enero":
                    diccionario["Enero"] = lista[0]

                if z == "Febrero":
                    diccionario["Febrero"] = lista[1]
                if z == "Marzo":
                    diccionario["Marzo"] = lista[2]
                if z == "Abril":
                    diccionario["Abril"] = lista[3]
                if z == "Mayo":
                    diccionario["Mayo"] = lista[4]
                if z == "Junio":
                    diccionario["Junio"] = lista[5]
                if z == "Julio":
                    diccionario["Julio"] = lista[6]
                if z == "Agosto":
                    diccionario["Agosto"] = lista[7]
                if z == "Septiembre":
                    diccionario["Septiembre"] = lista[8]
                if z == "Octubre":
                    diccionario["Octubre"] = lista[9]
                if z == "Noviembre":
                    diccionario["Noviembre"] = lista[10]
                if z == "Diciembre":
                    diccionario["Diciembre"] = lista[11]

    except ValueError:

        raise NameError("Tienes que volver a introducir todas las temperaturas")

    return diccionario

lista=[]
meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
diccionario={}


def prom1(x):
    cont1 = 0
    a = x.values()
    for x in a:
        cont1 = cont1 + x
        c = cont1 / len(a)

    return c

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#Santander
def base2():
    try:
        for x in range(0, 12):
            n = int(input("Introduce las temperaturas del mes {}: ".format(x+1)))
            lista1.append(n)
        for i in lista1:
            for z in meses1:
                if z == "Enero":
                    diccionario1["Enero"] = lista1[0]

                if z == "Febrero":
                    diccionario1["Febrero"] = lista1[1]
                if z == "Marzo":
                    diccionario1["Marzo"] = lista1[2]
                if z == "Abril":
                    diccionario1["Abril"] = lista1[3]
                if z == "Mayo":
                    diccionario1["Mayo"] = lista1[4]
                if z == "Junio":
                    diccionario1["Junio"] = lista1[5]
                if z == "Julio":
                    diccionario1["Julio"] = lista1[6]
                if z == "Agosto":
                    diccionario1["Agosto"] = lista1[7]
                if z == "Septiembre":
                    diccionario1["Septiembre"] = lista1[8]
                if z == "Octubre":
                    diccionario1["Octubre"] = lista1[9]
                if z == "Noviembre":
                    diccionario1["Noviembre"] = lista1[10]
                if z == "Diciembre":
                    diccionario1["Diciembre"] = lista1[11]
    except ValueError:

        raise NameError("Tienes que volver a introducir todas las temperaturas")



    return diccionario1

lista1=[]
meses1=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
diccionario1={}


def prom2(x):
    cont2 = 0
    b = x.values()
    for x in b:
        cont2 = cont2 + x
        d = cont2 / 12

    return d

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#Guajira
def base3():
    try:
        for x in range(0, 12):
            n = int(input("Introduce las temperaturas del mes {}: ".format(x+1)))
            lista2.append(n)
        for i in lista2:
            for z in meses2:
                if z == "Enero":
                    diccionario2["Enero"] = lista2[0]

                if z == "Febrero":
                    diccionario2["Febrero"] = lista2[1]
                if z == "Marzo":
                    diccionario2["Marzo"] = lista2[2]
                if z == "Abril":
                    diccionario2["Abril"] = lista2[3]
                if z == "Mayo":
                    diccionario2["Mayo"] = lista2[4]
                if z == "Junio":
                    diccionario2["Junio"] = lista2[5]
                if z == "Julio":
                    diccionario2["Julio"] = lista2[6]
                if z == "Agosto":
                    diccionario2["Agosto"] = lista2[7]
                if z == "Septiembre":
                    diccionario2["Septiembre"] = lista2[8]
                if z == "Octubre":
                    diccionario2["Octubre"] = lista2[9]
                if z == "Noviembre":
                    diccionario2["Noviembre"] = lista2[10]
                if z == "Diciembre":
                    diccionario2["Diciembre"] = lista2[11]

    except ValueError:

        raise NameError("Tienes que volver a introducir todas las temperaturas")

    return diccionario2

lista2=[]
meses2=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
diccionario2={}


def prom3(x):
    cont3 = 0
    f = x.values()
    for x in f:
        cont3 = cont3 + x
        e = cont3 / 12

    return e

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#Hallar el mes
def mes_caliente(x):
    oc = x.values()
    ca= max(oc)
    a=x.get("Enero")

    if a == ca:
        print("c) Su mes más caliente es enero")
        return ca
    else:
        a = x.get("Febrero")
        if a == ca:
            print("c) Su mes más caliente es Febrero")
            return ca
        else:
            a = x.get("Marzo")
            if a == ca:
                print("c) Su mes más caliente es Marzo")
                return ca
            else:
                a = x.get("Abril")
                if a == ca:
                    print("c) Su mes más caliente es Abril")
                    return ca

                else:
                    a = x.get("Mayo")
                    if a == ca:
                        print("c) Su mes más caliente es Mayo")
                        return ca

                    else:
                        a = x.get("Junio")
                        if a == ca:
                            print("c) Su mes más caliente es Junio")
                            return ca
                        else:
                            a = x.get("Julio")
                            if a == ca:
                                print("Su mes más caliente es Julio")
                                return ca
                            else:
                                a = x.get("Agosto")
                                if a == ca:
                                    print("c) Su mes más caliente es Agosto")
                                    return ca
                                else:
                                    a = x.get("Septiembre")
                                    if a == ca:
                                        print("c) Su mes más caliente es Septiembre")
                                        return ca
                                    else:
                                        a = x.get("Octubre")
                                        if a == ca:
                                            print("c) Su mes más caliente es Octubre")

                                            return ca
                                        else:
                                            a = x.get("Noviembre")
                                            if a == ca:
                                                print("c) Su mes más caliente es Noviembre")
                                                return ca
                                            else:
                                                a = x.get("Diciembre")
                                                if a == ca:
                                                    print("c) Su mes más caliente es Diciembre")
                                                    return ca


