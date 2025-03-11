Problem 1:Write an algorithm that calculates the sum of all natural numbers from 1 to a given number n.

The user should input a value for n.
The algorithm should compute the sum using a loop and display the result.


n = int(input("Enter a positive integer: "))

if n > 0:
    total = sum(range(1, n + 1))  # Using sum() function
    print("Sum of natural numbers from 1 to", n, "is:", total)
else:
    print("Error: Please enter a positive integer.")


Output-
Enter a positive integer: 10
Sum of natural numbers from 1 to 10 is: 55

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Problem 2:Write an algorithm that checks if a given number n is a prime number or not.

The user should input a value for n.
The algorithm should check whether the number is divisible by any number other than 1 and itself.


n = int(input("Enter a number: "))

if n > 1:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(f"{n} is not a prime number.")
            break
    else:
        print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")


Output-
Enter a number: 12
12 is not a prime number.

Enter a number: 13
13 is a prime number.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Problem 3: Find the Maximum of Three Numbers

Write an algorithm that takes three numbers as input and finds the largest of them.

The user should input three values: a, b, and c.
The algorithm should compare the numbers and print the maximum value.

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

max_num = max(a, b, c)  

print("The largest number is:", max_num)


Output-
Enter the first number: 12
Enter the second number: 23
Enter the third number: 5
The largest number is: 23.0

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Problem 4: Factorial Calculation

Write an algorithm that calculates the factorial of a number n.

The user should input a number n.
The algorithm should compute the factorial by multiplying all the integers from 1 to n.

def factorial(n):
    if n < 0:
        return "Error: Factorial is not defined for negative numbers."
    
    fact = 1
    for i in range(1, n + 1):  
        fact *= i  
    
    return fact

try:
    n = int(input("Enter a number: "))
    print(f"Factorial of {n} is: {factorial(n)}")
except ValueError:
    print("Error: Please enter a valid integer.")


Output-
Enter a number: 5
Factorial of 5 is: 120
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Problem 5: Check if a Number is Even or Odd

Write an algorithm that checks if a given number n is even or odd.

The user should input a value for n.
The algorithm should check whether n is divisible by 2 and display the result as either "Even" or "Odd".

n = int(input("Enter a number: "))

if n % 2 == 0:
    print("Even")
else:
    print("Odd")


Output-
Enter a number: 3
Odd
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


