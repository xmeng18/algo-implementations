IM<- 2147483647
IMM1 <- IM -1
IA <- 16807
IQ <- 127773

IR <- 2836
NTAB <-32
NDIV <-1+(IM-1)/NTAB

MASK <- 123459976
AM <- 1.0/IM
EPS <- 1.2e-7
RNMX <- 1.-EPS

idum2<-123456789
idum<-100
numran<-100

ran1<-0
iy<-1
iv<-rep(0,NTAB)
random<-rep(0,numran)

icount<- 1
for (icount in 1:numran){
  if (idum <= 0){
    idum <- max(-idum,1)
    j = NTAB+8
    # K = idum/IQ
    j <- NTAB + 8
    
    while (j>0){
      
      k = as.integer(idum/IQ)
      
      idum<- IA*(idum-k*IQ)-k*IR
      
      if (idum<0){idum=idum+IM}
      
      if(j<=NTAB) {iv[j]<-idum}
      
      j<- j-1
      
      
    }
  
    iy <-iv[1]
    
  }

  k<- as.integer(idum/IQ)
  
  idum<-IA*(idum-k*IQ)-k*IR
  
  
  
  if (idum<0){idum=idum+IM}
  
  j<-as.integer(iy/NDIV)+1
  
  
  iy<-iv[j]-idum
  
  iv[j]<-idum
  if(iy<1){iy<-iy+IMM1}
  
  ran1<-min(AM*iy,RNMX)
  random[icount] = ran1
  icount = icount + 1;
  
}