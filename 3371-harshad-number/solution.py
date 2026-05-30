class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        temp=x
        s=0
        while x>0:
            d=x%10
            s+=d
            x=x//10
        if temp%s==0:
            return s
        else:
            return -1
        
