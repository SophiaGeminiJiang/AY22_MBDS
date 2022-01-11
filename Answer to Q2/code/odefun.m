function dydt = odefun(~,y)
k1 = 100;
k2 = 600;
k3 = 150;
dydt = zeros(4,1);
dydt(1) = k2*y(3)+k3*y(3)-k1*y(1)*y(2);
dydt(2) = k2*y(3)-k1*y(1)*y(2);
dydt(3) = k1*y(1)*y(2)- k2*y(3)-k3*y(3);
dydt(4) = k3*y(3);
end

