# plot the functions y1 and y2 from 0-0.4
x  <- seq(0, 0.4, 0.001)
y1 <- (x)^2
y2 <- (x)^4 + 4*(1-(x))*(x)^3

plot(x,y1,type="l",col="red")
lines(x,y2,col="blue", lwd=3)
lines(x,y1,col="red", lwd=3)
