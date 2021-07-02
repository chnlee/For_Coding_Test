# mistake(use list to find valuse)
data = [1,2,3,4,5,6,7,8,9,10]
for i in range(100):
  if i in data:
    print(1)

#set to save the time
_data_set = set(data)

for i in range(100):
  if i in data:
    print(1)

#lambda
test_list = ['TEST','test','TEST', 'tteesstt']

converted_list = list(set(map(lambda string:string.lower(), test_list)))
