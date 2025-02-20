'''Approach-
    1. Take a hashmap in python dictionary to store cumulative sum
    2. Iterate through the array to find sum, and add sum to the map
    3. If sum==0, update length, and add element to the hash map 
    4. If while iterating a number already exsists in the map find max_length
        else - store the element in the hash map
    
    '''
class Solution:
    def maxLen(self, arr):
        n=len(arr)
        hash_map={}
        sum=0
        longest=0
        for i in range(n):
            sum+=arr[i]
            
            if sum==0:
                longest=i+1 #length will be index+1
            
            if sum in hash_map: #subarray with sum=0 exsists so just update length
                longest=max(longest, i-hash_map[sum])
                
            else:#add element to map
                hash_map[sum]=i
                
                
                
        return longest
        
#Test case
arr=[15, -2, 2, -8, 1, 7, 10, 23]
#Create an instance of Solution
sol=Solution()
print("Longest subarray with sum 0:", sol.maxLen(arr))