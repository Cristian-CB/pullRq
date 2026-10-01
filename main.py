lista = [2, 4, 1, 3, 7, 9]
resultado = lista[-2:] + lista [:-2]
direccion = "izq"




def moverPosicionesDerecha(lista,n):

    if direccion == "izq":
        resultado = lista[n:] + lista[:n]
        return resultado

    else:
        resultado = lista[-n:] + lista[:-n]
        return resultado


print(moverPosicionesDerecha(lista,2))
