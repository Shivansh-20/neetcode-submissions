class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen and n > 1: #while because iteration not known
            seen.add(n)
            square_sum = 0
            while n:
                digit = n % 10
                square_sum += digit * digit
                n //= 10
            n = square_sum
        return n == 1  #return is of a function not while loop
            
        
        


'''Create an empty set() called seen.
While n is not 1 and hasn't been seen before:
Add n to seen.
Compute the sum of the squares of its digits.
Assign that sum back to n.
Return whether n == 1.'''
        