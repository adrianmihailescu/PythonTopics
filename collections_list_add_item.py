def add_item(item, item_list=[]):
    item_list.append(item)
    return item_list

# Calling multiple times
print(add_item("apple"))   # Output: ['apple']
print(add_item("banana"))  # Output: ['apple', 'banana']  (unexpected!)
