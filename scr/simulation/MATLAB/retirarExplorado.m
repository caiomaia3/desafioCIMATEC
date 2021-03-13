function m = retirarExplorado(estado,mapa)
[x,y] = estado2posicao(estado);
mapa(y,x) = false;
m=mapa;
end