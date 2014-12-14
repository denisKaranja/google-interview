#!/usr/bin/python
"""
Author: Denis Karanja,
Institution: The University of Nairobi, Kenya,
Department: School of Computing and Informatics, Chiromo campus
Email: dee.caranja@gmail.com,
Task: Flatten a nested list
License type: MIT :)
"""
flat_list = []
country = ["Kenya", ["Nairobi",["Buruburu", ["Phase1", "Phase2"], "Lavington"], "Mombasa", "Kisumu"], "Tanzania"]
name = ["Abby", ["Moses", "James", "Joseph", ["Nampaso", "Karanja", "Omondi"]], ["Lilian"]]

array = [1, 2, 3, 4, [5, country, 6, 7], [8, 9], 10, [11], name]

def flatten_list(my_list):
  if type(my_list) is not list:
    raise TypeError("Function 'flatten_list' expects a list. '{}' given ".format(type(my_list)))
  elif type(my_list) is list:
    print "\nNested list \n{}". format(my_list)
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


print "\n++++++++++++++++++++++++++++++++"
print "\nFlattened array \n{}\n". format(flatten_list(1234))
