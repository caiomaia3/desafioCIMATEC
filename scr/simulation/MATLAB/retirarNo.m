function [listaAberta,listaFechada] = retirarNo(no,listaAberta,listaFechada)
listaFechada = [listaFechada,no];
posicao = no.posicao;
for i=1:length(listaAberta)
   noExistente = all(listaAberta(i).posicao==posicao);
   if noExistente
      if length(listaAberta(1:i))>1
         anterior = listaAberta(1:(i-1));
      else
         anterior = [];
      end
      if length(listaAberta(i:end))>1
         posterior = listaAberta((i+1):end);
      else
         posterior = [];
      end
      listaAberta = [anterior,posterior];
      break
   end
end

end