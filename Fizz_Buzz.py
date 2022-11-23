#Fizz_Buzz in Python
class Solution(object):
    def Fizz_Buzz(self,n):
        result = []
        for i in range(1,n+1):
            #if a number is divisible by 3 and 5 both, print "Fizz_Buzz"
            if i%3 == 0 and i%5 ==0:
                result.append("Fizz_Buzz")
            #othrwise when the number is divisible by 3, print "Fizz"
            elif i%3 == 0:
                result.append("Fizz")
            #othrwise when the number is divisible by 5, print "Buzz"
            elif i %5 ==0:
                result.append("Buzz")
            #otherwise, write the number as a string
            else:
                result.append(str(i))
        return result
ob1 = Solution()
print(ob1.Fizz_Buzz(51))
