pliki <- list.files("./pd2-zbiory-benchmarkowe","data(\\.gz|)$", recursive=TRUE)
labels <- list.files("./pd2-zbiory-benchmarkowe","labels0(\\.gz|)$", recursive=TRUE)


zapis4 <- function(){
  wyniki <- matrix(0,ncol=5)
  wyniki <- as.data.frame(wyniki)

  for(a in c(2,3,5,7,10,15,20)){
    srednia_Rand <- 0
    srednia_FM <- 0
    srednia_standard_Rand <- 0
    srednia_standard_FM <- 0
    srednia <- 0
    srednia1 <- 0
    srednia2 <- 0
    srednia3 <- 0
  for(i in 1:length(pliki)){
    dane <- paste("./pd2-zbiory-benchmarkowe",pliki[i],sep="/")
    x <- read.table(dane)
    x_standard <- scale(x)
    label <- paste("./pd2-zbiory-benchmarkowe",labels[i],sep="/")
    label <- read.table(label)
    label <- as.matrix(label)
    wynik <- e1071::cmeans(x,length(unique(as.vector(label))),m=a)
    wynik <- wynik$cluster
    wynik <- as.matrix(sort(wynik))
    wynik_standard <- e1071::cmeans(x_standard,length(unique(as.vector(label))),m=a)
    wynik_standard <- wynik_standard$cluster
    wynik_standard <- as.matrix(sort(wynik_standard))
    score <- mclust::adjustedRandIndex(label,wynik)
    score1 <- dendextend::FM_index(label,wynik)[1]
    score_standard <- mclust::adjustedRandIndex(label,wynik_standard)
    score1_standard <- dendextend::FM_index(label,wynik_standard)[1]
    srednia <- srednia+score
    srednia1 <- srednia1 +score1
    srednia2 <- srednia2+score_standard
    srednia3 <- srednia3+score1_standard
  }
  srednia_Rand <- srednia/length(pliki)
  srednia_FM <- srednia1/length(pliki)
  srednia_standard_Rand <- srednia2/length(pliki)
  srednia_standard_FM <- srednia3/length(pliki)
  wektor <- c(a,srednia_Rand,srednia_FM,srednia_standard_Rand,srednia_standard_FM)
  wyniki <- rbind(wyniki,wektor)
  }
  return(wyniki)
}


std4 <- function(){
  wyniki <- matrix(0,ncol=1)
  wyniki <- as.data.frame(wyniki)
  for(i in 1:length(pliki)){
    dane <- paste("./pd2-zbiory-benchmarkowe",pliki[i],sep="/")
    x <- read.table(dane)
    label <- paste("./pd2-zbiory-benchmarkowe",labels[i],sep="/")
    label <- read.table(label)
    label <- as.matrix(label)
    wynik <- e1071::cmeans(x,length(unique(as.vector(label))),m=a)
    wynik <- wynik$cluster
    wynik <- as.matrix(sort(wynik))
    score <- mclust::adjustedRandIndex(label,wynik)
    wektor <- c(score)
    wyniki <- rbind(wyniki,wektor)
  }
  return(wyniki)
}

y4 <- std4()
y4 <- y4[2:47,]
y4 <- round(y4,2)
write.csv(y4,"Cmeans_best")

x4 <- zapis4()
x4 <- x4[2:8,]
colnames(x4) <- c("M","Rand","FM","Rand_Scaled","FM_Scaled")
x4[,2] <- round(as.numeric(x4[,2]),2)
x4[,3] <- round(as.numeric(x4[,3]),2)
x4[,4] <- round(as.numeric(x4[,4]),2)
x4[,5] <- round(as.numeric(x4[,5]),2)
write.csv(x4,"Dane_cmeans")