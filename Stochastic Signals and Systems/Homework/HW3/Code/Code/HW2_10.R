u <- runif(1000)
Fx <- 1-(1/u)^5
fx <- 1/(1-u)^(1/5)

hist(Fx)
#hist(fx)

f=function(n, a=0.5, b=1) qpareto(runif(n),a,b)
