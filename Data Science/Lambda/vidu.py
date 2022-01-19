'''
sorted trong ham lambda
coordinate2D = [(6,9), (9,6), (-1,3), (2,10)]
print(sorted(coordinate2D)) # sap xep theo bien x
print(sorted(coordinate2D, key = lambda point:point[1])) # sap xep theo bien y

number_list = [5,3,-2,1,4,-1,-3,4,5]
print(sorted(number_list))
print(sorted(number_list, key = lambda x:abs(x)))
'''


#lambda for map function
'''
list_keyword = ["Duong", "dep trai", "vcl"]
print(list(map(lambda x : x.title(), list_keyword)))
new_list = [keyword.title() for keyword in list_keyword]
print(new_list)
'''

# Use lambda for filter function
'''
list_number = [1,2,3,4,5,6,7,8,9,10]
print(list(filter(lambda x : x%2 !=0, list_number)))
new_list = [x for x in list_number if x%2 != 0]
print(new_list)
'''


# Use lambda for reduce function
from functools import reduce
sequence = [1,3,5,9,6,2,8]
print(reduce(lambda a,b : a + b, sequence))
print(reduce(lambda a,b : a if a >b else b, sequence))