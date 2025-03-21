'''
Write a function add2D() that takes two two-dimensional lists of same size (i.e., same number of rows and columns)
as input arguments and increments every entry in the first list with the value of the corresponding entry in the second list.
t = [[4, 7, 2, 5], [5, 1, 9, 2], [8, 3, 6, 6]]
s = [[0, 1, 2, 0], [0, 1, 1, 1], [0, 1, 0, 0]]
add2D(t,s)
for row in t:
    print(row)
[4, 8, 4, 5]
[5, 2, 10, 3]
[8, 4, 6, 6]
'''

t = [[4, 7, 2, 5], [5, 1, 9, 2], [8, 3, 6, 6]]
s = [[0, 1, 2, 0], [0, 1, 1, 1], [0, 1, 0, 0]]

nrows = len(t)
ncols = len(t[0])
def add2D(t,s):
    for i in range(nrows):
      for j in range(ncols):
         t[i][j] += s[i][j]
    for row in t:
        print(row)

add2D(t, s)

'''
did you got the reason?
yes " answered the proclaimer "
good. now, we all know the truth
'''