clear;
clc;
% initial concentration
E0 = 1;
S0 = 10;
ES0 = 0;
P0 = 0;
y0 = [E0;S0;ES0;P0];
h=1e-7; 
tspan = 0.1;
digits(8);
[t,y] = RK4(@odefun, y0, h, tspan);
p = y(4,:);
s = y(2,:);
% Given p a derivative to get v
V = zeros(1,length(p)-1);
for i =1:length(p)-1
    V(:,i) = (p(i+1)-p(i))/(t(i+1)-t(i));
end
t1 = t(2:end);
s = s(2:end);
format long

plot(s,V,'b','LineWidth',1)
title('Plot between S and V')
xlabel('the concentration of the substrate S (µM)');
ylabel('the velocity V (µM/min)');
%method 1
% directly find the maximum from V
Vm1 = max(V);
% Vm1 = 82.647865702941047
%method 2
% find the index of the value closest to 0 in dV
dV = zeros(1,length(V)-1);
for i =1:length(V)-1
    dV(:,i) = (V(i+1)-V(i))/(t1(i+1)-t1(i));
end
t2 = t1(2:end);
Vm2 =V(find(dV<0,1));
% Vm2 = 82.647865702941047
% we can see Vm1 = Vm2, the two different methods get the same result
