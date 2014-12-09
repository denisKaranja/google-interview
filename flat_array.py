#!/usr/bin/python
flat_list = []
country = ["Kenya", ["Nairobi",["Buruburu", ["Phase1", "Phase2"], "Lavington"], "Mombasa", "Kisumu"], "Tanzania"]
name = ["Abby", ["Moses", "James", "Joseph", ["Nampaso", "Karanja", "Omondi"]], ["Lilian"]]

array = [1, 2, 3, 4, [5, country, 6, 7], [8, 9], 10, [11], name]

def flatten_list(my_list):
  if type(my_list) is not list:
    return "Function 'flatten_list' expects a list. '{}' given ".format(type(my_list))
  elif type(my_list) is list:
    #check if list is null
    if len(my_list) != 0:
      for i, num_one in enumerate(my_list):
        #check if elements inside list is a list
        if type(num_one) is list:
          flatten_list(num_one)
        else:
          flat_list.append(num_one)
    else: return "List passed is empty."
  return flat_list
  
print "\nNested list \n{}". format(array)
print "\n++++++++++++++++++++++++++++++++"
print "\nFlattened array \n{}". format(flatten_list(array))

