classdef graficoRobot
   properties
      Mapa
      Imagem
      ImagemHandle
   end
   methods
      function obj = graficoRobot(imagem,limiteMapa)
         mapaBinary = imbinarize(imagem);
         tamanhoImagem = size(imagem,1);
         mapaMenor = imresize(mapaBinary,limiteMapa/tamanhoImagem);
         mapa = mapaMenor(:,:,1);
         obj.Imagem = mapaMenor;
         obj.ImagemHandle = image(mapaMenor);
         obj.Mapa = mapa;
      end
      function this = plotarImagem(this)
         this.ImagemHandle = image(this.Imagem);
      end 
   end
   methods (Static)
      function quadrado = plotarQuadrado(estado,corRGB)
        [x,y] = estado2posicao(estado);
         C = zeros(1,1,3);
         for i=1:3
            C(:,:,i) = corRGB(i);
         end
         hold on
         quadrado = image(x,y,C);
      end
   end
   
end
