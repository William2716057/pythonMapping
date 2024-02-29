
#square of numbers
numbers = [1,2,3,4,5,6,7,8,9]
squared = list(map(lambda x: x**2, numbers))
print(squared)

#string lengths
words = ["foot", "house","grass", "smoke", "fish", "lamp", "elephant", "telephone"]
lengths = list(map(len, words))
print(lengths)

#capitalise
names = ["steve", "ken", "jim", "stan", "mike", "bob", "frank"]
capitalised = list(map(str.capitalize, names))
print(capitalised)

#celsius to Fahrenheit 
celsius = [0, 15, 72, -4, 20]
fahrenheit = list(map(lambda x: (9/5) * x + 32, celsius))
print(fahrenheit)

#check odd or even 
numbers2 = [1,3,4,5,7]
print(numbers2)
evenOdd = list(map(lambda x: "Even" if x % 2 == 0 else "odd", numbers2))
print(evenOdd)