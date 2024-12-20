def add_item(item, item_list=None):
    if item_list is None:
        item_list = []
    item_list.append(item)
    return item_list

# Now the list is unique per function call
print(add_item("apple"))   # Output: ['apple']
print(add_item("banana"))  # Output: ['banana']
