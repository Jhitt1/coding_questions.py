# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.
# Question 1:
def hello_name(user_name):
    user_name = "user_NAME"
    print("user_NAME")
hello_name("user_name")

# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
# Question 2:
def first_odds():
    first_odds = 0
    while first_odds < 101:
        first_odds += 1
        if first_odds % 2 == 0:
            continue
        print(first_odds)

# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.
# Question 3:
def max_num_in_list(a_list):
    nums = a_list[0]
    for num in a_list:
        nums = num
    return nums
print(max_num_in_list([1,100,52,95,10,1025,455,2,78]))

# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).
# Question 4:
def is_leap_year(a_year):
    a_year = False
    if a_year % 4 ==0 and a_year % 100 != 0 or a_year % 400 == 0:
        a_year = True
        return a_year
a_year = int(input())
print(is_leap_year(a_year))