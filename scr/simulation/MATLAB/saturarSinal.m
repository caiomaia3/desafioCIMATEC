function esforco = saturarSinal(esforco,limiteVelocidade)
   for i=1:length(esforco)
      saturado = abs(abs(esforco(i))-abs(limiteVelocidade))>limiteVelocidade;
      if saturado
         esforco(i) = sign(esforco(i))*limiteVelocidade;
      end
   end
end