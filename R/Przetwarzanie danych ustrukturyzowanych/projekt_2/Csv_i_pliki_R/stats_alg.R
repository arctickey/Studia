pliki <- list.files("./pd2-zbiory-benchmarkowe","data(\\.gz|)$", recursive=TRUE)
labels <- list.files("./pd2-zbiory-benchmarkowe","labels0(\\.gz|)$", recursive=TRUE)
opts <- c("ward.D", "ward.D2", "single", "complete", "average", "mcquitty", "median","centroid") 


x <- read.table("output.csv")
zapis <- function(){
  wyniki <- matrix(0,ncol=6)
  wyniki <- as.data.frame(wyniki)
  for(b in opts){
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
      wynik <- stats::hclust(dist(x),method = b)
      wynik <- stats::cutree(wynik,length(unique(label)))
      wynik_standard <- stats::hclust(dist(x_standard),method=b)
      wynik_standard <- stats::cutree(wynik_standard,length(unique(label)))
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
    wektor <- c(b,srednia_Rand,srednia_FM,srednia_standard_Rand,srednia_standard_FM)
    wyniki <- rbind(wyniki,wektor)
    }
    return(wyniki)
}

std3 <- function(){
  wyniki <- matrix(0,ncol=1)
  wyniki <- as.data.frame(wyniki)
  for(i in 1:length(pliki)){
    dane <- paste("./pd2-zbiory-benchmarkowe",pliki[i],sep="/")
    x <- read.table(dane)
    label <- paste("./pd2-zbiory-benchmarkowe",labels[i],sep="/")
    label <- read.table(label)
    label <- as.matrix(label)
    wynik <- stats::hclust(dist(x),method="ward.D")
    wynik <- cutree(wynik,length(unique(label)))
    score <- mclust::adjustedRandIndex(label,wynik)
    wektor <- c(score)
    wyniki <- rbind(wyniki,wektor)
  }
  return(wyniki)
}

y3 <- std3()
y3 <- y3[2:47,]
y3 <- round(y3,2)
write.csv(y3,"Stats_best")

x <- zapis()
x <- x[2:9,1:5]
colnames(x) <- c("Algorytm","Rand","FM","Rand_Scaled","FM_Scaled")
x[,2] <- round(as.numeric(x[,2]),2)
x[,3] <- round(as.numeric(x[,3]),2)
x[,4] <- round(as.numeric(x[,4]),2)
x[,5] <- round(as.numeric(x[,5]),2)
write.csv(x,"Dane_stats")
Stats_alg <- x