# def a_first(a):
#     return a[1]
#
# l = [[1,14],[5,6],[0,2]]
# l.sort(key=a_first)
# # print(l)

l = [[1,14],[5,6],[0,2]]
l.sort(key=lambda x:x[1])
print(l)
