def polinomioMas(gxC):
    gxSinX = gxC.replace('x','')
    gxSinElevado = gxSinX.replace('^','')
    return gxSinElevado

def polinomioGrado (gxNM):
    return gxNM[0:(gxNM.find('+'))]

def xOr(gxD,mD):
    if gxD == mD :
        return "0"
    else :
        return "1"

def addCero(r,m):
    for i in range(r):
        m = m+'0'
    return m

def polinomioLista(gxNM):
    cantidadNumeros = gxNM.count('+')
    lista = []
    for i in range(cantidadNumeros):
        lista.append(gxNM[0:(gxNM.find('+'))])
        gxNM = gxNM[gxNM.find('+')+1:len(gxNM)]
    lista.append(gxNM)
    return lista

def polinimioGenerado (lista):
    n = int(lista[0])
    u = lista.pop()
    b = ""
    for j in range(n):
        if(esElemento(str(j+1), lista)):
            b = '1' + b
        else:
            b = '0' + b       
    b = b + u
    return b

def esElemento(s,lista):
    e = False
    for i in range(len(lista)):
        if(s == lista[i]):
            e = True
    return e   

def division(gx,m):
    gxT = len(gx)
    mm = m[0:gxT]
    mC = m[gxT:len(m)]
    rf = miniXOr(gx,mm,gxT)
    f = 0
    c = 0
    r = ""
    while c == 0 :
        r = rf
        rf = quitaCeros(rf)
        mm = rf + mC[0:falta(gxT,rf)]
        if(len(gx)>len(mm)):
            if (f == 1):
                r = r + mC 
            break
        mC = mC[falta(gxT,rf):len(mC)]
        rf = miniXOr(gx,mm,gxT)
        if(len(mC) == 1):
            f = f + 1
    return r
    
    
def miniXOr(gx,mm,gxT):
    r = ""
    for i in range(gxT):
        r = r + xOr(gx[i],mm[i])
    return r

def quitaCeros(r):
    return r[r.find('1'):len(r)]

def falta(gxT,mm):
    return  gxT - len(mm)

def crc(r,div):
    return div[len(div)-r:len(div)]

def agregaCRC(m,crc):
    return m + crc
    
m = input ("Ingresa la trama que se desea enviar en binario :  ")
print("Ingresa el polinomio generador (ingresa el polinomio de las 2 siguientes posibles maneras y ")
gxC = input ("sin espacios: x4+x2+x1+1 o x^4+x^2+x^1+1):  ")
gxNM = polinomioMas(gxC)
gxLista = polinomioLista(gxNM)
r = polinomioGrado(gxNM)
mC = addCero(int(r),m)
gxB = polinimioGenerado( gxLista)
div = division(gxB,mC) 
crc = crc(int(r),div)
mCRC = agregaCRC(m,crc)
com = division(gxB,mCRC)
print("-_-_-_-_-_- Resultados -_-_-_-_-_-")
print("M : " + m)
print("G(x) : " + gxC)
print("r : " + r)
print("x^rM(x) : " + mC)
print("Polinomio generado en binario : " + gxB)
print("resuido de la division : " + div)
print("CRC : " + crc)
print("Trama unido con CRC : " + mCRC)
print("Comprobación : " + com)
print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")

