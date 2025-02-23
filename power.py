class Solution:
    def myPow(self, x: float, n: int) -> float:
        #create  copy of power n to avoid changing original number
        copy_n=n
        ans=1
        if copy_n<0: #when copy of power is negative make it positive
            copy_n *=-1
        while (copy_n >0):
            if (copy_n%2==0): #when power is even
                x*=x
                copy_n//=2
            else :  #when power is odd
                ans*=x
                copy_n-=1
        if n<0: #handling negative exponent 
            ans=1/ans
        return ans
#Test case
x=2
n=10
sol=Solution()
print("The output is : ",sol.myPow(x,n))