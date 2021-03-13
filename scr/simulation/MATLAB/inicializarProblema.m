function [listaAberta,listaFechada,mapaExplorado] = inicializarProblema(posicaoInicial,posicaoFinal,mapaRestricao)
   no = gerarNoInicial(posicaoInicial,posicaoFinal);
   mapaExplorado = zeros(size(mapaRestricao));
   mapaExplorado(posicaoInicial(2),posicaoInicial(1)) = true;
   listaAberta = no;
   [listaAberta,listaFechada,mapaExplorado] = explorarAdjacencia(no,listaAberta,[],mapaRestricao, ...
                                                         mapaExplorado,posicaoFinal);
end