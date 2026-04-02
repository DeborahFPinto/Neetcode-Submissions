class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if s1 == s2:
            return True
        if len(s1) > len(s2):
            return False

        palavra = list(s1)

        for i in range(len(s2)):

            if palavra == []:
                return True

            palavra = list(s1)

            for j in range(i, len(s2)):

                if s2[j] in palavra:
                    palavra.remove(s2[j])
                else:
                    break

        return False