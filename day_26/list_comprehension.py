# list comprehension [item_operation for item in list] # basic syntax
# or [item_operation for item in list if condition] # conditional syntax
#
# dict comprehension {new_key: new_value for item in list}

# example:
name = "Jason"
new_name = [letter for letter in name]
print(f'\n{"".join(new_name)}')  # break it apart and put it back together, because I am in the mood to do that.
# prints Jason

num_range = range(1, 5)
new_range = [n * 2 for n in num_range]
print(f"\n{new_range}")  # prints [2, 4, 6, 8]

num_range2 = range(1, 20)  # conditional list operation
new_range2 = [n * 2 for n in num_range2 if n % 2 == 0]
print(new_range2)  # prints [4, 8, 12, 16, 20, 24, 28, 32, 36]

my_list = [1, 2, 3]  # dict comprehension {new_key: new_value for item in list}
new_dict = {item: "A" for item in my_list}
print(new_dict)  # prints {1: 'A', 2: 'A', 3: 'A'}

new_dict2 = {key: item for (key, item) in new_dict.items() if key > 1}
print(new_dict2)  # conditional, prints {2: 'A', 3: 'A'} due to key being filtered
