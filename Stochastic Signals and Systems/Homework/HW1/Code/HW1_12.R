# Input values
pe <- 0.15 #probability of defect

# tests given part is defective
te  <- c(0.80, 0.64, 0.86, 0.80, 0.74, 0.76, 0.77, 0.84, 0.85, 0.75) #prob of positive test given disease

#tests given part is non-defective
tec <- c(0.20, 0.16, 0.07, 0.09, 0.18, 0.13, 0.17, 0.14, 0.21, 0.08) #prob of positive tests given no disease

#test results 
n <- 10
test_i   <- c(1,0,1,0,1,1,1,0,0,1) 
test_ii  <- c(1,1,1,0,0,1,0,0,0,0) 
test_iii <- c(0,0,0,1,1,0,1,1,1,1)

# returns a vector of probabilities
probv <- function(test){
  pr <- rep(NA, n+1)
  pr[1] <- pe
  for (i in (1:n)){
    if (test[i]==1){p=te[i]; q=tec[i]}
    if (test[i]==0){p=1-te[i]; q=1-tec[i]}
    pr[i+1]=(pr[i]*p)/(pr[i]*p+(1-pr[i])*q)
  }
  return(pr) 
}

# test results for part (a)
probv(test_i)
probv(test_ii)
probv(test_iii)


# Simulating a matrix of test results given defected
seq1 <- matrix(NA, nrow=50000, ncol=n)
for (j in (1:n)){
  seq1[,j] <- rbinom(50000,1,te[j])}

#Calculate the probability estimate
prob1 <- apply(seq1, MARGIN=1, probv)
alpha <- 0.5 # this is a treshold we set

#The fraction of wrongly not given treatment
frac1 <- sum(prob1<=alpha)/ length(prob1) 
frac1 


#Simulating test results given not defective
seq2 <- matrix(NA, nrow=50000, ncol=n)
for (j in (1:n)){
  seq2[,j] <- rbinom(50000,1,tec[j])
}
#Calculate the probability estimate
prob2 <- apply(seq2, MARGIN=1, probv)

#Fraction of those wrongly given treatment
frac2 <- sum(prob2>=alpha)/ length(prob2)
frac2 



# Error probabilities for different cutoffs
alpha <- seq(from=0.00, to=0.99, by=0.01)
Total <- rep(NA, length(alpha))
for (k in (1:length(alpha))){
  frac1 <- sum(prob1<=alpha[k])/ length(prob1)
  frac2 <- sum(prob2>=alpha[k])/ length(prob2)
  
  fnd <- frac2
  fd  <- frac1

  #fnd -- wrongly rejected P(E|non defective)  / wrongly positive
  #fd  -- wrongly approved P(E|defective)      / wrongly negative
  
  Total[k] <- fnd*0.85 + fd*0.15
  
  # print so I can put it into LaTeX
  message(sprintf("%s & %s \\\\", alpha[k], Total[k]))
}

# minimum possibility of error
min(Total)

# simulation number with minimum error
match(c(min(Total)), Total)

# plot all values
plot(Total,type = "b")
