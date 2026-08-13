n = int(input("Enter a number : "))
num = n
counter = 0
length = 0
result =0

while num > 0:
    length = len(str(n))
    last_digit = num % 10
    counter = last_digit**length
    num = num // 10
    result += counter

if n == result:
    print(f"The number {n} is Armstrong number.")
else:
    print(f"The number {n} is not a Armstrong number.")
