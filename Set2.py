my_set = {1, 2, 3, 4, 5}
my_set.add(6)
my_set.remove(3)
is_present = 4 in my_set
set_length = len(my_set)
another_set = {4, 5, 6, 7, 9}
union_set = my_set.union(another_set)
intersection_set = my_set.intersection(another_set)
difference_set = my_set.difference(another_set)
is_subset = my_set.issubset(another_set)
print("Is 4 Present:- ", is_present)
print("Set Length:- ", set_length)
print("Union Set:- ", union_set)
print("Intersection Set:- ", intersection_set)
print("Difference Set:- ", difference_set)
print("Is my_set a subset of another_set:- ", is_subset)
