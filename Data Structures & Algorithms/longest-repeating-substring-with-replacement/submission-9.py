class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        maiortamesq = 0
        maiortamdir = 0
        tamvet = len(s)

        for i in range(tamvet):

            carac = s[i]
            cont = 1
            buffer = k

            for j in range(i + 1, tamvet):

                if s[j] == carac:
                    cont += 1
                else:
                    if buffer > 0:
                        buffer -= 1
                        cont += 1
                    else:
                        break
            
            if cont > maiortamesq:
                maiortamesq = cont

        for i in range(tamvet):

            carac = s[tamvet - i - 1]
            cont = 1
            buffer = k

            for j in range(i + 1, tamvet):

                if s[tamvet - j - 1] == carac:
                    cont += 1
                else:
                    if buffer > 0:
                        buffer -= 1
                        cont += 1
                    else:
                        break
            
            if cont > maiortamdir:
                maiortamdir = cont

        if maiortamdir == tamvet - 1 and maiortamesq == tamvet - 1 and k > 0:
            maiortam = tamvet
        elif maiortamdir > maiortamesq:
            maiortam = maiortamdir
        else:
            maiortam = maiortamesq
            

        return maiortam