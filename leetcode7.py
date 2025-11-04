"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-2^31 <= x <= 2^31 - 1
"""

class Solution:
    def reverse(self, x: int) -> int:

        if x == 0:
            return 0
            
        if x<0:
            negative = 1
            number = -1*x
        else:
            negative = 0
            number = x
        integer = ""
        while number>=10:
            digit = number%10
            integer += str(digit)
            number = number//10
        integer += str(number)

        while integer[0]==0:
            integer = integer[1:]

        n = len(integer)
        output = 0

        for i in range(n):
            letter = int(integer[n-1-i])
            output += letter * pow(10,i)

        if negative==1:
            output = -1*output
        
        if output>pow(2,31)-1 or output<-1*pow(2,31):
            return 0

        return output