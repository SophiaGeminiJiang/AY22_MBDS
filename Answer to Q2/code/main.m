clear;
% initial condition
y0 = [1,10,0,0];
tspan = [0 0.5]; 
[t,y] = ode45(@odefun, tspan, y0);
p = y(:,4);

for i =1:length(p)-1
    V(i,:) = (p(i+1)-p(i))/(t(i+1)-t(i));
end
t1 = t(2:end);

plot(t1,V)
% plot(t2,dV)
Vm = max(V);