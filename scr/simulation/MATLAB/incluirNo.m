function listaAberta = incluirNo(posicao,posicaoFinal,listaAberta,pai)
   G =@(x,y) ceil(10*sqrt(sqrt((x - y )*(x - y)')));
   no.posicao = posicao;
   no.pai = pai.posicao;
   no.g = pai.g + G(posicao,pai.posicao);
   no.h = 10*(posicao - posicaoFinal)*(posicao - posicaoFinal)';
   no.f = no.g + no.h;
   listaAberta = [listaAberta,no];
end