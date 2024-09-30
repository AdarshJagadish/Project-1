s={1,2,3,5,4,9,7,} 
s.add(10)                                            # to add a single element to the set
s.update({11,12,15,16})                              # To add multiple values , similar like append in list
s.pop()                                              # To remove a random element from the set
s.remove(5)                                          # To remove a specific element, if the return element is not in the set it consider as error
s.discard(7)                                         # To remove specific element,if the given element is not in set it will not consider as error
s.difference({9,4,7,8,0})                            # Remove union set from the original set
s.difference_update({9,4,7,8,0})                     # Remove union set and update it to the original set
s.intersection({2,0,11,20})                          # Shows the common elements only
s.intersection_update({2,0,11,20})                   # Shows the common elements only
s.symmetric_difference({1,2,3,4,9,6,1,})             # returns the elements not common in both sets
s.symmetric_difference_update({1,2,3,4,9,6,1,})      # returns the elements not common in both sets and save
s.union({0,1,2,3,15,16,33})                          # Shows every elements from both sets without duplication
s.copy()                                             # Return a copy of the set
s.clear()                                            # clear every elements from the set,returns an empty set
print(s)