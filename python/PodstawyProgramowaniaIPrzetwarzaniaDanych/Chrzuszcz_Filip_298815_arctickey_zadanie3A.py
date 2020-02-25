import math

def insertion_sort(t):
    n = len(t)
    for i in range(1,n):
        x = t[i]
        j = i
        while j>0 and t[j-1]>x:
            t[j] = t[j-1]
            j-=1
        t[j]= x
    return t



def histogram(t,k,count=5):
    n = len(t)
    t = insertion_sort(t)
    najmniejszy = t[0]
    najwiekszy = t[-1]
    wmin = najmniejszy
    wmax = najwiekszy *1.0001
    skok_przedzialu = (wmax+wmin)/k
    l =wmin
    x = wmin +skok_przedzialu
    o = 0
    maks = 0
    for i in range(n):
         for j in range(k): 
            if t[i]<x:
                o+=1
            if o>maks:
                maks = o
         print('[',l,':',x,')','|'*o)
         o = 0
         l +=skok_przedzialu
         x +=skok_przedzialu
    

            

histogram([43,34,215,45],6)

with open('simulations.txt','r')as f:
        x = f.readline()
        x = int(x)
        lista = [0]*x
        for i in range(1000):
            lista[i] = f.readline()

