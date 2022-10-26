class Solution:
    def climbStairs(self, n: int, x=1, y=1) -> int:
        if n < 1 or n > 45:
            print("Please enter a valid positive integer between 1 to 45 inclusive")
        else:
            for i in range(n-1):
                temp = x
                x = x + y
                y = temp
        
            return x

e1 = Solution()
print(e1.climbStairs(2))