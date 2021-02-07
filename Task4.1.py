# ///////////Refactored Task #2////////////
import random as r


def generate_dictionary(_some_params, _num, _max):              # Creation of the function to generate dictionary
    _element_params = r.sample(_some_params, _num)              # Number of elements within 1 dict.
    _dict_item = {}
    for _element in _element_params:
        _dict_item[_element] = r.randint(0, _max)               # Generation of 1 pair key-value
    return _dict_item

params = ['age', 'weight', 'height', 'tally', 'shoes_size', 'dress_size', 'pants_size']  # Made up keys

mylist = []
for i in range(0, 5):
    mylist.append(generate_dictionary(params, 3, 100))      # Generating 5 dictionaries with params
print(mylist)


def result_dict():                                          # Creating of the function for result dictionary
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
    return result_dict

print(result_dict())