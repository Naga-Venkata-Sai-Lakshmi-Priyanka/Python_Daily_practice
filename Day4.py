"""
Create a function greet_user(name) that:
takes a name
prints: Hello, <name>!
"""
def greet(name):
    print("hello, "+name)
(greet('priya'))

"""Task 2: Sum using *args
Create a function total_sum(*numbers) that:
accepts any number of integers
returns their sum"""
def total_sum(*numbers):
    i=0
    for i in numbers:
        i+=i
    print(i)
total_sum(23,33,44)
'''Task 3: Find maximum using *args
Create a function find_max(*values) that:
returns the largest number
if no values are passed, return "No values given"'''
def find_max(*values):
    if len(values)==0:
        return "there are no values"
    else:
        return max(values)
print(find_max())

"""Task 4: Student details using **kwargs
Create a function student_info(**details) that:
prints each key and value in this format:"""
def student_information(**details):
    print(details.keys())
    print(details.values())
    print(details.items())
    print(details)
student_information(
    name=['Priya','Vasudeva', 'Jai'],
program=['Graduate','Graduate','Kindergarten']
)
"""
Task 5: Mixed arguments
Create a function:
def order_food(item, *extras, **preferences):
Function should:
print item name
print extras
print preferences (like spice level, quantity)
"""
def order_item(item, *extras, **preferences):
    print(item)
    print(extras)
    print(preferences)
order_item('noodles', 'spring onions', 'cheese', spicelevel='spicy', ajinomoto='no')
"""Mini Project 1: Bank Account System
Create functions:
create_account(name, **details)
deposit(amount)
withdraw(amount)
show_balance()
Rules:
balance starts at 0
cannot withdraw more than balance
Use functions only, no classes yet."""
balance=0
def create_account(name, **details):
    return(name, details)
print(create_account('Jai ram', age=18, salary='$15,000'))
def deposit(amount):
    global balance
    balance+=amount
    print(f'amount deposited: {amount}')
deposit(100)
def withdraw(amount):
    global balance
    if amount>balance:
        print('No sufficient balance')
    else:
        balance-=amount
        print(f'amount withdrawn:{amount}')
withdraw(50)
def show_balance():
    print(f'current balance: {balance}')

show_balance()

"""Mini Project 2: Student Marks Analyzer
Create functions to:
accept subject marks using *args
calculate total and average
decide Pass/Fail (average ≥ 40)
Example call:
analyze_marks(55, 60, 35, 80)"""
def analyze_marks(*marks):
    sum=0
    avg=1
    for i in marks:
        sum+=i
        avg = sum / len(marks)
        if i>=40:
            print('pass')
        else:
            print('fail')
    print(f'sum of marks: {sum}')
    print(f'average of marks: {avg}')

(analyze_marks(55,66,40,35,90))
"""Mini Project 3: Shopping Cart
Create functions:
add_items(*items)
calculate_bill(**prices)
apply_discount(total, discount=0)"""
def add_items(*items):
    print(items)
add_items('apple','banana', 'pears', 'peach')
def calculate_bill(**prices):
    print(prices)
    global total
    total=sum(prices.values())
    print(f'total bill: {total}')
calculate_bill(banana=1.20,apple=3.3,pears=4.4,peach=5.5)
def apply_discount(total, discount):
    print(total-discount)
apply_discount(total,1.5)

"""Mini Project 4 (Data Engineer Style)
Create a function:
def log_events(*events, **metadata):"""
def log_events(*events, **metadata):
    print(events)
    print(metadata)
log_events('login','create a pipeline', 'upload', 'logout', user='naga', cloud='aws', status='success')




