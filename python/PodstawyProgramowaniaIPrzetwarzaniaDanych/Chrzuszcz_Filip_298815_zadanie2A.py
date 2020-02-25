import sys
import random
import math
import matplotlib.pyplot as plt
import numpy as np
random.seed(12345)

def f(x):
    """
    f: R -> R
    Nie interesuje nas kod funkcji.
    """
    t = 0.1 
    if x < -4:
        return(x**2 - 10.46)
    elif x <= 4:
        return(t*math.cos(14*x) + (1 - t) * 8*math.sin(x))        
    elif x <= 6:
        return(t*math.cos(x) + (1 - t) * 0.5*math.sin(14*x))  
    else:
        return(t*math.cos(6) + (1 - t) * 8*math.sin(14*6))

with open('input.txt','w') as l:
    l.write(str(1000))
    l.write('\n')
    l.write(str(50))
    l.write('\n')
    l.write(str(1))
    l.write('\n')
    l.write(str(-5))
    l.write('\n')
    l.write(str(5))
    l.write('\n')
with open('input.txt','r') as l:
    N = int(l.readline())
    T0 =  int(l.readline())
    Tn =  int(l.readline())
    a =  int(l.readline())
    b =  int(l.readline())

def simulated_annealing(f,N,T0,Tn,a,b):
    if N<0 or Tn>T0 or a>b:
        sys.exit()
    for k in range(N):
        x = random.uniform(a,b) 
        dod = random.uniform(-1,1)
        y = x +dod
        if f(x)>f(y):
            x=y
        else:
            u2 = random.uniform(0,1)
            if math.exp((f(x)-f(y)/T0))<u2:
                x=y
    T0 = T0*math.exp(-(k/N)*math.log2(T0/Tn))
    return x
    


k =simulated_annealing(f,N,T0,Tn,a,b)
l = f(k)
            
with open('output.txt','w') as d:
    print(str.format('{0:^1s}{1:^5d}','a=',a),file=d)
    print(str.format('{0:^1s}{1:^5d}','b=',b),file=d)
    print(str.format('{0:^1s}{1:^5d}{2:^5s}{3:^5.03f}','N=',N,'x=',k),file=d)
    print(str.format('{0:^1s}{1:^5d}{2:^5s}{3:^5.03f}','TO=',T0,'f(x)=',l),file=d)
    print(str.format('{0:^1s}{1:^5d}','Tn=',Tn),file=d)


fig = plt.figure()
u = np.linspace(a,b)
v = [f(x) for x in u]
plt.plot(u,v)
fig.savefig('output.png',dpi=90)


def g(x):
    return math.sin(x**2) + abs(x)


suma = 0
for N in range(1000,11000,1000):
    for i in range(100):
        k = simulated_annealing(g,N,T0,Tn,a,b)
        l = g(k)
        m = l-0
        suma +=m
    blad = suma/1000
with open('simulations.txt','w') as a:
    for i in range(10):
        for j in range(1):
            if i == 0:
                print(str.format('{0:^1s}{1:^5s}','N |', 'm.error'),file=a)
                print(str.format('{0:^1s}{1:^5f}','1000| ',blad),file=a)
                print(str.format('{0:^1s}{1:^5f}','2000| ',blad),file=a)
                print(str.format('{0:^1s}{1:^5f}','3000| ',blad),file=a)
                print(str.format('{0:^1s}{1:^5f}','4000| ',blad),file=a)
                print(str.format('{0:^1s}{1:^5f}','5000| ',blad),file=a)
                print(str.format('{0:^1s}{1:^5f}','6000| ',blad),file=a)
                print(str.format('{0:^1s}{1:^5f}','7000| ',blad),file=a)
                print(str.format('{0:^1s}{1:^5f}','8000| ',blad),file=a)
                print(str.format('{0:^1s}{1:^5f}','9000| ',blad),file=a)
                print(str.format('{0:^1s}{1:^5f}','10000| ',blad),file=a)






