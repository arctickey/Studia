pliki <- list.files("./pd2-zbiory-benchmarkowe","data(\\.gz|)$", recursive=TRUE)
labels <- list.files("./pd2-zbiory-benchmarkowe","labels0(\\.gz|)$", recursive=TRUE)


zapis1 <- function(){
  wyniki <- matrix(0,ncol=5)
  wyniki <- as.data.frame(wyniki)
    for(a in seq(0.1,1,0.1)){
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
        wynik <- genie::hclust2(dist(x),thresholdGini = a)
        wynik <- stats::cutree(wynik,length(unique(label)))
        wynik_standard <- genie::hclust2(dist(x_standard),thresholdGini = a)
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
      wektor <- c(a,srednia_Rand,srednia_FM,srednia_standard_Rand,srednia_standard_FM)
      wyniki <- rbind(wyniki,wektor)
  }
  return(wyniki)
}
std1 <- function(){
  wyniki <- matrix(0,ncol=1)
  wyniki <- as.data.frame(wyniki)
  for(i in 1:length(pliki)){
    dane <- paste("./pd2-zbiory-benchmarkowe",pliki[i],sep="/")
    x <- read.table(dane)
    label <- paste("./pd2-zbiory-benchmarkowe",labels[i],sep="/")
    label <- read.table(label)
    label <- as.matrix(label)
    wynik <- genie::hclust2(dist(x),thresholdGini = 0.5)
    wynik <- cutree(wynik,length(unique(label)))
    score <- mclust::adjustedRandIndex(label,wynik)
    wektor <- c(score)
    wyniki <- rbind(wyniki,wektor)
  }
  return(wyniki)
}

y <- std1()
y <- y[2:47,]
y <- round(y,2)
write.csv(y,"Genie_best")

x1 <- zapis1()
x1 <- x1[2:11,]
colnames(x1) <- c("Gini","Rand","FM","Rand_Scaled","FM_Scaled")
x1[,2] <- round(as.numeric(x1[,2]),2)
x1[,3] <- round(as.numeric(x1[,3]),2)
x1[,4] <- round(as.numeric(x1[,4]),2)
x1[,5] <- round(as.numeric(x1[,5]),2)
write.csv(x1,"Dane_genie")
Genie_alg <- x1
