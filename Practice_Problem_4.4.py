'''
Write function even() that takes a positive integer n as input and prints on the screen all
numbers between, and including, 2 and n divisible by 2 or by 3, using this output format:
even(17)
2, 3, 4, 6, 8, 9, 10, 12, 14, 15, 16,
'''

def even(n):
    if n % 2 == 0:
        print(n, end=', ')


for i in range(20):
    even(i)

weekday = 'Wednesday'
month = 'March'
day = 10
year = 2010
hour = 11
minute = 45
second = 33

'''
x = '{}, {} {}, {} at {}:{}:{}'.format(weekday, month, day, year, hour, minute, second)
print("\n",x)'''