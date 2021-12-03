# this is script to make for a dataset, the correlation matrix for its features
# Version : V1


# lets get the dataset to use



# lets do the plot 




# test step 1 (making the corr matrix)

head(mtcars)
M<-cor(mtcars)
head(round(M,2))

# test step 2 (drawing the corr matrix plot)
library(corrplot)


# -- methods de visalisation
# Sept méthodes de visualisation différentes peuvent être utilisées : 
# “circle”, “square”, “ellipse”, “number”, “shade”, “color”, “pie”
corrplot(M, method="circle")


# --Les différentes dispositions du corrélogrammes
# Il y a 3 dispositions différentes :
#   
#   “full” (par défaut) : Affiche la Matrice de corrélation en entier.
# “upper”: Affiche le triangle supérieur de la matrice de corrélation.
# “lower”: Affiche le triangle inférieur de la matrice de corrélation.
corrplot(M, type="upper")
corrplot(M, type="lower") # preférable

# -- Réordonner la matrice de corrélation
# La matrice de corrélation peut être réordonnée en fonction du coefficient 
# de corrélation. Ceci est important pour identifier des profiles cachés 
# dans la matrice. La méthode hclust (pour hierarchical clustering) est 
# utilisée dans les exemples ci-dessous.

# Corrélogramme avec rearrengement de type hclust
corrplot(M, type="upper", order="hclust")

# -- Utilisation de differents spectres de couleurs
col<- colorRampPalette(c("red", "white", "blue"))(20)
corrplot(M, type="upper", order="hclust", col=col)

# Changement de la couleur du corrélogramme
# Comme montré dans les sections ci-dessus, 
# la couleur du corrélogramme peut être personnalisée. 
# Les palettes de couleurs du package RcolorBrewer sont utilisées dans 
# le script ci-dessous :
#   
#   library(RColorBrewer)
# corrplot(M, type="upper", order="hclust", 
#          col=brewer.pal(n=8, name="RdBu"))
# also exists : name="RdYlBu", name="PuOr", 


# -- Changer la couleur de fond en lightblue
corrplot(M, type="upper", order="hclust", col=c("black", "white"),
         bg="lightblue")


# -- Changement de la couleur et de la rotation des étiquettes de textes
# tl.col (for text label color) et tl.srt (for text label string rotation) 
# sont utilisés pour changer la couleur et l’angle de rotation des textes.

corrplot(M, type="upper", order="hclust", tl.col="black", tl.srt=45)

# -- Combiner le corrélogramme avec le test de significativité
# Calcul de la p-value des corrélations
# Pour calculer la p-value des matrices, nous allons utiliser 
# une fonction personnalisée:
  
  # mat : matrice de donnée
  # ... : Arguments supplémentaire à passer à la fonction cor.test
cor.mtest <- function(mat, ...) {
  mat <- as.matrix(mat)
  n <- ncol(mat)
  p.mat<- matrix(NA, n, n)
  diag(p.mat) <- 0
  for (i in 1:(n - 1)) {
    for (j in (i + 1):n) {
      tmp <- cor.test(mat[, i], mat[, j], ...)
      p.mat[i, j] <- p.mat[j, i] <- tmp$p.value
    }
  }
  colnames(p.mat) <- rownames(p.mat) <- colnames(mat)
  p.mat
}
# Matrice de p-value de la corrélation                  
p.mat <- cor.mtest(mtcars)
head(p.mat[, 1:5])

aaa

# what we maintained
col<- colorRampPalette(c("red", "white", "blue"))(20)
corrplot(M, method="circle",type="lower",order="hclust", col=col,
         bg="darkgrey",
         tl.col="black", tl.srt=45)
# hesitations
method="color"
method="circle"


# -- final trial of the plot 
col <- colorRampPalette(c("#BB4444", "#EE9988", "#FFFFFF", "#77AADD", "#4477AA"))
corrplot(M, method="color", col=col(200),  
         type="upper", order="hclust", 
         addCoef.col = "black", # Ajout du coefficient de corrélation
         tl.col="black", tl.srt=45, #Rotation des etiquettes de textes
         # Combiner avec le niveau de significativité
         p.mat = p.mat, sig.level = 0.01, insig = "blank", 
         # Cacher les coefficients de corrélation sur la diagonale
         diag=FALSE 
)
