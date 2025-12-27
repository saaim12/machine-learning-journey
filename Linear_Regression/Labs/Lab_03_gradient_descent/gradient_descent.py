## this code is for gradient descent in action
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0, 10, 10)
y=np.linspace(0, 10, 10)

print("__"*50)
#showing y and x on graph
plt.scatter(x, y, color='blue', label='Data points')
plt.xlabel("houses Size")
plt.ylabel("houses Price")
plt.title("Data points")
#plt.show()

# showing slope of cost function initially
def compute_cost(x,y,w,b,m):
    total_cost=0
    for i in range(m):
        error=(y[i]-(w*x[i]+b))**2
        total_cost+=error
    return total_cost/(2*m)
m=len(x)
w=0
b=0
cost=compute_cost(x,y,w,b,m)
print("Initial Cost at w =",w,", b =",b,"is",cost)
# plotting initial line
y_pred=w*x+b
plt.scatter(x, y, color='blue', label='Data points')
plt.plot(x,y_pred,color="yellow",label="Initial Model line")
plt.legend(loc='upper left')  # position
plt.legend(fontsize=5)
plt.legend("Line for Initial w and b")
plt.show()

# Gradient Descent Function
def gradient_descent(x,y,w,b,m,iterations,lr):
    cost_history=[]
    for it in range(iterations):
        dw,db=0,0
        for i in range(m):
            f_wb=w*x[i]+b
            dw+=-(2/m)*(x[i]*(y[i]-f_wb))
            db+=-(2/m)*(y[i]-f_wb)
        w=w-lr*dw
        b=b-lr*db
        cost=compute_cost(x,y,w,b,m)
        cost_history.append(cost)
    return w,b,cost_history
# Running Gradient Descent
iterations=1000
lr=0.01
w,b,cost_history=gradient_descent(x,y,w,b,m,iterations,lr)
print("Final Cost at w =",w,", b =",b,"is",cost_history[-1])
# plotting final line
y_pred=w*x+b
plt.scatter(x, y, color='blue', label='Data points')
plt.plot(x,y_pred,color="red",label="Final Model line after GD")
plt.legend(loc='upper left')  # position
plt.legend(fontsize=5)
plt.legend("Line for Final w and b after GD")
## cost graph
plt.figure()
plt.plot(range(iterations),cost_history,color="green")
plt.xlabel("Iterations")
plt.ylabel("Cost")
plt.title("Cost vs Iterations")
plt.show()
