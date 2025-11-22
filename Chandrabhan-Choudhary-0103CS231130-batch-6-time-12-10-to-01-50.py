'''
Basic If–Else Problems: 
1. Write a program to check whether a number is positive, negative, or zero.
Solution:
'''
num = int(input("Enter a no. : "))
if num>0:
    print(f"{num} is a positive integer.")
elif num<0:
    print(f"{num} is a negative integer.")
else:
    print(f"{num} is zero")

'''
2. Write a program to check whether a number is even or odd. 
Solution:
'''
num = int(input("Enter a no. : "))
if num%2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")

'''
3. Write a program to check if a given year is a leap year or not. 
Solution:
'''
yr = int(input("Enter year: "))
if yr%4 == 0 and yr%100 != 0 and yr%400 == 0:
    print(f"{yr} is a leap year.")
else:
    print(f"{yr} is not a leap year.")

'''
4. Write a program to find the greatest of two numbers. 
solution:
'''
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1>num2:
    print(f"{num1} is greatest.")
elif num2>num1:
    print(f"{num2} is greatest.")
else:
    print(f"{num1} and {num2} are equal.")

'''
5. Write a program to check whether a person is eligible to vote (age >= 18). 
solution:
'''
age = int(input("Enter age: "))
if age >= 18:
    print("Congratulations! you can vote.")
else:
    print("You are not eligible.")

'''
6. Write a program to check whether a given character is a vowel or consonant.
solution:
'''
char = input("Enter any character: ")
vowel = ['a','e','i','o','u','A','E','I','O','U']
if char in vowel:
    print(f"{char} is a vowel.")
else:
    print(f'{char} is a consonant.')

'''
7. Write a program to check if a number is divisible by 5. 
solution:
'''
num = int(input("Enter a number: "))
if num%5 == 0:
    print(f"{num} is divisible by 5.")
else:
    print(f"{num} is not divisible by 5.")

'''
8. Write a program to determine whether a given number is a single-digit, two-digit, or more than two-digit 
number.  
solution:
'''
num = int(input("Enter a number: "))
if num<10:
    print(f"{num} is single digit.")
elif num >=10 and num<100:
    print(f"{num} is two digit.")
else:
    print(f"{num} is more than two digit.")

'''
9. Write a program to check whether a student has passed or failed (passing marks = 40).
solution:
'''
marks = int(input("Enter marks: "))
if marks >= 40:
    print("Passed.")
else:
    print("Failed.")

'''
10. Write a program to find whether the entered number is a multiple of both 3 and 7.
solution:
'''
num = int(input("Enter a number: "))
if num%3 == 0 and num%7 == 0:
    print(f"{num} is a multiple of both 3 and 7.")
else:
    print(f"{num} is not a multiple of both 3 and 7.")








'''
Ladder If & Nested If: 
1. Write a program to find the greatest among three numbers.
solution:
'''
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3
print("The largest number is", largest)

'''
2. Write a program to classify a person based on age: Child (<13), Teenager (13-19), Adult (20-59), Senior (60+).
solution:
'''
age = int(input("Enter age: "))
if age < 13:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 59:
    print("Adult")
else:
    print("Senior")

'''
3. Write a program to assign grades based on marks: 90-100: A, 75-89: B, 50-74: C, 35-49: D, <35: Fail.
solution:
'''
marks = float(input("Enter marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
elif marks >= 35:
    print("Grade: D")
else:
    print("Fail")

'''
4. Write a program to check the type of triangle (equilateral, isosceles, or scalene) based on sides.
solution:
'''
side1 = float(input("Enter length of side 1: "))
side2 = float(input("Enter length of side 2: "))
side3 = float(input("Enter length of side 3: "))
if side1 == side2 and side2 == side3:
    print("Equilateral triangle")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("Isosceles triangle")
else:
    print("Scalene triangle")

'''
5. Write a program to check if a character is uppercase, lowercase, digit, or special symbol.
solution:
'''
char = input("Enter a character: ")
if 'a' <= char <= 'z':
    print("Lowercase alphabet")
elif 'A' <= char <= 'Z':
    print("Uppercase alphabet")
elif '0' <= char <= '9':
    print("Digit")
else:
    print("Special symbol")

'''
6. Write a program to calculate electricity bill based on units: Up to 100 units: ₹5 per unit, 101–200 units: ₹7 per unit, Above 200 units: ₹10 per unit.
solution:
'''
units = int(input("Enter number of units: "))
bill = 0
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)
else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)
print(f"Total electricity bill: ₹{bill}")

'''
7. Write a program to determine the largest of four numbers using nested if.
solution:
'''
n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
n3 = float(input("Enter third number: "))
n4 = float(input("Enter fourth number: "))
if n1 > n2:
    if n1 > n3:
        if n1 > n4:
            largest = n1
        else:
            largest = n4
    else:
        if n3 > n4:
            largest = n3
        else:
            largest = n4
else:
    if n2 > n3:
        if n2 > n4:
            largest = n2
        else:
            largest = n4
    else:
        if n3 > n4:
            largest = n3
        else:
            largest = n4
print("The largest number is", largest)

'''
8. Write a program to check if a given year is a century year and also a leap year.
solution:
'''
year = int(input("Enter a year: "))
if year % 100 == 0:
    print(year, "is a century year.")
    if year % 400 == 0:
        print(year, "is also a leap year.")
    else:
        print(year, "is not a leap year.")
else:
    print(year, "is not a century year.")

'''
9. Write a program to classify BMI value: Underweight (<18.5), Normal (18.5-24.9), Overweight (25-29.9), Obese (30+).
solution:
'''
weight_kg = float(input("Enter weight in kg: "))
height_m = float(input("Enter height in meters: "))
bmi = weight_kg / (height_m **2)
print("Your BMI is:", round(bmi, 2))
if bmi < 18.5:
    print("Classification: Underweight")
elif bmi < 25:
    print("Classification: Normal")
elif bmi < 30:
    print("Classification: Overweight")
else:
    print("Classification: Obese")

'''
10. Write a program to display the smallest number among three using nested if.
solution:
'''
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
if num1 < num2:
    if num1 < num3:
        smallest = num1
    else:
        smallest = num3
else:
    if num2 < num3:
        smallest = num2
    else:
        smallest = num3
print("The smallest number is", smallest)







'''
For Loop Problems: 
1. Write a program using a for loop to print all Armstrong numbers between 100 and 999.
solution: 
'''
print("Armstrong numbers between 100 and 999 are:")
for num in range(100, 1000):
    num_str = str(num)
    order = len(num_str)
    sum_of_powers = 0
    for digit_char in num_str:
        digit = int(digit_char)
        sum_of_powers += digit ** order
    if num == sum_of_powers:
        print(num)
'''
2. Write a program to generate and display the first n prime numbers using a for loop.
solution:
'''
import sys
n = int(input("Enter the number of prime numbers to generate: "))
l = []
primes_found = 0
for num in range(2, sys.maxsize):
    if primes_found == n:
        break
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        l.append(num)
        primes_found += 1
print(l)
'''
3. Write a program to display all numbers from 1 to 500 that are divisible by 3, but the sum of their digits should not exceed 10.
solution:
'''
print("Numbers from 1 to 500 divisible by 3 with digit sum <= 10:")
l = []
for num in range(1, 501):
    if num % 3 == 0:
        sum_digits = 0
        for digit_char in str(num):
            sum_digits += int(digit_char)
        if sum_digits <= 10:
            l.append(num)
print(l)
'''
4. Write a program using a for loop to print a pyramid of stars (*) of height n.
solution:
'''
n = int(input("Enter the height of the pyramid: "))
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", end="")
    print()
'''
5. Write a program to accept a string and check whether it is a pangram.
solution:
example panagram : the quick brown fox jumps over the lazy dog
'''
input_string = input("Enter a string to check for pangram: ").lower()
alphabets = "abcdefghijklmnopqrstuvwxyz"
is_pangram = True
for char in alphabets:
    if char not in input_string:
        is_pangram = False
        break
if is_pangram:
    print("The string is a pangram.")
else:
    print("The string is not a pangram.")
'''
6. Write a program using a for loop to print all twin primes between 1 and 100.
solution:
'''
print("Twin primes between 1 and 100:")
l = []
for num in range(2, 100):
    is_prime1 = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime1 = False
            break
    if is_prime1:
        num2 = num + 2
        is_prime2 = True
        for i in range(2, int(num2**0.5) + 1):
            if num2 % i == 0:
                is_prime2 = False
                break
        if is_prime2 and num2 < 100:
            l.append((num,num2))
print(l)
'''
7. Write a program that accepts a number and prints whether it is a Harshad number.
solution:
Harshad number - a postitve integer that is divisible by the sum of its own digits.
'''
num = int(input("Enter a number to check for Harshad number: "))
sum_digits = 0
for digit_char in str(num):
    sum_digits += int(digit_char)
if sum_digits != 0 and num % sum_digits == 0:
    print(num, "is a Harshad number.")
else:
    print(num, "is not a Harshad number.")
'''
8. Write a program to generate Pascal’s Triangle up to n rows.
solution:
'''
n = int(input("Enter the number of rows for Pascal's Triangle: "))
row = [1]
for i in range(n):
    print(" ".join(map(str, row)))
    new_row = [1]
    for j in range(len(row) - 1):
        new_row.append(row[j] + row[j+1])
    new_row.append(1)
    row = new_row
'''
9. Write a program using a for loop to display the sum of the series: 1² + 2² + 3² + ... + n²
solution:
'''
n = int(input("Enter the value of n for sum of squares series: "))
total_sum = 0
for i in range(1, n + 1):
    total_sum += i * i
print("The sum of the series is:", total_sum)
'''
10. Write a program that accepts a number and prints whether it is a Strong number.
solution:
Strong number - the sum of the factorials of its digits is equal to the number itself.
'''
num = int(input("Enter a number to check for Strong number: "))
sum_of_factorials = 0
for digit_char in str(num):
    digit = int(digit_char)
    factorial = 1
    if digit > 0:
        for i in range(1, digit + 1):
            factorial *= i
    sum_of_factorials += factorial
if sum_of_factorials == num:
    print(num, "is a Strong number.")
else:
    print(num, "is not a Strong number.")






'''
While Loop Problems: 
11. Write a program using a while loop to find the reverse of a number and check if the reversed number is prime.
solution:
'''
num = int(input("Enter a number: "))
reversed_num = 0
temp = num
while temp > 0:
    digit = temp % 10
    reversed_num = reversed_num * 10 + digit
    temp //= 10
print("Reversed number:", reversed_num)
is_prime = True
if reversed_num <= 1:
    is_prime = False
else:
    i = 2
    while i * i <= reversed_num:
        if reversed_num % i == 0:
            is_prime = False
            break
        i += 1
if is_prime:
    print(reversed_num, "is a prime number.")
else:
    print(reversed_num, "is not a prime number.")

'''
12. Write a program that continues to accept numbers from the user until the sum of digits of all numbers entered becomes greater than 100.
solution:
'''
total_digit_sum = 0
while total_digit_sum <= 100:
    num = int(input(f"Current digit sum is {total_digit_sum}. Enter a number: "))
    temp = num
    while temp > 0:
        total_digit_sum += temp % 10
        temp //= 10
print("Total sum of digits has exceeded 100. Final sum:", total_digit_sum)

'''
13. Write a program using a while loop to check whether a number is a Duck number.
solution:
A Duck number is a positive number that contains at least one zero, excluding zeros in leading positions.
'''
num_str = input("Enter a number to check for Duck number: ")
is_duck = False
i = 0
n = len(num_str)
while i < n:
    if num_str[i] == '0' and num_str[0] != '0':
        is_duck = True
        break
    i += 1
if is_duck:
    print(num_str, "is a Duck number.")
else:
    print(num_str, "is not a Duck number.")

'''
14. Write a program using a while loop to check if it is a Happy number.
solution:
A number (positive integer) is called a happy number when it is replaced 
by the sum of the squares of its digits on a repeated basis until the sum of the squares of its digits equals to 1.
'''
num = int(input("Enter a number to check for Happy number: "))
seen = set()
while num != 1 and num not in seen:
    seen.add(num)
    sum_sq = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum_sq += digit * digit
        temp //= 10
    num = sum_sq
if num == 1:
    print("It is a Happy number.")
else:
    print("It is not a Happy number.")

'''
15. Write a program using a while loop to find the largest prime factor of a given number.
solution:
'''
n = int(input("Enter a number to find its largest prime factor: "))
largest_prime = -1
i = 2
while i * i <= n:
    while n % i == 0:
        largest_prime = i
        n //= i
    i += 1
if n > 1:
    largest_prime = n
print("The largest prime factor is:", largest_prime)

'''
# 16. Write a program to repeatedly accept a string from the user until the string entered is a palindrome.
solution:
'''
while True:
    input_str = input("Enter a string: ")
    reversed_str = input_str[::-1]
    if input_str == reversed_str:
        print("It is a palindrome. Exiting.")
        break
    else:
        print("Not a palindrome. Try again.")

'''
17. Write a program using a while loop to compute the digital root of a number.
solution:
The digital root of a number is the single-digit value obtained by repeatedly summing its digits until only one digit remains.
'''
num = int(input("Enter a number to find its digital root: "))
while num > 9:
    sum_digits = 0
    temp = num
    while temp > 0:
        sum_digits += temp % 10
        temp //= 10
    num = sum_digits
print("The digital root is:", num)

'''
18. Write a program using a while loop to generate the Collatz sequence for a given number.
solution:
Starting with any positive integer N, Collatz sequence is defined corresponding to n as the numbers formed by the following operations :
If n is even, then n = n / 2.
If n is odd, then n = 3*n + 1.
Repeat above steps, until it becomes 1.
'''
n = int(input("Enter a number to generate its Collatz sequence: "))
print("Collatz sequence:", end=" ")
while n != 1:
    print(n, end=" -> ")
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
print(1)

'''
19. Write a program using a while loop to check whether it is a Kaprekar number.
solution:
A Kaprekar number is a number whose square can be split into two parts that add up to the original number, with none of the parts being zero.
'''
num = int(input("Enter a number to check for Kaprekar number: "))
square = num * num
square_str = str(square)
is_kaprekar = False
i = 1
n = len(square_str)
while i < n:
    part1_str = square_str[:i]
    part2_str = square_str[i:]
    if part1_str and part2_str:
        part1 = int(part1_str)
        part2 = int(part2_str)
        if part1 > 0 and part2 > 0 and part1 + part2 == num:
            is_kaprekar = True
            break
    i += 1
if is_kaprekar:
    print(num, "is a Kaprekar number.")
else:
    print(num, "is not a Kaprekar number.")

'''
20. Write a program to simulate an ATM machine using a while loop.
solution:
'''
balance = 1000
while True:
    print("\nATM Menu:")
    print("1. Check balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    if choice == '1':
        print("Your current balance is: ₹", balance)
    elif choice == '2':
        deposit = float(input("Enter amount to deposit: "))
        if deposit > 0:
            balance += deposit
            print("Deposit successful. New balance: ₹", balance)
        else:
            print("Invalid amount.")
    elif choice == '3':
        withdraw = float(input("Enter amount to withdraw: "))
        if 0 < withdraw <= balance:
            balance -= withdraw
            print("Withdrawal successful. New balance: ₹", balance)
        else:
            print("Insufficient balance or invalid amount.")
    elif choice == '4':
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")