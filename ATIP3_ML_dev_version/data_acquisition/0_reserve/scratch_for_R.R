
# ORFs = unique(as.character(dictionary$ORF)) # for the test
# yORFs = ORFs[grep( "Y\\w{2}\\d{3}.*", ORFs)]  #these are yeast ORFs
# str(yORFs)
# setdiff(ORFs, yORFs)
# ORFs = yORFs
# str(ORFs)
ORFs = unique(as.character(dictionary$"Gene Symbol")) # for the three cohorts
# remove the lines without gene symbol
if ("" %in% ORFs) {
  ORFs = ORFs[ORFs != ""]
}else {
  ORFs=ORFs
}
str(ORFs)

# lets see an oversview of the number of fts in our expression set object 
str(ex)
#########
# A simple approach to create an expression matrix with ORFs as row names
# This approach takes only one probe for each ORFs, which is often true for cDNA arrays

# ex2 = ex[match(ORFs, dictionary$ORF), ]   
ex2 = ex[match(ORFs, dictionary$"Gene Symbol"), ] # match return a vector of the pos of 1st occurence of vector 1 in vector 2
rownames(ex2) = ORFs
head(ex2) #Now, expression matrix is named by ORFs
# issue is we must not select the first occurence as kept probe but the best probe as kept probe see JETSET tool for that
##########
#Another approach is to calculate the average sigals for all the probes in the same ORFs
multipleProbedORFs = NA;
ex3 = ex2 #This is just a template
# orf = 'YLR331C'
# orf = "BCDIN3D-AS1"
# orf = "" # dealt with by removing the "" GS values
for (orf in ORFs) {
  # myrows = as.character( dictionary$ID[dictionary$ORF==orf] )
  myrows = as.character( dictionary$ID[dictionary$"Gene Symbol"==orf] )
  if (length(myrows) > 1) {
    print (orf)
    multipleProbedORFs = c(multipleProbedORFs, orf) # add to the list of all the orf with multiples probes
    ex[myrows[1], ] = apply(ex[myrows,], 2, mean) # put the mean in the cell of col as orf and line of first probe in list of probes
    ex3[orf, ] = ex[myrows[1], ] # keep value of first line (ie the mean of probes)
  }else {
    ex3[orf, ] = ex[myrows[1], ] # keep value of only existing probe
  }
}
multipleProbedORFs = multipleProbedORFs[-1]


# #=======>part not needed because values have already been normalized
# # R02 and R04 are GC-RMA normalised log2 values, MDA is log2 transformed and scaled to a ref distributionof 1322 BC specific genes
# ######
# #normalization of expression data between experiments
# # each colum is a seprate experiment
# colSums = apply(ex3, 2, sum)  #get total intensity of each experiment
# colSums/1E6
# ex3norm = ex3  #just generate a template
# for( col in 1:length(ex3[1,])) { #go over each column
#   ex3norm[,col] = ex3[,col] * max(colSums) / sum(ex3[,col])
#   #    individual signals * maxExperimentTotal / Total Signal of the current experiment
# }
# apply(ex3norm, 2, sum) / max(colSums)
# ex3 = ex3norm 
# #=======>

#########
# now, have a look at the signals
#=======> not needed forthe 3 cohorts
# we often to log2 transform microarray signals
hist(ex3[,1], br=100) # br is for the number of breaks between hist cells
ex4 = log2(ex3)
hist(ex4[,3])
ex4[ex4<0] = NA #remove backgrounds
#=======>


#############
#calculate coefficient of variation
myVar = apply( ex4, 1, FUN=function(x){var(x, na.rm=T)})
myStddev = sqrt(myVar)
myMean = apply( ex4, 1, FUN=function(x){mean(x, na.rm=T)})
myCV = myStddev / myMean
myarray= data.frame(cbind( myStddev, myMean, myCV))
myarray$ORF = ORFs
myarray = myarray[, c(4, 1:3)]
summary(myarray)

outfilename = paste(myGSE, "_log2CV.csv", sep='')
write.csv(myarray, outfilename, row.names=F)
test = read.csv( outfilename, colClasses = c('character', NA, NA, NA))
str(test)
hist(test$myCV, br=100)
hist(test$myStddev, br=100)
hist(test$myMean, br=100)



#############source of nice hist : https://www.r-graph-gallery.com/histogram_several_group.html
# Libraries
library(tidyverse)
library(hrbrthemes)
library(viridis)
library(forcats)

# Load dataset from github
data <- read.table("https://raw.githubusercontent.com/zonination/perceptions/master/probly.csv", header=TRUE, sep=",")
data <- data %>%
  gather(key="text", value="value") %>%
  mutate(text = gsub("\\.", " ",text)) %>%
  mutate(value = round(as.numeric(value),0))

# plot
p <- data %>%
  mutate(text = fct_reorder(text, value)) %>%
  ggplot( aes(x=value, color=text, fill=text)) +
  geom_histogram(alpha=0.6, binwidth = 5) +
  scale_fill_viridis(discrete=TRUE) +
  scale_color_viridis(discrete=TRUE) +
  theme_ipsum() +
  theme(
    legend.position="none",
    panel.spacing = unit(0.1, "lines"),
    strip.text.x = element_text(size = 8)
  ) +
  xlab("") +
  ylab("Assigned Probability (%)") +
  facet_wrap(~text)




# # non used drawings because not fitting the threshold
# curve(dnorm(x, mean = Mean1, sd = SD1), add=TRUE, lty=2,col = "green") # add the curve of mode 1
# curve(dnorm(x, mean = Mean2, sd = SD2), add=TRUE, lty=2,col = "coral4") # add the curve of mode 2

# #----R scrpt for dashes
# generateRLineTypes<-function(){
#   oldPar<-par()
#   par(font=2, mar=c(0,0,0,0))
#   plot(1, pch="", ylim=c(0,6), xlim=c(0,0.7),  axes=FALSE,xlab="", ylab="")
#   for(i in 0:6) lines(c(0.3,0.7), c(i,i), lty=i, lwd=3)
#   text(rep(0.1,6), 0:6, labels=c("0.'blank'", "1.'solid'", "2.'dashed'", "3.'dotted'",
#                                  "4.'dotdash'", "5.'longdash'", "6.'twodash'"))
#   par(mar=oldPar$mar,font=oldPar$font )
# }
# generateRLineTypes()

# source of nice histograms and figures (https://pages.mtu.edu/~shanem/psy5220/daily/Day18/modelbasedclustering.html)


# #=================================test of mclust 1
# # source : https://www.youtube.com/watch?v=6OtFwdcRp7k&list=WL&index=2
# set.seed(12345)
# x=c(rnorm(100,0,0.5), rnorm(200,3,1))
# y = c(rep(0,100), rep(1,200))
# library(lattice)
# densityplot(~x|as.factor(y), layout=c(1,2), n=200, width=1.5)
# 
# # show a binomdal plot 
# densityplot(x, 200, width = 1.5) # xlab, lim, ylim options see hist in others scripts 


