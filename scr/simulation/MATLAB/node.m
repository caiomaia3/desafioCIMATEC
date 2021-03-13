classdef node
   properties
      Posicao
      Pai
      F
      G
      H
   end
   methods
      function obj = node(estadoAtual,estadoFinal,pai)
         if nargin > 2
            obj.Pai = pai;
            
         else
            obj.G = 0;
         end
         obj.H = heristica(estadoAtual,estadoFinal);
         obj.F = obj.H
         obj.PosicaoGrafica = estadoAtual;
         end
      end
      function h = heristica(estadoAtual,estadoFinal)
         aux = estado2posicao(estadoAtual) - estado2posicao(estadoFinal);
      end
         
   end
end
