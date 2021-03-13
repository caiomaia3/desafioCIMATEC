function no = gerarNoInicial(posicao,posicaoFinal)
   no.posicao = posicao;
   no.pai = 0;
   no.g = 0;
   no.h = (posicao - posicaoFinal)*(posicao - posicaoFinal)';
   no.f = no.g + no.h;
end