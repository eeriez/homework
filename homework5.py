my_list = ['apple', 'orange', 'banana', 'pomergranate', 'pear', 'tangerine']

print(my_list)
print(my_list[0])
print(my_list[-1])
print(my_list[2:5])
my_list[2] = 'grape'
print(my_list)


my_dict = {'apple': 'яблоко', 'orange': 'апельсин', 'banana': 'банан', 'pomergranate': 'гранат', 'pear': 'груша', 'tangerine': 'мандарин'}

print(my_dict)
print(my_dict['banana'])
my_dict['pear'] = 'пеар'
my_dict.update({'tangerine': 'тангерине',
                'orange': 'оранге'})
print(my_dict)
