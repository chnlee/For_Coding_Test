# sort(), sorted()
_list = [5, 6, 4, 8, 2, 3]
sorted_list = sorted(_list) # 2, 3, 4, 5, 6, 8
_list.sort()
print(_list) # 2, 3, 4, 5, 6, 8

_set = {65, 12, 15, 156, 31, 54, 94, 82, 31}
_set.sort() # Error!!!!
print(sorted(_set)) # 12, 15, 31, 54, 65, 82, 94, 156
print(type(sorted(_set)))
#descending order
_list = [5, 6, 4, 8, 2, 3]
sorted_list = sorted(_list, reversed = True) # 8, 6, 5, 4, 3, 2
#List of Tuple
_list = [(1, 3), (8, 2), (2, 5), (4, 7)]
sorted_list = sorted(_list, key = lambda dt: dt[1]) # (8, 2), (1, 3), (2, 5), (4, 7)

_list = [(1, 3), (8, 2), (2, 5), (4, 7)]
sorted_list = sorted(_list, key = lambda dt: (dt[1], -dt[0])) # (8, 2), (1, 3), (2, 5), (4, 7)
# variable type of sorting
_list = ["CHicken", "hamburger", "Sushi", "chocolate"]

print(sorted(_list)) # ['CHicken', 'Sushi', 'chocolate', 'hamburger']
print(sorted(_list, key = lambda dt: dt.lower())) # ['CHicken', 'chocolate', 'hamburger', 'Sushi']



