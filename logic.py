"""
def even_check(number):
    result = number%2==0
    return result

print(even_check(20))
print(even_check(21))
print()
# return true if any number is even inside a list

def check_even_list(num_list):
    even_nums = []
    for number in num_list:
        if number % 2 == 0:
            even_nums.append(number)
        else:
            pass
    return even_nums

print(check_even_list([1,3,5]))
print(check_even_list([2,4,6]))
print(check_even_list([2,1,1,1]))


stock_prices = [('APPL',200),('GOOG',400),('MSFT',100)]
for ticker,price in stock_prices:
    print(price)
"""
work_hours = [('Abby',100),('Billy',1000),('Cassie',800)]
def employee_check(work_hours):
    current_max = 0
    employee_of_month = ''
    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass
    return (employee_of_month,current_max)

print(employee_check(work_hours))

result = employee_check(work_hours)
print(result)

name,hours = employee_check(work_hours)
print(name)
print(hours)

