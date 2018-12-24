motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)

# motorcycles[0] = 'ducati'
# print(motorcycles)

# motorcycles.append('ducati')
# print(motorcycles)
# motorcycles.insert(3, 'ducati')
# print(motorcycles)

# del motorcycles[0]
# print(motorcycles)

# poped_motorcycles = motorcycles.pop()
# print(motorcycles)
# print(poped_motorcycles)

# last_owned = motorcycles.pop()
# print("The last motorcycle I owned was " + last_owned.title() + ".")
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() +'.')
del motorcycles[0]
print(motorcycles)