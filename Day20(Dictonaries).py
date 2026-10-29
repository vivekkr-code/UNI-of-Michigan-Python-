############################        Dictionaries        ##########################

#  What is a collection?
# A collection is nice because we can put more than one value in it and carry them all around in one convenient package
# We have a bunch of values in a single "Variable"

#  What is not a collection? 
#  Most of our variables have one value in them, when we put a new value in the variable, the old value is overwritten
x = 2
x = 4
print(x)

#  List   vs   Dictonaries
#  List - A linear collection of values Lookup by position 0.. length-1
#  Dictionary - A linear collection of key-value pairs lookup by "tag" or "key"

###############      Dictionaries 
# It is pythons most powerful data collection.
# It allows us to do fast database like operations in Python.

##############################  Lists Review
# We append values to the end of the list and look them up by position

cards = list()
cards.append(12)
cards.append(3)
cards.append(75)
print(cards)
print(cards[1])
cards[1] = cards[1] + 2
print(cards)


