'''2.28 Write the relevant Python expression or statement, involving a list of numbers lst
and using list operators and methods for these specifications:
(a) An expression that evaluates to the index of the middle element of lst
(b) An expression that evaluates to the middle element of lst
(c) A statement that sorts the list lst in descending order
(d) A statement that removes the first number of list lst and puts it at the end
Note: If a list has even length, then the middle element is defined to be the right most of the
two elements in the middle of the list.'''

# A ----------------------------
lst = [8, 1, 5, 2, 1, 3, 5, 9, 5, 5, 40, 8, 7, 5, 2, 3, 5, 9, 5, 20]
print(lst)

ad = len(lst)
print("list length: ", ad)
midItem = len(lst)//2
print("mid list length: ", midItem)
print("mid list item value: ", lst[midItem])
print("mid list item index value: ", lst.index(lst[midItem]))
# B ----------------------------
print("mid list item value: ", lst[midItem])
# C ----------------------------
lst.sort()
lst.reverse()
print(lst)
# D ----------------------------
lst.insert(ad, lst[0])
lst.pop(0)
print(lst)
