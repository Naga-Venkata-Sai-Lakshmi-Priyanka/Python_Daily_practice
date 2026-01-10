from functools import reduce
"""Lambda Functions
Write a lambda function to:
Add two numbers"""
add=lambda a,b: a+b
res=add(2,3)
print(res)
"""Write a lambda to:
Check if a number is even"""
even_num=lambda num: num%2==0
num=int(9)
print(even_num(num))
"""Write a lambda to:
Convert a string to uppercase"""
upper_str=lambda str_obj: str_obj.upper()
print(upper_str('priya'))
"""PART 2: map()
 Practice Questions
Given a list of numbers, use map() to:
Square each number"""
nums=[23,34,4,5,6,7]
square=lambda x:x*x
res=map(square,nums)
print(list(res))
"""Convert a list of names to uppercase"""
list_names=['priya','vasu','jai']
exp= map(lambda x: x.upper(),list_names)
print(list(exp))
"""Convert a list of strings to integers"""
str_list=['1','2','3']
exp=map(lambda x: int(x),str_list)
print(list(exp))
"""PART 3: filter()
Filter only even numbers from a list"""
nums=[22,23,24,25,155]
exp=filter(lambda x: x%2==0,nums)
print(list(exp))

"""Filter names that start with a vowel"""
list_names=['edward','james','angel']
exp= filter(lambda x: x[0]=='a' or x[0]=='e'or x[0]=='i' or x[0]=='o'or x[0]=='u',list_names)
print(list(exp))
"""Filter patients whose age ≥ 18"""
patient_age={'edward':18, 'james':13,'thomas':19,'jack':14}
exp=filter(lambda x: patient_age[x]>=18,patient_age.keys())
print(list(exp))
"""PART 4: reduce()
(Import from functools)
Find the sum of all numbers in a list
"""
list_numbers=[1,2,3,4,5,6]
sum_numbers=reduce(lambda x,y: x+y,list_numbers)
print(sum_numbers)
"""Find the maximum number in a list
"""
max_list=[99,9,87,60]
max_list_exp=reduce(lambda x,y: max(x,y), max_list)
print(max_list_exp)
"""Multiply all numbers in a list"""
multiply_list=[99,9,87,60]
multiply_list_exp=reduce(lambda x,y: x*y, multiply_list)
print(multiply_list_exp)
"""Mini Project 1: Student GPA Analyzer ⭐ (Recommended)
Task:
Store student GPAs in a list
Use:
filter() → GPAs ≥ 3.5
map() → Round GPAs
reduce() → Average GPA"""
gpas = [3.6, 3.9, 2.9, 4.0, 3.4]
high_gpas = list(filter(lambda x: x >= 3.5, gpas))
round_gpas = list(map(lambda x: round(x, 2), high_gpas))
average_gpa = reduce(lambda x, y: x + y, round_gpas) / len(round_gpas)
print(round(average_gpa, 2))
"""Mini Project 2:List of patient ages
Filter:
Adults (≥ 18)
Map:
Add risk label ("High Risk" if age ≥ 60)"""
list_ages=[12,18,34,56,23,90,87,78]
list_filter=filter(lambda x: x>=60,list_ages)
list_filter=map(lambda x:(x,'High risk') if x>=60 else(x,'Normal risk'),list_filter)
print(list(list_filter))