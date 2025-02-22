from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        count1=0
        count=0
        
        for i in range(n):
            if (count==0):
                count+=1
                element=nums[i]
            elif(nums[i]==element):
                count+=1
            else:
                count-=1
        for i in range(n):
            if(nums[i]==element):
                count1+=1
        if(count1 > (n//2)):
            return element
Solution()
# Example usage:
nums = [3, 2, 3]
solution = Solution()
print("Elements appearing more than n/3 times:", solution.majorityElement(nums))
