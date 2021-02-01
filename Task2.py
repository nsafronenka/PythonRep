mylist = []
import random
params = ['age', 'weight', 'height', 'tally', 'shoes_size', 'dress_size', 'pants_size']     # Made up keys
for i in range(0, 5):
    element_params = random.sample(params, 3)           # Number of elements within 1 dict.
    dict_item = {}
    for element in range(0, 3):
        dict_item[element_params[element]] = random.randint(0, 100)     # Generation of 1 pair key-value
    mylist.append(dict_item)                                            # Adding generated dict.to mylist dict.
print(mylist)

result_dict = {}
for key in params:
    # This comment belongs to 3 rows below for better understanding.Check if my list has a dictionary with the key value
    max_value_index = None
    for dict_item in mylist:
        if key in dict_item:
            # Save the index of the dictionary with the maximum key value
            if max_value_index is None:
                max_value_index = mylist.index(dict_item)
            else:
                if dict_item[key] > mylist[max_value_index][key]:
                    max_value_index = mylist.index(dict_item)
    # Add item to the resulting list if a key is in the mylist at least once
    if max_value_index is not None:
        result_dict[key + '_' + str(max_value_index)] = mylist[max_value_index][key]
print(result_dict)

