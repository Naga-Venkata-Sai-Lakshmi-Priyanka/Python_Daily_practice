"""
Level 1: Basics
Write a program to check if a number is positive, negative, or zero.
"""
n=-17
if n>=0:
   if n==0:
       print('Number is zero')
   else:
       print("The number is positive")
else:
    print('The number is negative')

"""Check if a person is eligible to vote (age ≥ 18)."""
age=12
if age>=18:
    print("The person is eligible to vote")
else:
    print("The person is not eligible to vote")
"""Level 2: Logical Conditions
Given a student’s GPA:
GPA ≥ 3.7 → "Excellent"
GPA ≥ 3.0 → "Good"
Else → "Needs Improvement"
"""
GPA=3.8
if GPA>=3.7:
    print("The grade is excellent")
elif GPA>=3.0 and GPA<3.7:
    print("The grade is good")
else:
    print("The grade needs improvement")
""" Check if a number is even or odd. """
num=11
if num%2==0:
    print("the number is even")
else:
    print("The number is odd")
"""Check if a patient is eligible for insurance coverage
(Age ≥ 18 AND has insurance flag = True)"""
age=13
has_insurance=True
if age>=18 and has_insurance:
    print("The patient is eligible for insurance coverage")
else:
    print("The patient is not eligible for insurance coverage")
"""Level 1: for loop
Print numbers from 1 to 10.
Print each character in a string."""
for i in range(1,11):
    print(i)
i="apple"
for j in i:
    print(j)
"""Level 2: Loop with Conditions
Print all even numbers between 1 and 20.
Count how many vowels are in a string."""
for i in range(1,21):
    if i%2==0:
        print(i)
word='throat'
vowel='aeiou'
count=0
for i in word:
    if i in vowel:
        count+=1
print(count)
"""
Level 3: while loop
Print numbers from 5 to 1 using while.
"""
n=6
while n>0:
    n=n-1
    print(n)
"""Keep asking user to enter a number until they enter 0."""
n=int(input('enter a number:'))
while True:
    n=int(input('enter number:'))
    if n==0:
        break
        print('You entered 0. So stopped the loop')
    else:
        print(f"you entered {n}")

"""
Mini Project : Login Attempt System (Loops)
Task:
Set a correct password
Allow user 3 attempts
Lock account after 3 failures"""

password='Sa!sekahra'
count=3
while count>0:
    your_password = input('enter your password:')

    if password==your_password:
        print("Your password is correct")
        break
    else:
        count -= 1
        print(f"you have only {count} attempts left")
if count==0:
    print("Account locked")


