function [listaAberta,listaFechada,mapaExplorado] = explorarAdjacencia(no,listaAberta,listaFechada,mapaRestricao,mapaExplorado,posicaoFinal)
%Explora adjacencia e inclui nos vizinho admissiveis na regiao de busca.
[listaAberta,listaFechada] = retirarNo(no,listaAberta,listaFechada);
posicaoMatricial = no.posicao(end:-1:1);
for i=-1:1
   for j=-1:1
      posicaoTeste = posicaoMatricial + [i,j];
      eExplorado = mapaExplorado(posicaoTeste(1),posicaoTeste(2));
      eAdmissivel = ~mapaRestricao(posicaoTeste(1),posicaoTeste(2));
      if ~eExplorado && eAdmissivel
         posicaoIncluida = posicaoTeste(end:-1:1);
         noPai = no;
         listaAberta = incluirNo(posicaoIncluida,posicaoFinal,listaAberta,noPai);
         mapaExplorado(posicaoTeste(1),posicaoTeste(2)) = true;
      end
   end
end
end