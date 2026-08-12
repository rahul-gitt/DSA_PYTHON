n = int(input("Enter a number : "))
num = n

while num > 0:
    last_digit = num % 10
    print("The last digit is :",last_digit)
    num = num// 10

# Logic : 
'''
n= 1234
num = n
while num > 0:
    last = num % 10         -> 1234 % 10 = 4 
    print(last)             -> print = 4
    num = num // 10         -> 123
    and goes on upto num = 0
    then loop break

Time complexity = O(n)
Space complexity = 0(1)
'''