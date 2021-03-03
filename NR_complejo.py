import math

#Quitar las veces que se repita las raices complejas
#agregar cuando la funcion es concava hacia arriba o abajo

def horner(grado, coeficientes, x):
    polinomio = coeficientes[grado]
    k = grado - 1
    while k >= 0:
        polinomio = coeficientes[k] + (polinomio*x)
        k = k - 1
    return polinomio

print("Ingresa el grado del polinomio: ")
grado = int(input())

polin = []
dx = []
i = 0

print("Ingresa el grado de los coeficientes empezando por el termino independiente: ")
while(i <= grado):
    polin.append(float(input()))
    i = i + 1

a = 70 + 150j

theta = math.atan(a.imag/a.real)
phi= 2*math.pi / (grado*2)
r = float(abs(a))
 
#print("Ingresa el punto a evaluar")
#x0 = float(input())

i = 0
for x in polin:
    if(i!=0):
        dx.append(0)
        dx[i-1] = x*i
    i = i + 1

d2x = []    
i=0
for x in dx:
    if(i!=0):
        d2x.append(0)
        d2x[i-1] = x*i
    i = i + 1

d3x = []    
i=0
for x in d2x:
    if(i!=0):
        d3x.append(0)
        d3x[i-1] = x*i
    i = i + 1

print("Introduce la cifra significativa: ")
CifSig = float(input())
tolerancia = (0.5*(10**(2-CifSig)))
comparacion = 0
n = 0
while n < grado*2:
    real =float(r * math.cos(theta + phi * n))
    img =float(r * math.sin(theta + phi * n))
    x0 = complex(real,img)
    error = 1 
    xant = 0

    while error >= tolerancia:
        fx = horner(grado, polin, x0)
        dfx = horner(grado - 1, dx, x0)
        x1 = x0 - fx/dfx
        if x1 != 0:
            error = abs((x1-xant)/x1)
            xant = x1 
            x0 = x1 
        else:
            error = 0
    if((x1.imag < 0.00001) and (x1.imag > -0.00001)):    
        print("La raiz mas cercana es : ",x1.real)
    else:
        print("La raiz mas cercana es : ",x1)    
    comparacion = x1    
    n = n + 1 

intervalo = abs(dx[0])+3
comparacion = 0
a = intervalo*(-1)    
puntoscrit = []
i = 0
while a <= intervalo:
    x0 = a
    error = 1 
    xant = 0

    while error >= tolerancia:
        fx = horner(grado - 1, dx, x0)
        dfx = horner(grado - 2, d2x, x0)

        if(dfx != 0 and x1 != 0):
            x1 = x0 - fx/dfx
            if x1 != 0:
                error = abs((x1-xant)/x1)
                xant = x1 
                x0 = x1
            else:  
                error = 0    
        else:
            error = 0 
    if(comparacion != x1):        
        puntoscrit.append(0)
        puntoscrit[i] = x1
        i = i + 1
    comparacion = x1
    a = a + 1    

for x in puntoscrit:
    antes = horner(grado - 1, dx, x-0.001)
    despues = horner(grado - 1, dx, x+0.001)
    if antes < 0:
        print("La función es decreciente antes de: ",x)
    else:
        print("La función es creciente antes de: ",x)  

    if despues < 0:
        print("La función es decreciente despues de: ",x)
    else:
        print("La función es creciente despues de: ",x)          

intervalo = abs(d2x[0])+3
comparacion = 0
a = intervalo*(-1)    
concavo = []
i = 0
while a <= intervalo:
    x0 = a
    error = 1 
    xant = 0

    while error >= tolerancia:
        fx = horner(grado - 2, d2x, x0)
        dfx = horner(grado - 3, d3x, x0)

        if(dfx != 0 and x1 != 0):
            x1 = x0 - fx/dfx
            if x1 != 0:
                error = abs((x1-xant)/x1)
                xant = x1 
                x0 = x1
            else:  
                error = 0    
        else:
            error = 0 
    if(comparacion != x1):        
        concavo.append(0)
        concavo[i] = x1
        i = i + 1
    comparacion = x1
    a = a + 1 

for x in concavo:
    antes = horner(grado - 1, dx, x-0.001)
    despues = horner(grado - 1, dx, x+0.001)
    if antes < 0:
        print("La función es concava hacia abajo antes de: ",x)
    else:
        print("La función es concava hacia arriba antes de: ",x)  

