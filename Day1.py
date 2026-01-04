"""
Level 1: Basics
Create variables for:
first_name
last_name
city
Print them in one sentence.
"""
first_name="Priyanka"
last_name="Yeddanapudi"
city="Chicago"
print(first_name+ " " +last_name+" "+city)
print(first_name, last_name, city)
"""
Level 2: String Operations
Store a sentence in a variable and:
Print it in uppercase
Print it in lowercase
Find the length of the string.
"""
sentence= "hello Vasu, I Love you and I missed you so much"
print(sentence.upper())
print(sentence.lower())
print(len(sentence))
"""Level 3: String Formatting 
Store:
student name
university
GPA
Print this using f-strings."""
student_name="Priyanka"
University="Governors State University"
GPA= 3.8
print(f"Hi My name is {student_name} I'm masters student at {University}, and My GPA is {GPA}")
"""
Level 4: String Methods
Given:
email = "student2025@university.edu"
Extract only the username
Check if the email contains "@"
"""
email = "student2025@university.edu"
username=email.split("@")
print('username:', username[0])
"""
Mini Project 1: Student Introduction Generator (Recommended)
Requirements:
Use variables
Use strings
Use f-strings
Use .upper() or .title()
"""
name= 'Priyanka'
university='Governors State University'
res=f"My name is {name} and I'm an health informatics graduate student at {university.title()}"
print(res)

""" 
Mini Project 2: Email Username Extractor
Task:
Take an email string
Extract username
Print domain name
"""
email='nyeddanapudi@govst.edu'
username=email.split("@")
print('username:',username[0] )
domain_name=username[1]
print(domain_name)

"""
Mini Project 3: Patient Summary Generator (Healthcare-Focused)
Task:
Store patient name, age, condition
Print a clean medical summary 
"""
patient='Srujana'
age=24
condition='Lukemia'
print('--------Patient Summary Generator-------- ')
print(f'patient name: {patient}')
print(f'age: {age}')
print(f'condition: {condition}')