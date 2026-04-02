class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        results = []

        while nums != []:
            cont = 0
            temp = nums[0]
            
            while True:
                if temp in nums:
                    nums.remove(temp)
                    cont += 1
                else:
                    break

            results.append((temp, cont))
        
        most_frequent = []
        for i in range(k):
            maior = 0
            num = 0
            for value, times in results:
                if times > maior:
                    maior = times
                    num = value

            most_frequent.append(num)
            results.remove((num, maior))
        
        return most_frequent
