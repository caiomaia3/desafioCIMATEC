function dq =  DDMRkinematic(t,q,dphi)
%Parameters
R = 1;
L = 1;
dq =[ R*cos(q(3))*(dphi(1)+dphi(2))/2;
R*sin(q(3))*(dphi(1)+dphi(2))/2;
 R*(dphi(1)-dphi(2))/(2*L)];
