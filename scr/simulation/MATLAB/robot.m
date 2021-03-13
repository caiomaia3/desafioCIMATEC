classdef robot
   properties
      x
      y
   end
   methods
      function obj = robot(x0,y0)
         obj.x = x0;
         obj.y = y0;
      end
      function this = andar(this,x1,y1)
         if this.testarPosicao(x1,y1)
            this.x = x1;
            this.y = y1;
            %this.atualizarGrafico()
         end
      end 
      function posicaoValida = testarPosicao(this,x,y)
         for i=-1:1
            for j=-1:1
               xTeste
         posicaoValida = true;
      end
      function atualizarGrafico()
      end
   end
end

      