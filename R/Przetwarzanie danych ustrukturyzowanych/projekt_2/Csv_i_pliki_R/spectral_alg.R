pliki <- list.files("./pd2-zbiory-benchmarkowe","data(\\.gz|)$", recursive=TRUE)
labels <- list.files("./pd2-zbiory-benchmarkowe","labels0(\\.gz|)$", recursive=TRUE)

zapis2 <- function(){
  wyniki <- matrix(0,ncol=5)
  wyniki <- as.data.frame(wyniki)
  for(j in c(2,3,5,7,10,12,15)){
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
        wynik <- spectral_clustering(x,j,length(unique(label)))
        wynik_standard <- spectral_clustering(x_standard,j,length(unique(label)))
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
      wektor <- c(j,srednia_Rand,srednia_FM,srednia_standard_Rand,srednia_standard_FM)
      wyniki <- rbind(wyniki,wektor)
  }
  return(wyniki)
}
std2 <- function(){
  wyniki <- matrix(0,ncol=1)
  wyniki <- as.data.frame(wyniki)
  for(i in 1:length(pliki)){
    dane <- paste("./pd2-zbiory-benchmarkowe",pliki[i],sep="/")
    x <- read.table(dane)
    label <- paste("./pd2-zbiory-benchmarkowe",labels[i],sep="/")
    label <- read.table(label)
    label <- as.matrix(label)
    wynik <- spectral_clustering(x,12,length(unique(label)))
    score <- mclust::adjustedRandIndex(label,wynik)
    wektor <- c(score)
    wyniki <- rbind(wyniki,wektor)
  }
  return(wyniki)
}

y2 <- std2()
y2 <- y[2:47,]
y2 <- round(y,2)
write.csv(y2,"Spectral_best")


x2 <- zapis2()
x2 <- x2[2:8,]
colnames(x2) <- c("M","Rand","FM","Rand_Scaled","FM_Scaled")
x2[,2] <- round(as.numeric(x2[,2]),2)
x2[,3] <- round(as.numeric(x2[,3]),2)
x2[,4] <- round(as.numeric(x2[,4]),2)
x2[,5] <- round(as.numeric(x2[,5]),2)

write.csv(x2,"Dane_Spectral")

