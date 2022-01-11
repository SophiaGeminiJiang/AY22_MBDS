clear all;
clc;
%% initial condition
E0 = 1;
S0 = 10;
ES0 = 0;
P0 = 0;
y0 = [E0,S0,ES0,P0];
h=0.01; 
tspan = 0.5
[t,y] = RK4(@odefun, y0, h, tspan);
