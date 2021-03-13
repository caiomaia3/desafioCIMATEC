%fast lagrange interpolation
function xInterpolado = fastLagrangePoli(xData,raizes,t)
   dimensao_t = length(t);
   xInterpolado = zeros(size(t));

   for k = 1:dimensao_t
   ordem = length(raizes);

      for indice=1:ordem
         xInterpolado(k) = xInterpolado(k)  + xData(indice)*baseLagrange(raizes,indice,ordem,t(k));
      end
   end

   function l = baseLagrange(raizes,indice,ordem,tau)
      l=1;
      for ii=1:ordem
         if ii~=indice
            l = l*(tau-raizes(ii)) / (raizes(indice) - raizes(ii));
         end
      end
   end
end
