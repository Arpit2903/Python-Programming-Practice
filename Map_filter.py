# list_1 = [1,2,3,4,5,6,7,8,9]
#
# def is_greater_5(num):
#     return num > 5
#
# gr_than_5 = list(filter(is_greater_5,list_1))
# print(gr_than_5)
from functools import reduce
list1 = [1,2,3,4,5]
result = reduce(lambda x,y:x+y,list1)
print(result)
