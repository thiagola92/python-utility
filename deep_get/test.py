from deep_get import dget

structure = 10
key_list = []
print(1, dget(structure, key_list))

structure = 10
key_list = [1]
print(2, dget(structure, key_list))

structure = 10
key_list = ["yes"]
print(3, dget(structure, key_list))

structure = ['a', 'b', 'c']
key_list = [1]
print(4, dget(structure, key_list))

structure = ['a', [0, 2, 3], 'c']
key_list = [1]
print(5, dget(structure, key_list))

structure = ['a', [0, 2, 3], 'c']
key_list = [1, 2]
print(6, dget(structure, key_list))

structure = {'first': 0, 'second': [10,20,30,40,50]}
key_list = [2]
print(7, dget(structure, key_list))

structure = {'first': 0, 'second': [10,20,30,40,50]}
key_list = ['second']
print(8, dget(structure, key_list))

structure = {'first': 0, 'second': [10,20,30,40,50]}
key_list = ['second',2]
print(9, dget(structure, key_list))

structure = {'first': 0, 'second': [10,20,30,40,50]}
key_list = ['second',1000]
print(10, dget(structure, key_list, 0))