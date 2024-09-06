
# basic style 
print("Welcome to the Python tutorial !")
#===============================================================
# Multiple Arguments
product_name = "Python Programming tutorial"
price = 29.99
print("Product:", product_name, "Price:", price)
#===============================================================
# Custom Separator
fruits = ["apple", "banana", "orange"]
print("Fruits:", *fruits, sep=", ")
#===============================================================
# Custom End Character
for i in range(10):
    print("Progress:", i, end="\r")
#===============================================================
# Old-style formatting
order_id=1111
subject = "Order Confirmation: %d" % order_id
print(subject)
#===============================================================
# f-strings
name = "Ahmed"
age = 30
message = f"Happy {age}th Birthday, {name}!"
print(message)
#===============================================================
# Using the format() Method
pi = 3.14159265359
print("Pi to 3 decimal places: {:.3f}".format(pi))
#===============================================================
# Using the join() Method
colors = ["red", "green", "blue"]
sentence = "My favorite colors are: " + ", ".join(colors)
print(sentence)