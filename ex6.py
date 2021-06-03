types_of_people =10 #variable
x = f"There are {types_of_people} types of people." # string inside a string variable eaquals the format

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}." #string inside a string

print(x)
print(y)

print(f"I said: {x}") #string inside a string
print(f"I also said: '{y}'") #string inside a string

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
print(joke_evaluation.format(hilarious))

w= "This is the left side of..."
e = "a string with a right side."

print(w + e)
