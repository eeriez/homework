immutable_var = 7, False, 'зима уже близко', [4, 7, 8]

print(immutable_var)

#immutable_var[0] = 8
#TypeError: 'tuple' object does not support item assignment
# Несмотря на то, что кортеж может содержать изменяемые элементы, такие как списки, сам кортеж изменяться не может

mutable_list = [4, 56, 7]

mutable_list[0] = True
mutable_list[1] = 8
mutable_list[2] = 'm'

print(mutable_list)
