% script
script
close all
trajetoria = (12/limiteMapa)*listaInversaPosicao(end:-1:1,:);
trajetoria = [trajetoria(:,1)-6,-trajetoria(:,2)]
deltaX = -0.9637;
deltaY = 7.0949
trajetoria = [trajetoria(:,1)+deltaX,trajetoria(:,2)+deltaY]


name = ['C:\myCodes\Python\Tutorials\Classes\trajetoria.csv']
csvwrite(name,trajetoria) 


% clearvars -except trajetoria
q0 = [trajetoria(1,:),0]';
Ts = 0.01;
limiteVelocidade = 1;%Rad/s
qk = q0;
refXY = trajetoria(2,:)';
q = [];
Kxy =0.01*[1;1];
Kphi = 1*[1;-1];
figure()
hold on


q = [q,q0];
for i=1:size(trajetoria,1)
   refXY = trajetoria(i,:)';
   t=0;
while any(( abs(qk(1:2)-refXY)>0.05))
   t=t+1;
   q = [q,qk];
   [mod,ang] = erroCart2pol(qk,refXY);
   esforco = mod*Kxy + ang*Kphi;
   esforco = saturarSinal(esforco,limiteVelocidade);
   sol = ode45(@(t,q) DDMRkinematic(t,q,esforco),[0, Ts],qk);
   qk = sol.y(:,end);
   if t>10000
      break;
   end
end
plot(q(1,end),q(2,end),'xr')
end
% 
% trajetoriaPolinomial = fastLagrangePoli(trajetoria(:,2),trajetoria(:,1),2)


plot(q(1,:),q(2,:),'--b')
%plot(trajetoria(:,1),trajetoria(:,2),'-bo')
xlim([-6, 6])
ylim([-6,6])