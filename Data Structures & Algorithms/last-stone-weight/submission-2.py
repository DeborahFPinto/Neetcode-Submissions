class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones) > 1:
            stones.sort()
            
            maxstone = max(stones)
            stones.remove(maxstone)
            secmaxstone = max(stones)
            stones.remove(secmaxstone)

            if maxstone != secmaxstone:
                stones.append(maxstone - secmaxstone)

        if len(stones) == 0:
            return 0
        else:
            return stones[0]