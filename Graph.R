library(tidyverse)

data = read.csv("output.csv")

ggplot(data = data, aes(x= Stop_min, y = Time_Elapsed_min)) + geom_col()
