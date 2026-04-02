class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t) > len(s):
            return ""
        if t == s:
            return t
        if len(s) == len(t) and set(s) != set(t):
            return ''

        listSearching = list(t)
        listSearched = list(s)
        strResult = 'a'*1000
        strTemp = ''
        startsearching = 0
        tam = len(s)

        for i in range(tam):

            strTemp = ''
            listSearching = list(t)

            for j in range(i, tam):
                
                if listSearched[j] in listSearching:
                    listSearching.remove(listSearched[j])
                    startsearching = 1

                if startsearching:
                    strTemp += listSearched[j]

                if len(listSearching) == 0:
                    break

            if len(strTemp) < len(strResult)  and len(listSearching) == 0:
                strResult = strTemp
        
        if strResult == 'a'*1000:
            return ''
        
        return strResult







