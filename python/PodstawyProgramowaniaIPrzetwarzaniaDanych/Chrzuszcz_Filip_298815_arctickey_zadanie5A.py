import random
import math
import csv
import matplotlib.pyplot as plt


x =[]
f = open('faithful.csv', "r") # r=do odczytu
for row in csv.reader(f):
    for i in range(len(row)):
        row[i] = float(row[i]) # konwersja z str na float
    list.append(x, row) # == A.append(row)
f.close()

def distance(ai,aj):
    '''liczymy dystans'''
    pierwszy = (ai[0]-aj[0])**2
    drugi = (ai[1]-aj[1])**2
    return math.sqrt(pierwszy + drugi) #zwracamy pierwiastek
def unique(x):
    '''szukamy unikalnych'''
    wynik =[]
    for i in range(len(x)):
        if x[i] not in wynik:
            wynik.append(x[i])
    return wynik #zwracamy unikalne


def transpose(x):
    '''funkcja pomoicnicza'''
    wynik = [[0]*len(x) for i in range(len(x[0]))]
    for i in range(len(x)):
        for j in range(len(x[0])):
            wynik[j][i] = x[i][j]
    return wynik

def srednia(x):
    '''pomocnicza srednia'''
    suma =0 
    for i in range(len(x)):
        suma +=x[i]
    
    return suma/len(x) #zwrot sredniej


def centroids(A,c):
    '''liczymy centroidy'''
    assert len(c) == len(A) #sprawdzamy wymkiary
    lista = unique(c)
    pom_x= [[]for i in range(len(lista))]
    pom_y = [[]for i in range(len(lista))]
    wynik_x =[]
    wynik_y = []#listy pomocnicze
    konc =[]
    A = transpose(A)
    x = A[0]
    y = A[1]
    for i in range(len(x)):
        pom_x[c[i]].append(x[i])
    for j in range(len(y)):
        pom_y[c[j]].append(y[j])
    for k in range(len(pom_x)):
        wynik_x.append(srednia(pom_x[k]))
    for l in range(len(pom_y)):
        wynik_y.append(srednia(pom_y[l]))
    for a in range(len(wynik_x)):
        konc.append([wynik_x[a],wynik_y[a]]) #ostateczne centroidy
    return konc
    


def updateGroups(A,y):
    '''liczymy grupy'''
    wynik =[]
    mini = math.inf
    for i in range(len(A)):
        a=0 #licznik
        for j in range(len(y)):
            if distance(A[i],y[j])<mini:
                a = j
        wynik.append(a)
        mini = math.inf
    return wynik

def kmeans(A,k,maxiter=50):
    '''algorytm'''
    lista =[]
    for i in range(len(A)):
        lista.append(random.randint(0,k))
    x =centroids(A,lista)
    for j in range(maxiter): #iterujemy 
        grupa = updateGroups(A,x)
        lista[j] = grupa[j]
    centr_konc = centroids(A,lista)
    return lista,centr_konc #zwracamy koncowa lista i centroidy

g = kmeans(x, 2, 50)
#rysunek
for i in range(len(x)):
    for j in range(len(x[0])):
        if g[0][i]==0:
            plt.scatter(x[i][0],x[i][1],c='r')
        elif g[0][i]==1:
            plt.scatter(x[i][0],x[i][1],c='b')
        plt.scatter(g[1][0][0],g[1][0][1],s=100,c='r')
        plt.scatter(g[1][1][0],g[1][1][1],s=100,c='b')

plt.show()
    

    

