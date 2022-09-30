"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""


def frequencies(items):
    frequency = {}
    for j in items:   #iterate through the items
        j = str(j)    #convert values in items to a string 
        if j in frequency.keys(): #if the item is in the dictionary
            frequency[j] += 1 #increment the value 
        else:
            frequency[j] = 1 #if item is not in dictionary equal it to one
    return frequency


print(frequencies(['chocolate','chocolate','chocolate','3',3,3,3,2,2]))
