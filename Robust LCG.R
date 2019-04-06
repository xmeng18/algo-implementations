random = function(idum,numran){
IM1 <- 2147483563
IMM1 <- IM1 -1
IM2 <- 2147483399
IA1 <- 40014
IA2 <- 40692
IQ1 <- 53668
IQ2 <- 52774


IR1 <- 12211
IR2 <- 3791
NTAB <-32
NDIV <-1+IMM1/NTAB

AM <- 1.0/IM1
EPS <- 1.2e-7

RNMX <- 1.-EPS

idum2<-123456789
#idum<-100
#numran<-100000

ran1<-0
ran2 <- 0
iy<-1
iv<-rep(0,NTAB)

random<-rep(0,numran)

icount<- 1

for (icount in 1:numran){
  if(idum <=0){
    idum <- max(-idum,1);
    idum2 <- idum
    j <- NTAB + 8
    while (j>0){
      k <-as.integer(idum/IQ1)
      idum <- IA1*(idum - k*IQ1) - k*IR1
      if(idum<0){idum <- idum + IM1}
      if(j<=NTAB){iv[j] <- idum}
      j<- j-1
    }
    
    iy <-iv[1]
    
  }
  
  
  k <- as.integer(idum/IQ1)
  idum <- IA1*(idum-k*IQ1)-k*IR1
  
  if(idum<0){idum <- idum +IM1}
  k <- as.integer(idum2/IQ2)
  idum2 <- IA2*(idum2 - k*IQ2)-k*IR2
  if(idum2 <0){idum2 <- idum2+IM2}
  j <- as.integer(iy/NDIV)+1
  
  iy <- iv[j]-idum2
  iv[j] <- idum
  
  if(iy<1){
    
    iy<-iy+IMM1
    
    }
  ran2 <- min(AM*iy,RNMX)
  random[icount] <- ran2
  icount <- icount +1

}
return( random)
}













