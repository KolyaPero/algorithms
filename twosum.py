class Solution(object):
    def twoSum(self, nums, target):
        k={}#создаем словарь, который будет сожержать элементы массива nums
        for i in range(len(nums)):
            b = target - nums[i]#ищем число b, которое при суммировании с и-тым числом массива даст значение target
            if b in k:
                return (k[b],i)#возвращай индекс числа b и i-тый индекс
            else:
                k[nums[i]] = i# закидывай в словарь i-тое значение массива и приравнивай его к индексу
solution = Solution()
result = solution.twoSum([2,7,11,15],9)
print(result)
