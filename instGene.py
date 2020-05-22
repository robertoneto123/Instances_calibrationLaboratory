import math
import numpy
import os

NOFFILES = 20
NOFORDERS = [5, 10, 15, 20, 30, 40, 50, 100, 200]
COMPATIBILITY = [0.25, 0.5, 0.75, 1]
SIZE = [4, 6, 8]

#@param n Number of orders
def getSizeArray(n):
    return [0]*n

#@param n Number of orders
def getProcessingArray(n):
    limiteF = [106, 345]
    limiteO = [0.2, 0.4]
    limiteCertificado = [20, 75]
    ret = [[0,0,0]]
    for i in range(n-1):
        a = numpy.random.randint(low=limiteF[0],high=limiteF[1])
        b = int((numpy.random.rand() * (limiteO[1] - limiteO[0]) + limiteO[0]) * a)
        c = numpy.random.randint(low=limiteCertificado[0],high=limiteCertificado[1])
        ret.append([a, b, c])
    return ret

def getCompatibilityArray(n, c):
    ret = numpy.zeros((n, n))
    for x in range(n):
        for y in range(n):
            if x != y:
                if numpy.random.rand() <= c:
                    ret[x][y] = 1
                    ret[y][x] = 1
            else:
                ret[x][y] = 1
    return ret


if not os.path.exists("data"):
    os.makedirs("data")
for n in NOFORDERS:
    if not os.path.exists("data/"+str(n)):
        os.makedirs("data/"+str(n))
    for c in COMPATIBILITY:
        for s in SIZE:
            for i in range(NOFFILES):
                arquivo = open("data/"+str(n)+"/data_"+str(n)+"_"+str(c)+"_"+str(s)+"_"+str(i)+".txt", "w")
                arquivo.write(str(n)+"\t"+str(s)+"\n")
                for p in getProcessingArray(n):
                    arquivo.write("\t".join(str(a) for a in p))
                    arquivo.write("\n")
                compatibility = getCompatibilityArray(n, c)
                for x in range(n):
                    for y in range(n):
                        arquivo.write(str(compatibility[x][y])+"\t")
                    arquivo.write("\n")
                arquivo.flush()
                arquivo.close()
