clear
close all

imagem = imread('pioneer3dx_desafioBMP2.bmp');
limiteMapa = 30;
graf = graficoRobot(imagem,limiteMapa);
close all
graf = graf.plotarImagem();
vermelho = [0.9,0,0];
azul = [0,0,0.9];
verde = [0,0.9,0];

xx = ceil(limiteMapa/5);
yy = ceil(limiteMapa-limiteMapa/10);
posicaoInicial = [xx,yy];
estadoInicial.x =xx;
estadoInicial.y = yy;
estadoAtual = estadoInicial;
xxx = ceil(22*limiteMapa/30);
posicaoFinal = [xxx,yy];
estadoFinal.x = posicaoFinal(1);
estadoFinal.y = posicaoFinal(2);

mapaRestricao = ~graf.Mapa;
[listaAberta,listaFechada,mapaExplorado] = inicializarProblema(posicaoInicial,posicaoFinal,~graf.Mapa);
quadrado = graf.plotarQuadrado(estadoFinal,vermelho);
robo = graf.plotarQuadrado(estadoAtual,azul);
for i=1:length(listaAberta)
   estadoExplorado = posicao2estado(listaAberta(i).posicao);
   explorado = graf.plotarQuadrado(estadoExplorado,verde);
   explorado.AlphaData = 0.2;
end
%explorado.AlphaData = 0.2;
no = listaFechada;
while any(no.posicao ~= posicaoFinal)
   no = selecionarAdjacente(listaAberta);
   robo.XData = no.posicao(1);
   robo.YData = no.posicao(2);
   [listaAberta,listaFechada,mapaExplorado] = explorarAdjacencia(no,listaAberta,listaFechada,mapaRestricao,mapaExplorado,posicaoFinal);
%    pause(0.1)
end

for i=1:(length(listaFechada)-1)
   estadoExplorado = posicao2estado(listaFechada(i).posicao);
   explorado = graf.plotarQuadrado(estadoExplorado,azul);
   explorado.AlphaData = 0.2;
end
listaInversa = [];
listaFechadaPosicao = [];
for i=1:length(listaFechada)
   listaFechadaPosicao = [listaFechadaPosicao;listaFechada(i).posicao];
end
listaInversaPosicao = [];
while any(no.posicao ~= posicaoInicial)
   listaInversa = [listaInversa,no];
   index = find(all((no.pai==listaFechadaPosicao)'));
   no = listaFechada(index);
   listaInversaPosicao = [listaInversaPosicao;no.posicao];
end
for i=2:(length(listaInversa))
   estadoExplorado = posicao2estado(listaInversa(i).posicao);
   explorado = graf.plotarQuadrado(estadoExplorado,vermelho);
   explorado.AlphaData = 0.5;
end


