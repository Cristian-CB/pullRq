lista = [2, 4, 1, 3, 7, 9]

def moverPosiciones(vector,n,dir):

    if dir == "izq":
        resultado = vector[n:] + vector[:n]
        return resultado

    else:
        resultado = vector[-n:] + vector[:-n]
        return resultado


print(moverPosiciones(lista,2,"izq"))