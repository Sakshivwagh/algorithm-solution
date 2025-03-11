---Armstrong Number

n = int(input("Enter a number: "))

sum = 0
temp = n

while temp > 0:
    digit = temp % 10
    temp = temp // 10
    sum += digit ** 3 

if sum == n:
    print("Armstrong")
else:
    print("Not Armstrong")

Output-
Enter a number: 12
Not Armstrong

Enter a number: 153
Armstrong