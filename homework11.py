def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(2, 3, 4)
print_params(7, 'b')
print_params(b='453', c=64)
print_params(b = 25)
print_params(c = [1,2,3])
print()

values_list = [False, 'абабабаб', 6478]
values_dict = {'a': 'fsdhcjk', 'b': 8765, 'c': True}

print_params(*values_list)
print_params(**values_dict)
print()

values_list_2 = [34, 'aaaaaaaaaa']
print_params(*values_list_2, 42)

