# we found out that scikit-learn, cyanure and SPAMS output  multiples labels for their brand of multitasking
# issue is : we want really one output but with the same separate treatment that multitasking offers

# we propose the following strategies :
# - Strategy 1 is a very manual strategy :
# 0- use on datasets that has the same type of values (e.g. : only datasets that have log2 values)
# 1- on the largest dataset, scale the values in each feature Fi with standardscaler()
# 2- used that scaler on the values of the feature Fi on all the others datasets (we do the same everytime we scale train_w and use it on test_x)
# 3- now features values are of the same type, and on the same scale so we can join the dataset into one big dataset
# 4-use the big dataset for one learning task (we have only one response that is pCR status)

# - Strategy 2 is based on ensembling (ref2):
# 0- the principle of ensemble methods is to make a consensus entity by using entities of the same nature
# 1-we train each dataset separatly to obtain a model
# 2-we use ensemble methods on the different models used to get a consensus model
# 3-the consensus model should use the info from all models hence is in the same spirit of using all datasets at the same time without mixing the samples from different datasets

# - Strategy 3 : use transfer learning in a gradient boosting fashion (ref1)

# References :
# ref2: Alberto Verdecia-Cabrera comment in here : https://www.researchgate.net/post/How_to_proceed_in_case_of_multiple_datasets_for_training_but_a_single_test_set
#
# ref 1 : Youcef Heraibia comment in here : https://www.researchgate.net/post/How_to_proceed_in_case_of_multiple_datasets_for_training_but_a_single_test_set


# Bonjour Chloé,
#
# merci pour cette remarque. La définition de la partie réponse est importante dans ce que l'on veut que le multitasking nous fasse.
#
# J'ai pris un peu de temps pour refléchir à la question et voici 3 propositions sur lesquelles j'aimerai ton avis :
#
# - Stratégie 1 qui peut remplacer le multitask learning :
# + l'idée : utiliser les méthodes ensemblistes qui permettent de faire un consensus d'entités de la même nature.
# + étape 1 : produire le model venant de chaque jeu de donnéés
# + étape 2 : utiliser des méthodes ensemblistes pour résumer les résultats des différents modèles en un seul modèle
# NB : j'imagine déjà que l'on pourra accorder des importances égales ou différentes à tel ou tel autre modèle selon la taille du jeu de données ou un autre critère de notre choix
#
# - Stratégie 2 qui n'est pas très "propre" mais je veux ton avis dessus car j'aimerais bien le faire en marge de la Stratégie 1 :
# + l'idée:  fabriquer un seul unique "super-jeu de données" en combinant tous les autres puis l'analyser en une tâche
# + étape 1 : s'assurer que les valeurs dans nos jeux données sont tous de la même nature (ex: tous les jeux de données ont des log2 values dans mon cas)
# + étape 2 : sur le plus grand jeu des jeux de données, faire un standardscaler() sur un feature Fi puis mettre à cette échelle le feature Fi dans tous les autres jeux de données (comme il est d'habitude fait entre train_x et test_x avant de prédire avec test_x...)
# + étape 3 :  nous nous retrouvons avec différents jeux de données contenant des valeurs de la même nature et sur une même échelle, donc nous "devrions pouvoir" joindre les jeux de données en un seul grand jeu données
# + étape 4 : utiliser le "super jeu de données" ainsi formé pour sortir un seul modèle (la réponse "pCR status" est déjà présente chez tous les échantillons donc une seule tâche et pas de multitask learning)
#
# - Stratégie 3 sur laquelle je dois encore m'informer un peu plus :
# + l'idée : le transfer learning permet de commencer des analyses "à chaud" en partant d'un modèle qui existait déjà et que l'on fournit en entrée dans l'analyse
# + étape 1 : commencer une tâche mais avec le plus gros jeu de données: aappelons model_i le modèle ainsi produit
# + étape 2 : faire une tâche avec le modèle le plus grand parmi ceux non encore utilisés, en introduisant le modèle précédemment obtenu (model_i) pour le modifier selon des critères (un certain seuil d'infos atteint par ex). répéter cette opération jusqu'à épuisement de nos jeux de données.
# + Nous pouvons ainsi "améliorer ou pas" le modèle initial comme le principe de Gradient Boosting de XGBoost et on se retrouve en fin d'analyse avec un modèle ayant tiré parti "si cela est possible" de tous les jeux de données à notre disposition.
#
# Chloé, en attendant ton avis, je pense commencer à préparer les sorties pour chaque jeu de données car pour la comparaison avec le multitask comme pour les méthodes ensemblistes nous en avons besoin, en plus c'est un début de base de discussion de ce qui ressort.
#
# Merci.
# Amad.