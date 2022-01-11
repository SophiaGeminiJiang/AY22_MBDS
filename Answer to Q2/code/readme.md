### 1. write down the four equations
According to the law of mass action, and the formula given in the stem, we can write the equations of the rate fo changes of the four species, shown as the equations in 'odefun.m'
y(1) refers to the concentration of E; y(2) refers to the concentration of S; y(3) refers to the concentration of ES; y(4) refers to the concentration of P.

### 2. write a code to numerically solve these equations
With the initial concentrations given in the stem and with the use of the fourth-order Runge-Kutta method, we can numerically solve this function. In our code 'main.m', the result is stored in the variable 'y'

### 3. plot the relationship between the value of the rate of the change of the product P, V, and the concentraion of S, find the maximum of V
The required plot has been save as 'Plot between S and V.jpg', and the maximum of Vm is 82.647865702941047 um/min, the process of calculating is shown in the code
