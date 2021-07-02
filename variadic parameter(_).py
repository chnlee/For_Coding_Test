# using asterisk as variadic parameter
_list = [1,2,3,4,5]

first, *rest, last = _list

print(_list)
print(rest) #print except the first and last element of list