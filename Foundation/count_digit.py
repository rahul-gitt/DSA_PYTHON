n = int(input("Enter a number : "))
num = n
count = 0

while num > 0:
    last = num % 10
    count += 1
    num = num // 10
print("The number count is : ", count)




'''
n = 123
num = n

while num > 0 :
    last = num % 10        -> 123 % 10   = 3
    count += 1             -> remove count = 0 and assign 1
    num = num // 10        -> 12
    and goes up to num = 0
    and it automatically increase the count value 
    then loop break

Time Complexity = O()

'''