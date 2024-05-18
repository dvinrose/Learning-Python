'''
3.34 Implement function pay() that takes as input two arguments: an hourly wage and the
number of hours an employee worked in the last week. Your function should compute and
return the employee’s pay. Any hours worked beyond 40 is overtime and should be paid at
1.5 times the regular hourly wage
'''

hourly_wage = 15
Nhours = int(input("please enter the number of hours worked: "))

def pay(hourly_wage, Nhours):
    if Nhours > 40:
        regular_pay = 40 * hourly_wage
        overtime_pay = (( Nhours - 40 ) * (hourly_wage * 1.5) )
        total_pay = regular_pay + overtime_pay
        return total_pay
    else:
        regular_pay = hourly_wage * Nhours
        return regular_pay

x = pay(hourly_wage, Nhours)
print(x)

