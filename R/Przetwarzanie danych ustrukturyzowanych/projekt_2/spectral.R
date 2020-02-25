
spectral_clustering<- function(X,M,k){

Mnn <- function(X,M){
  m <- matrix(0,nrow(X),nrow(X)) #tworze pusta macierz
  m <- as.data.frame(as.matrix(dist(X))) #macierz odleglosci punktow od siebie
  m[row(m)==col(m)] <- Inf  #ustawiam punkty na przekatnej na nieskoncznosc zeby nie brac ich pod uwage
  m <- t(apply(m,1,order)[1:M,]) #ustawiam w kolejnosci tak zeby kolejne kolumny odpowiadaly
  #kolejnym punktom od siebie i biore M z nich
  m <- as.matrix(m) #jako macierz aby latwiej bylo pracowac potem na danych
  return(m)
}
Mnn_graph <- function(S){
  ro <- rep(1:nrow(S), each = ncol(S)) #ustawiam dane, aby stworzyc macierz sasiedztwa
  co <- unlist(as.data.frame(t(S))) 
  points <- cbind(ro, co) # punkty do macierz sasiadow
  sym_points <- cbind(co, ro)#symetryczne punkty do macierzy sasiadow
  m<- matrix(0, nrow = nrow(S), ncol = nrow(S)) # tworza pusata macierz o odpowiednich wymiarach
  m[points] <- 1 #ustawiam sasiadow na 1
  m[sym_points] <- 1 #ustawiam punkty symetryczne do sasiadow na 1 tak aby macierz byla symetryczna
  gra <- graph.adjacency(m) #robimy graf z tej macierzy
  com <- components(gra) #szukamy skladowych
  comp <- igraph::groups(com)#zwracamy skladowe
  if(length(comp)==1){ #jezeli mamy jedna skladowa to zwroc macierz
    m <- as.matrix(m)
    return(m)
  }
  elem <- lapply(comp, `[[`, 1) # jezeli mamy wiecej niz jedna skladowa to
  #bierzemy po jednym elemencie z kazdej skladowej aby uspojnic graf
  elem <- unlist(elem) 
  for(i in 1:length(elem)){ #jest to mala petla wiec nie zwolni znaczaco algorytmu
    m[elem[i-1],elem[i]] <- 1 #laczymy ze soba kazdy pierwszy punkt z kazdej skladowej
    m[elem[i],elem[i-1]] <- 1 #symetrycznie to co wyzej
  }
  m <- as.matrix(m)
  return(m)
}
Laplacian_eigen <- function(G,k){
  m <- Matrix(G,sparse = TRUE) #uzywamy pakietu Matrix aby otrzymac macierz rzadka tak jak w poleceniu
  #i zaoszczedzic troche pamieci
  m <- graph.adjacency(m,mode="undirected")#korzystamy z igrpha aby stworzyc graf a potem otrzymac laplacian
  laplace <- laplacian_matrix(m) #tworzymy macierz laplacianu
  wartosci <- eigen(as.matrix(laplace))#robimy wartosci wlasne
  wektory <- wartosci[[2]] #bierzemy wektory wlasne
  E <- wektory[,(ncol(wektory)-k+1):ncol(wektory)] #bierzemy odpowiodnio k najwiekszych wektorow
  return(E)
}

  var <- Mnn(X,M) #pusczamy kazda z funkcji
  var <- Mnn_graph(var)
  var <- Laplacian_eigen(var,k)
  var <- kmeans(var,k,nstart = 25) #uzywamy opcji nstart aby zwiekszyc stabilnosc dzialania kmeans
  #oraz aby otrzymac spojne wyniki
  wynik <- as.vector(unlist(var[1]))
  wynik <- sort(wynik) #sortujemy wynik, bo tego wymagaja mclust oraz dendextend aby poprawnie analizowac
  #i porownywac poprawnosc danych
  return(as.matrix(wynik))
}



