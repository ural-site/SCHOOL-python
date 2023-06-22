print('Hello World!')

lst = [1, 2, 3, None, 4]
[print(x) if x is not None else print('None') for x in lst]



