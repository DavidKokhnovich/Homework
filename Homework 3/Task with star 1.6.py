my_dict = {"name": 'David', "pet": "dog", "key": "house"}
my_dict['password'] = 1234
my_dict[('Привет!')] = ['Как', 'дела?']
print(my_dict.get("key"))
del my_dict['key']
print(my_dict.keys())
