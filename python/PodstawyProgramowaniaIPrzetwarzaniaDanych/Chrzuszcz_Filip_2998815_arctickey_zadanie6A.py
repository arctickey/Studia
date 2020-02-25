import matplotlib.pyplot as plt
import math

class Graph():
    def unique(x):
        '''Metoda pomocnicza'''
        wynik = []
        for i in range(len(x)):
            if x[i] not in wynik:
                wynik.append(x[i]) #szukamy unikalnych wartosci
        return wynik
            
    def __init__(self,edges):
        '''Konstruktor'''
        self.__edges = edges #przypisanie
        assert type(edges) == list #sprawdzenie typu
        self.len = len(self.__edges) #dlugosc listy
        for i in range(len(self.__edges)):
            self.__edges[i] = Graph.unique(edges[i]) #sprawdzamy zeby sie nie powtarzalo
            if i in self.__edges[i]:
                self.__edges[i].remove(i) #usuwamy zle
            for j in range(len(self.__edges[i])):
                if self.__edges[i][j]>self.len:
                    raise Exception('Too big')  #zwrot wyjatku
    
    def get_edges(self):
        '''Zwraca wierzcholki'''
        print(self.__edges)

    def __len__(self):
        '''Zwraca dlugosc'''
        return self.len
    
    def add_vertex(self,lista):
        '''Dodawanie wierzcholkow'''
        assert type(lista) == list
        nowa = [[] for i in range(self.len+1)] #nowa lista
        for i in range(self.len+1):
            if i >self.len:
                nowa[i] = self.__edges[i] #przepisanie
            else:
                nowa[self.len] = lista
        return Graph(nowa) #zwrot w postaci klasy tego obiektu
    
    def add_edge(self,v1,v2):
        '''Dodawanie krawedzi'''
        assert type(v1)==int #sprawdzenie danych
        assert type(v2) == int  #sprawdzenie danych
        if v1>self.len or v1<0:
            raise Exception('Bad value') #ewentualne bledy
        if v2>self.len or v2<0:
            raise Exception('Bad value')
        if v1 in self.__edges[v2] and v2 in self.__edges[v1]: #jesli juz mamy cos takiego
            raise Exception('Already there')
        else:
            self.__edges[v1].append(v2) #jesli wszystko ok,dodawanie danych
            self.__edges[v2].append(v1)


    def plot(self):
        '''Rysunek strzalek'''
        lista = []
        t =0
        for i in range(self.len):
            lista.append([math.sin(t),math.cos(t)])
            t +=2*math.pi/self.len #dzielimy okrag co odpowiedni kąt
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.set_xlim([-1, 1]) #limity na osiach
        ax.set_ylim([-1, 1])
        x =[] #lista z wspolrzednymi x
        y =[] #lista z wspolrzednymi y
        for i in range(len(lista)):
            x.append(lista[i][0]) #uzupelniami odpowiednimi punktami
            y.append(lista[i][1]) #uzupelniami odpowiednimi punktami
        for i in range(len(x)):
             plt.scatter(x[i],y[i])
        for i in range(self.len):
            ax.text(x[i],y[i],'%d'%i,size=20,horizontalalignment="center", verticalalignment="center") #tekst przy wierzchlokach
        for i in range(self.len):
            for j in range(len(self.__edges[i])):
                plt.arrow(x[i],y[i],(x[self.__edges[i][j]]-x[i]),(y[self.__edges[i][j]]-y[i]),head_width=0.07, head_length=0.15, fc="k",length_includes_head=True) #strzalki
        ax.axis("off") # nie rysuj osi
        ax.axis("equal") # OX i OY proporcjonalne
        plt.show()





   
G = Graph([[2,4],[1,2],[4,1,2,3],[1,2,3],[4,1,2]])
G.plot()
