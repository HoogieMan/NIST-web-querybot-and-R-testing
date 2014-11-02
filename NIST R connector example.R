setwd("~/R/RSocrata/R")
source("RSocrata.R")
library(ggplot2)

## R Connector for Socrata ##
nistDF <- read.socrata("https://nist-stat.demo.socrata.com/Measurement-Standards/NIST-Atomic-Spectra-Database/26uj-tyzz")

head(nistDF,50)

nrow(nistDF)

selectDF <- nistDF[,c('Atomic_Number','Element_Name','Ionization_Energy')]
atom1DF <- selectDF[ selectDF[, "El. name"]=="Hydrogen",]
atom2DF <- selectDF[ selectDF[, "El. name"]=="Helium",]
dataFrame <- rbind(atom1DF, atom2DF)

at1Vec <- atom1DF$Ionization Energy
at2Vec <- atom2DF$Ionization Energy

##ggplot2 correlation plot##
ggplot(dataFrame, aes(x=at1Vec, y=at2Vec))+
  geom_point(shape=16, size= 4, color = "red") +
  geom_smooth(method=lm)+ 
  theme(                              
    axis.title.x = element_text(face="bold", color="black", size=20),
    axis.title.y = element_text(face="bold", color="black", size=20),
    plot.title = element_text(face="bold", color = "black", size=30))+
  labs(x="Relative Correlation - Atomic Vector 1", 
       y="Relative Correlation - Atomic vector 2",
       title="Correlation Between Two Atomic Vectors, via Socrata R Connector")