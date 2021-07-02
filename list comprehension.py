import random
#list comprehension

_list = [ i for i in range(10)]

_set = [ i for i in range(3,13)]
# unpacking & list comprehension
print (*[1 if data in _set else 0 for data in _list], sep ='\n')

#multi-dimensional array

square = [[x**2 for x in range(3)] for _ in range(3)]
print(square)

#multiple of 3

tmp = [random.randrange(1,200) for i in range(100)]
_lst = [i for i in tmp if i % 3 ==0]

for j in range(100,0,-1):
  print(j)

#reverse the tuple
list_of_tuple = [(i,j) for i in range(100) for j in range(100, 0,-1)]
_listt = [(j,i) for i, j in list_of_tuple]
print(list_of_tuple) 