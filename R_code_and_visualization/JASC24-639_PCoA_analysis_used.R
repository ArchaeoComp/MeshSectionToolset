library(FD)
library(ggplot2)
library(cluster)
library(dbscan)
library(plotly)
library(here)


###################################################################
## This R code use data exported from Slicing Tool for Blender. It was used for performing of Gowers distance analysis (figures 8 and 9 in the article)
## The figures 5-7 (rows H1, H2, A1 and A2) are ploted in Blender and they was manually transformed/scaled according to graphs transformations according to Fusek 1994.
###################################################################
##
## 1) Calculate gower distance
##
## This section of code loads dataset of extracted variables from Blender Slicing tool and perform Gowers distance,
## then use Multidimensional scaling tool (Principled Coordinate Analysis -PCoA)
## (in format of .txt, pleas ensure that . is used as decimal symbol; It is mandatory, to have names of object in first row)
## For Gover_matrix function, it is mandatory to have defined weights for each row in form of R vector(no more, no less than number of rows - first row, otherwise there will be an error:
##
## gower_matrix2 <- gowdis(df, w)
## Error in gowdis(df, w) :
## w needs to be a numeric vector of length = number of variables in x
##
###################################################################
df <- read.csv(here("data/JASC24-639_Data_PCoA_used.txt"),row.names = 1, header = TRUE, sep="\t", )

variables <- colnames(df)

#Weights - it is mandatory to have defined weights for each row in form of R vector. For example in our case, the Hindex use only H values in calculation, others are == 0
w1 <- c(0,0,0,0,0,0,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0) #Hindex dataset
w2 <- c (0,0,1,2,3,3,1,1,0,0,0,0,0,0,1,1,3,2,2,1,0) #Technology similarity
w <- w2

gower_matrix2 <- gowdis(df, w)
gower_matrix2

## cmdscale() is the function for "Classical Multi-Dimensional Scalign" = PCoA; This takes the results of distances (in our case Gowers distance matrix) and use some fancy statistics
mds.stuff <- cmdscale(as.dist(gower_matrix2),
                      eig=TRUE,
                      x.ret=TRUE,
                      k = 3)

## calculate the percentage of variation that each PCoA axis accounts for...
mds.var.per <- round(mds.stuff$eig/sum(mds.stuff$eig)*100, 3)
mds.var.per


## now make a fancy looking plot that shows the PCoA axes and the variation
## (this part is only for visualization of pattern, final plots for
## figures 8 and 9 was graphically enhanced in Blender, where
## those reults was used as X,Y,Z coordinates. See part "Export dataset to .csv"):

mds.values <- mds.stuff$points
mds.data <- data.frame(Sample=rownames(mds.values),
                       X=mds.values[,1],
                       Y=mds.values[,2],
                       Z=mds.values[,3])
mds.data
mds_data <- mds.data
mds.data$Site <- df$Site

ggplot(data=mds.data, aes(x=X, y=Y, label=Sample, color=Site )) +
  #geom_text(size=2) +
  geom_point(size=2) +
  theme_bw() +
  xlab(paste("PCoA1 - ", mds.var.per[1], "%", sep="")) +
  ylab(paste("PCoA2 - ", mds.var.per[2], "%", sep="")) +
  #ggtitle("PCoA plot using gower's coeficient as the distance")#
  ggtitle(paste("PCoA plot using gower's coefficient as the distance:"))




###################################################################
##
## 2) Eport dataset to .csv, using three axes of PCoA as 3D coordinates for coresponding 3D models visualization in Blender software (rename output .csv for selected weights Hindex/Technology similarity)
##
###################################################################


# Creation of a data frame for export (including percentage variance for the axes)
mds.data <- data.frame(Sample = rownames(mds.stuff$points),
                       X = mds.stuff$points[,1],
                       Y = mds.stuff$points[,2],
                       Z = mds.stuff$points[,3],
                       PCoA1 = mds.var.per[1],  # Percents for PCoA1
                       PCoA2 = mds.var.per[2],  # Percents for PCoA2
                       PCoA3 = mds.var.per[3])  # Percents for PCoA3

write.csv(mds.data, file = here("data/Technology similarity.csv"), row.names = FALSE)

