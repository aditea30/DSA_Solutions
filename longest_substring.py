class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''Aproach followed- 
           1.  we take 2 pointers left and right both at first index and len=0
           2. we check if the element in right pointer exsists in the set
           if no we increase right and add elemnt to the map with index(tuple)
           3. If yes then we jump the left pointer to the right pointer posistion 
            and update the index to current posistion until entire array is 
            traversed'''

        set_map=set()
        n=len(s)
        left =0
        length=0
        for right in range(n):
            while s[right] in set_map : #if element at o index is presesnt in set 
                set_map.remove(s[left])  #if presesnt remove duplicate 
                left+=1
            set_map.add(s[right]) # if not presesnt add the element to set
            length=max(length,right-left+1)
        return length
#Test case
s="abcabcbb"
sol=Solution()
print("The longest substring without repeat :",sol.lengthOfLongestSubstring(s))
