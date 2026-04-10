class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones) > 1:
            stones.sort()
            tam = len(stones)

            maxstone = stones[tam - 1]
            stones.remove(maxstone)
            secmaxstone = stones[tam-2]
            stones.remove(secmaxstone)

            if maxstone != secmaxstone:
                stones.append(maxstone - secmaxstone)

        if len(stones) == 0:
            return 0
        else:
            return stones[0]