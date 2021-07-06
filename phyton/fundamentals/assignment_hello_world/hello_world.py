# 1. TASK: print "Hello World"
print("Hello World")

# 2. print "Hello Noelle!" with the name in a variable
# name = "Noelle"
# print( your code here )	# with a comma
# print( your code here )	# with a +

name = "Noelle"
print("My name is", name)
print("My name is " + name)

# # 3. print "Hello 42!" with the number in a variable
# name = 42
# print( your code here )	# with a comma
# print( your code here )	# with a +	-- this one should give us an error!

print("Hello 42")
name = "42"
print("Hello", name)
print("Hello " + name)

# # 4. print "I love to eat sushi and pizza." with the foods in variables
# fave_food1 = "sushi"
# fave_food2 = "pizza"
# print( your code here ) # with .format()
# print( your code here ) # with an f string

print("I love to eat sushi and pizza.")
fave_food1 = "sushi"
fave_food2 = "pizza"
print("I love to eat {} and {}.".format(fave_food1, fave_food2))
print(f"I love to eat {fave_food1} and {fave_food2}.")