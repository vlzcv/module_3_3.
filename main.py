def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(b = 25)
print_params(c = [1,2,3])
list = [1,3,5]
print_params(list)
print_params(*list)

value_list = [1, False, "Hello"]
values_dict = {'a': 2, 'b': "string", 'c': True}
print_params(*value_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)