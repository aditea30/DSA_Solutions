from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        #Moore's approach 
        count1=0
        count2=0
        el1=None
        el2=None
        for i in range(len(nums)):
            #Both the elements cannot have same number
            if (count1==0 and nums[i]!=el2 ):
                count1=1
                el1=nums[i]
            elif(count2==0 and nums[i]!=el1):
                count2=1
                el2=nums[i]
            #On traversing if next element is same as element then icrease count
            elif (el1==nums[i]) :
                count1+=1
                
            elif (count2==nums[i]):
                count2+=1
            else :
                count1-=1
                count2-=1

        count1=0 #these will count if the el1 and el2 are majority elements
        count2=0
        for i in range(len(nums)):
            
            if (nums[i]==el1):
                count1+=1
            elif(nums[i]==el2):
                count2+=1
        ls=[]
        majority=(len(nums)//3)
        if count1 >majority :
            ls.append(el1)
        if( count2 >majority):
            ls.append(el2)
        
        return ls
Solution()
#Test case 
nums=[3,5,3,5,3,6,7,5]
sol=Solution()
print("Majority element > n/3 is :",sol.majorityElement(nums))