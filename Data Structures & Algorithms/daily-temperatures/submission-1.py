class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        listaRetorno = []
        tam = len(temperatures)


        for i in range(tam):

            colocado = 0

            for j in range(i + 1, tam):

                if temperatures[j] > temperatures[i]:
                    listaRetorno.append(j - i)
                    colocado = 1
                    break
                
            if colocado == 0:
                listaRetorno.append(0)

        return listaRetorno