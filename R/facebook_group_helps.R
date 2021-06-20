## R studio facebook group question helps
## 2021-06-15

temp = data.frame(A=c(6,4,1,5), B=c(4,3,5,1), C=c(1,2,9,6))
## base R one liner (specifiy column index if needed)
temp$col1 = names(temp)[c(1:ncol(temp))][apply(temp, MARGIN=1, FUN=which.max)]
