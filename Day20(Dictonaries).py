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

############################ Dictionaries
cabinet = dict()
cabinet['summer'] = 12
cabinet['fall'] = 3
cabinet['spring'] = 75
print(cabinet)
print(cabinet['fall'])
cabinet['fall'] = cabinet['fall'] + 2
print(cabinet)

#  Comparing Lists and Dictonaries 
#  Dictionaries are like lists except that they use keys instead of numbers to look up values
lst = list()
lst.append(21)
lst.append(183)
print(lst)
lst[0] = 23
print(lst)

ddd = dict()
ddd['age']=21
ddd['course']=182
print(ddd)
ddd['age'] = 23
print(ddd)

#  Dictonary Literals (Constants)
#  Dictonary literals use curly braces and have a list of key : Value pairs
#  You can make an empty dictonary using empty curly braces

jjj = { 'chucks' : 1, 'fred' : 42, 'Jan' : 100}
print(jjj)
ooo = { }
print(ooo)


#  Some practice question on this topic
#  Basic 
#  Create and access a dictionary
student = {
    "name": "vivek",
    "age": "18",
    "branch": "CSE"
}
print(student)
print(student["name"])
print(student["age"])

# Add and update items
student = {"name":"Aman","age":19}
student["city"] = "Delhi"
student["age"] = "19"
print(student)

# Use dictionary Methods
student = {"name": "Riya", "age":19, "marks":87}
print(student.keys())
print(student.values())
print(student.items())
print(student.get("name"))

student.pop("age")
print(student)

# Loop through a dictionary
marks = {
    "Maths":90,
    "Python":82,
    "English":79
}
for subject, score in marks.items():
    print(subject, ":", score)

#  Logic Building codes
#  Count CHaracter frequency
text = "banana"
frequency = {}
for char in text:
    frequency[char] = frequency.get(char, 0) + 1
print(frequency)