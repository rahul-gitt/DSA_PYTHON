n= int(input("Enter your number : "))
num = n
result = 0

while num > 0:
    last_d= num % 10 
    result = (result * 10) + last_d
    num = num // 10

if n == result :
    print(f"The number {result} is Palindrome.")

else: 
    print(f"The number {result} is not a Palindrome.")


# Logic :
'''
n = 121
num = n
result = 0

while num > 0 :                                                 -> 1st-
     last_digit = num % 10                                      -> 121 % 10  = 1
     result = (result * 10) + last_digit                        -> 0*10 + 1 = 1
     num = num // 10                                            -> 12
                                                                 2nd-
                                                                -> 12 % 10 = 2
it repeat's until num becames 0 then the loop break             -> 1 * 10 + 2 = 12
                                                                -> 1 
and follows the condition part.

TC = O(log₁₀(n))
SC = O(1)
'''