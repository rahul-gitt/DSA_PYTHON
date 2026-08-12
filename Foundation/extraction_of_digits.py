n = int(input("Enter a number : "))
num = n

while num > 0:
    last_digit = num % 10
    print("The last digit is :",last_digit)
    num = num// 10