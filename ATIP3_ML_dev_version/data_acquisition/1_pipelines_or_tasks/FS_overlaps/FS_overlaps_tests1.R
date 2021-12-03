# this is a script to start testing the upset plots
# - introduced by this github page : https://github.com/hms-dbmi/UpSetR
# links are in it to know more about the manipulations possiblepset plots : 
# https://jku-vds-lab.at/tools/upset/#:~:text=UpSet%20concept,the%20figure%20on%20the%20right.&text=The%20first%20row%20in%20the,B%20or%20C)%2C%20etc.
# Upset plots website to do interactive plots : https://vcg.github.io/upset/
# hacking through upset plots : https://www.r-bloggers.com/2018/07/hacking-our-way-through-upsetr/
library(UpSetR)

#========== Basic usage (https://cran.r-project.org/web/packages/UpSetR/vignettes/basic.usage.html)
movies <- read.csv(system.file("extdata", "movies.csv", package = "UpSetR"), header = T, sep = ";")
# a quick example of basic things to modify
# - Plot Formatting (Displays only the intersections made with the top Largest Sets only with nsets ...)
upset(movies, nsets = 6, number.angles = 30, point.size = 3.5, line.size = 2, 
      mainbar.y.label = "Genre Intersections", sets.x.label = "Movies Per Genre", 
      text.scale = c(1.3, 1.3, 1, 1, 2, 0.75))

# Choosing Specific Sets and Matrix Ordering
# - mb.ratio is x, y with x and y respectively the proportion in the vertical length taken by the 2 parts of the plot
# -If no order is specified, the matrix will be ordered by degree, then frequency. so we choose freq as ordering 
upset(movies, sets = c("Action", "Adventure", "Comedy", "Drama", "Mystery", 
                       "Thriller", "Romance", "War", "Western"), mb.ratio = c(0.55, 0.45), order.by = "freq")

# keep the sets in the order entered using the sets parameter (Example 3), set the keep.order parameter to TRUE.
upset(movies, sets = c("Action", "Adventure", "Comedy", "Drama", "Mystery", 
                       "Thriller", "Romance", "War", "Western"), mb.ratio = c(0.55, 0.45), order.by = "freq", 
      keep.order = TRUE)

# show empty intersections turn on empty.intersections
upset(movies, empty.intersections = "on", order.by = "freq")

#====> best proposition : 
upset(movies, sets = c("Action", "Adventure", "Comedy", "Drama", "Mystery", 
                       "Thriller", "Romance", "War", "Western"), number.angles = 30, point.size = 3.5, line.size = 2, 
      mainbar.y.label = "Genre Intersections", sets.x.label = "Movies Per Genre", 
      text.scale = c(1.3, 1.3, 1, 1, 2, 0.75),mb.ratio = c(0.55, 0.45), 
      order.by = "freq", keep.order = TRUE, empty.intersections = "on")

# text.scale can either take a universal scale in the form of an integer, or a vector of specific scales in the format:
# c(
# intersection size title, 
# intersection size tick labels, 
# set size title, 
# set size tick labels, 
# set names, 
# numbers above bars)

#==========Querying the Data (https://cran.r-project.org/web/packages/UpSetR/vignettes/queries.html)

# 1) use the built in intersection query "intersects" to find or display elements in specific intersections
# an upset is done but queries add answers on it 
# active = F puts an arrow on the bar when the query has an answer  
# active = T colors the whole bar when the query has an answer
upset(movies, queries = list(list(query = intersects, params = list("Drama", "Comedy", "Action"), color = "orange", active = T), 
                             list(query = intersects, params = list("Drama"), color = "red", active = F), 
                             list(query = intersects, params = list("Action", "Drama"), active = T)))


# 2) use the built in intersection query "elements" to represent how much certain values are present in an intersection
# an upset is done but queries add answers on it 
# active = F puts an arrow on the bar when the query has an answer (top of the arrow is the amount...not preferred      )
# active = T colors the whole bar when the query has an answer (preferable)
upset(movies, queries = list(list(query = elements, params = list("AvgRating",3.5, 4.1), color = "blue", active = T), 
                             list(query = elements, params = list("ReleaseDate",1980, 1990, 2000), color = "red", active = F)))

# 3) use the expression parameter to Subset Intersection and Element Queries 
# - in order to highlight only when responding to an additionnal condition
upset(movies, queries = list(list(query = intersects, params = list("Action", "Drama"), active = T), 
                             list(query = elements, params = list("ReleaseDate", 1980, 1990, 2000), color = "red", active = F)), 
      expression = "AvgRating > 3 & Watches > 100")

# 4)  - in order to highlight when responding to mutiple additionnal condittions
#  (for that we do create Custom Queries on Set Elements and Attributes (selected rows of the data to operate on)
# NB : its does not color the intersections bullets points lines because its not about the intersection or its subgroups 
# but its about a part of the attributes that those carries with them

# step 1 : Creating a custom query to operate on the rows of the data.
Myfunc <- function(row, release, rating) {
   data <- (row["ReleaseDate"] %in% release) & (row["AvgRating"] > rating)
}
# step 2 : Applying the created query to the queries parameter.
upset(movies, queries = list(list(query = Myfunc, params = list(c(1970, 1980, 1990, 1999, 2000), 2.5), color = "blue", active = T)))



# 5) Applying a legend to a whole upset figure : 
# To add a legend for the queries applied, the query.legend parameter can be used. 
# The query.legend parameter takes the position where the legend should be displayed, either top or bottom. 
# To apply a specific name to each query, the parameter query.name can be used when defining the query in the queries paramter. 
# If no query.name is provided, a generic name will be used. The example below shows how to do this.
upset(movies, query.legend = "top", queries = list(list(query = intersects, params = list("Drama", "Comedy", "Action"), color = "orange", active = T, query.name = "Funny action"), 
                                                   list(query = intersects, params = list("Drama"),color = "red", active = F), 
                                                   list(query = intersects, params = list("Action", "Drama"), active = T, query.name = "Emotional action")))


# 6) Combining pieces from all previous examples into one awesome query!
upset(movies, query.legend = "bottom", queries = list(list(query = Myfunc, params = list(c(1970, 1980, 1990, 1999, 2000), 2.5), color = "orange", active = T), 
                                                      list(query = intersects, params = list("Action", "Drama"), active = F), 
                                                      list(query = elements, params = list("ReleaseDate",1980, 1990, 2000), color = "red", active = F, query.name = "Decades")), 
      expression = "AvgRating > 3 & Watches > 100")


   
#==========Attribute Plots (https://cran.r-project.org/web/packages/UpSetR/vignettes/attribute.plots.html)
# NB : for attributes plots, its really usefull when additionnal columnal with continuous values describe the elements of the intersections
# and that we want to represent the distribution of those values for all the elements of the groups making the intersections
# Issue one : we woul really like that to be possible for each intersection and as one amount for a considered variable describing elements of the intersection
# That can be maybe done with the last examples giving boxplots for each intersection but the elements to represent are so much that there will be a lot of boxplots stacked up
#  Solution : see on the side of incorporing set metadata or see the histogramms that Chloé proposed (some of them have values as x and a list of variables as y  )

#==========Incorporating Set Metadata   (https://cran.r-project.org/web/packages/UpSetR/vignettes/set.metadata.plots.html)
# this part shows how to add to the groups of that have been intersected, a mark for the quality it have in a certain catgorical sample 
# (eg: the city where the genre of movies is from)
# and its different from what we are looking for : for each intersection, we need horizontal bars extending, one bars being one categorical value for a intersection
# we can do that with Chloé histograms link for intersections sizes as histogramms



#===========> Sources for building attributes content 1 
# - if we have to add the (the gene bio type ie gene type)
# source 1 : https://www.r-bloggers.com/2015/11/annotables-r-data-package-for-annotatingconverting-gene-ids/
# source 1 as a github : https://github.com/stephenturner/annotables

# - if we have to add the content of some sort of analysis enrichment 
# source of the enrichment at the end of maEndtoEnd pipeline in bioconductor : 
# https://bioconductor.org/packages/release/workflows/vignettes/maEndToEnd/inst/doc/MA-Workflow.html#13_Gene_ontology_(GO)_based_enrichment_analysis
# source of bioincoductor annotations pipelines : https://bioconductor.org/packages/release/BiocViews.html#___AnnotationWorkflow

# an example of queries to see how to name the queries for that to appear in the queries legend 
upset(movies, 
      query.legend = "bottom", 
      queries = list(list(query = Myfunc, params = list(c(1970, 1980, 1990, 1999, 2000), 2.5), color = "orange", active = T),
                     list(query = intersects, params = list("Action", "Drama"), active = F),
                     list(query = elements, params = list("ReleaseDate", 1980, 1990, 2000), color = "red", active = F, query.name = "Decades")), 
      expression = "AvgRating > 3 & Watches > 100")


# this is the example for all metadata at once in incorporating meta data of the movies dt...
upset(movies, 
      set.metadata = list(data = metadata, 
                          plots = list(list(type = "hist", column = "avgRottenTomatoesScore", assign = 20), 
                                       list(type = "bool", column = "accepted", assign = 5, colors = c("#FF3333", "#006400")), 
                                       list(type = "text", column = "Cities", assign = 5, colors = c(Boston = "green", NYC = "navy", LA = "purple")),
                                       list(type = "matrix_rows", column = "Cities", colors = c(Boston = "green", NYC = "navy", LA = "purple"), alpha = 0.5))), 
      queries = list(list(query = intersects, params = list("Drama"), color = "red", active = F), 
                     list(query = intersects, params = list("Action", "Drama"), active = T), 
                     list(query = intersects, params = list("Drama", "Comedy", "Action"), color = "orange", active = T)), 
      attribute.plots = list(gridrows = 45, plots = list(list(plot = scatter_plot, x = "ReleaseDate", y = "AvgRating", queries = T), 
                                                         list(plot = scatter_plot, x = "AvgRating", y = "Watches", queries = F)), 
                             ncols = 2), 
      query.legend = "bottom")

# another example of upsetplots where every intersection implcating a set can be all colored the same color
upset(movies, 
      sets=c("Action", "Adventure", "Comedy", "Drama", "Mystery", 
             "Thriller", "Romance", "War", "Western"), 
      keep.order=T, 
      order.by = "freq",
      queries = list(list(query = function(row, value){ data <- (row["Drama"] == value)}, color="blue", params = list(1), active = T),
                     list(query = function(row, value){ data <- (row["Action"] == value)}, color="orange", params = list(1), active = T),
                     list(query = function(row, date){data <- (row["ReleaseDate"] %in% date)}, params = list(1995), color = "red", active = T)
                     )
      )

# from below source, we see that sizes can be added on top of set size bar hist
# source : https://stackoverflow.com/questions/55788414/upsetr-add-numeric-labels-to-set-size-on-plot
# before 
test <- upset(grouped_hot,
              sets                = c("A", "B", "C", "N"),
              nintersects         = 8,
              mb.ratio            = c(0.6, 0.4),
              sets.x.label        = "Number of Patients",
              sets.bar.color      =  "#56B4E9",
              mainbar.y.label     = "Number of Patients",
              order.by            = "freq",
              empty.intersections = "on",
              keep.order          = FALSE,
              scale.sets          = "identity",
              att.pos             = "top",
              text.scale          = c(2.5, 2.5, 2, 1.5, 2.5, 2.5))
# after
test <- upset(grouped_hot, 
              sets= c("A", "B", "C", "N"), 
              nintersects = 8, 
              mb.ratio = c(0.6, 0.4), 
              # ...
              att.pos = "top", 
              text.scale = c(2.5,2.5,2,1.5,2.5,2.5),
              set_size.show = TRUE)


