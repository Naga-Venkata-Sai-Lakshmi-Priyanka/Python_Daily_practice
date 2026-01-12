"""
PART 1: List Basics (Warm-up)
Practice Questions
Print:
First element
Last element
Change the 3rd element to a new value
Add a new element to the list
Remove one element from the list
"""
my_list=['apple','ball',1,21,321,34,(21,23)]
print(my_list[0])
print(my_list[-1])
my_list[3]={'book':'The sattvic way'}
print(my_list)
my_list.append('Jai')
print(my_list)
my_list.extend(['Ram','Bheem'] )
my_list.append(['Ram','Bheem'] )
print(my_list)
my_list.remove(my_list[6])
print(my_list)
"""PART 2: List Methods (VERY IMPORTANT)
Practice Questions
Use:
.insert()
.remove()
.pop()
Sort a list in:
Ascending order
Descending order
Count how many times a value appears
Find the index of an element"""
my_list1=[321,43,654,89,567,12,21]
my_list1.insert(1,9)
print(my_list1)
my_list1.pop()
print(my_list1)
my_list1.sort()
print(my_list1)
my_list1.sort(reverse=True)
print(my_list1)
my_lst=['jai',21,21,'jai']
my_lst=my_lst.count('jai')
print(my_lst)
"""PART 3: Looping Through Lists
Practice Questions
Print all elements using:
for loop
while loop
Print only even numbers from a list
Create a new list containing squares of numbers"""
count=0
my_list_nums=[12,32,34,2,3,4]
for i in my_list_nums:
    print(i)
while count<len(my_list_nums):
    print(my_list_nums[count])
    count+=1
lst=[]
for i in my_list_nums:
    if i%2==0:
       lst.append(i)
print(lst)
lst1=[]
lst_squares=[2,3,4,5,6]
for i in lst_squares:
    lst1.append(i**2)
print(lst1)
"""PART 4: List + Conditionals
Practice Questions
From a list of ages, print:
Minors (<18)
Adults (≥18)
From a list of GPAs, print only GPAs ≥ 3.5"""
ages=[12,31,23,4,5,67]
for age in ages:
    if age<18:
        print('Minor')
    else:
        print('Major')
GPAs=[3.3,3.5,4.0,3.9]
for GPA in GPAs:
    if GPA>=3.5:
        print(GPA)
    else:
        continue
"""PART 5: List Comprehension
Practice Questions
Create a list of squares using list comprehension
Filter even numbers using list comprehension
Convert names to uppercase using list comprehension"""
list1=[2,3,4,5,6,7,8,9]
my_list1_squares=[i**2 for i in list1]
print(my_list1_squares)
my_list1_evens=[i for i in list1 if i%2==0]
print(my_list1_evens)
list_names=['Priya','Scott','Jairam','vasudeva']
lst_nm=[i.upper() for i in list_names]
print(lst_nm)
"""Mini Project 1: Patient Age Analyzer (Healthcare)
Task:
Store patient ages in a list
Separate:
Minors
Adults
Count total adults"""
count=0
pt_age=[21,22,12,13,24,15,25]
for age in pt_age:
    if age>=18:
        count+=1
    else:
        print('Minors')

print('No.of Adults:',count)
"""Mini Project 2: Expense Tracker
Task:
Store daily expenses in a list
Find:
Total expense
Highest expense
Lowest expense"""
total=0
expenses=[1223, 3212,3245]
for i in expenses:
    total+=i
print('Total expenses:',total)
print('Highest expense:',max(expenses))
print('Lowest expense:', min(expenses))