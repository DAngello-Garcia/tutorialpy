#“We use the “wildcard” or “*” notation like this – *args OR **kwargs – as our function’s argument when we have doubts about the number of  arguments we should pass in a function.”

def multiply(*args):
    result = 1
    for i in args:
        result *= i
    return result

print(multiply(5,6,2))

def add(*num):
    result = 0
    for i in num:
        result += i
    return result

print(add(2,5,8,15,-7))

#Note that in the example the iterable object is a standard dict. If you iterate over the dictionary and want to return its values, like in the example shown, then you must use .values().

def concatenate(**words):
    result = ""
    for arg in words.values():
        result += arg
    return result

print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))

#In fact, if you forget to use this method, you will find yourself iterating through the keys of your Python kwargs dictionary instead
def concatenate(**kwargs):
    result = ""
    # Iterating over the keys of the Python kwargs dictionary
    for arg in kwargs:
        result += arg
    return result

print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))

# correct_function_definition.py
def my_function(a, b, *args, **kwargs):
    pass

# We can unpack With the Asterisk Operators: * & **
# print_list
my_list = [1, 2, 3]
print(my_list)
# print_unpacked_list
my_list = [1, 2, 3]
print(*my_list)
