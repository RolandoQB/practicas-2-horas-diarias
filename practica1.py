class practica():
    def __init__(self):
        pass
    def practica1(self,eje):
        n = len(eje)
        for i in range(n):
            eje[i] = int(eje[i])
        eje = tuple(eje)
        sum = 0
        sumsq = 0
        for i in eje:
            sum += i
            sumsq += i**2
        mean = sum/n
        stdev = (sumsq/n-mean**2)**(1/2)
        print('La media es', mean, ', y la desviación típica es', stdev)

prueba=practica()
muestra = input("Introduce una muestra de números separados por comas: ")
muestra = muestra.split(',')
prueba.practica1(muestra)
