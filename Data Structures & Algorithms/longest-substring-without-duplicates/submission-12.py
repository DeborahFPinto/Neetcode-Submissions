class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        maislongo = 0
        temp = 0
    
        for i in range(len(s)):

            listaCaract = []
            listaCaract.append(s[i])
            temp = 1

            for j in range(i + 1, len(s)):

                if s[j] in listaCaract:
                    listaCaract = []
                    if temp > maislongo:
                        maislongo = temp
                    temp = 0
                    break
                else: 
                    temp += 1
                    listaCaract.append(s[j])
                
                if j == len(s) - 1:
                    if temp > maislongo:
                        maislongo = temp

            if temp > maislongo:
                maislongo = temp
        return maislongo