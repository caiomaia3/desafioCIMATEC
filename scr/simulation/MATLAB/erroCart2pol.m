function [mod,ang] = erroCart2pol(qk,refXY)
erroXY = refXY - qk(1:2);
refTheta = atan2(erroXY(2),erroXY(1));
erroTheta = refTheta - qk(3);
mod = sqrt(refXY(1)^2+refXY(2)^2);
ang = erroTheta;
end
