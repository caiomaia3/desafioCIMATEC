function minNo = minimizarCusto(listaAberta)
N = length(listaAberta);
ff = zeros(1,N);
for i=1:length(listaAberta)
   ff(i) = listaAberta(i).f;
end
[~,minIndex] = min(ff);
minNo = listaAberta(minIndex);
end