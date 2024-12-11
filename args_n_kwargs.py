""" variable number functions with args and kwargs """
# 1. *args Variable Positional Arguments

# => *args allows a function to accept any number of positional arguments as a tuple.
# => Useful when you don't know in advance how many positional arguments will be passed.

def greet(*args):
    """ args implementation """
    for name in args:
        print(f"Hello, {name}!")

greet("Alice", "Bob", "Charlie")

# Output
# Hello, Alice!
# Hello, Bob!
# Hello, Charlie!

# Explanation:

# *args collects "Alice", "Bob", and "Charlie" into a tuple ("Alice", "Bob", "Charlie").
# The function iterates over the tuple and prints a greeting for each name.

# ------------------------------------------------------------------------------------------------

# 2. **kwargs (Variable Keyword Arguments)
# => **kwargs allows a function to accept any number of keyword arguments as a dictionary.
# => Useful for passing a flexible number of named arguments.

def display_info(**kwargs):
    """ **kwargs implementation """
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Alice", age=25, city="Nairobi")

# Output
# name: Alice
# age: 25
# city: Nairobi

# Explanation:

# **kwargs collects the keyword arguments name="Alice", age=25, and city="Nairobi" into a dictionary: {'name': 'Alice', 'age': 25, 'city': 'Nairobi'}.
# The function iterates over the dictionary and displays the key-value pairs.

# ------------------------------------------------------------------------------------------------

# 3. Using Both *args and **kwargs Together
# You can use *args and **kwargs in the same function to handle both positional and keyword arguments.

# Example:
def show_details(*args, **kwargs):
    ''' using both args and kwargs '''
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

show_details("Alice", "Bob", age=30, city="Nairobi")

# Output:

# Positional arguments: ('Alice', 'Bob')
# Keyword arguments: {'age': 30, 'city': 'Nairobi'}

# Explanation:

# Positional arguments "Alice" and "Bob" are collected into the tuple args.
# Keyword arguments age=30 and city="Nairobi" are collected into the dictionary kwargs.

# ------------------------------------------------------------------------------------------------

# 4. Using *args and **kwargs with Other Parameters
# You can mix *args and **kwargs with regular parameters, but their order matters:

# 1. Regular arguments
# 2. *args
# 3. Keyword-only arguments (optional)
# 4. **kwargs

# Example:

def person_details(greetings, *args, age=None, **kwargs):
    ''' Using *args and **kwargs with Other Parameters '''
    print(greetings)
    print("Names:", args)
    print("Age:", age)
    print("Additional Info:", kwargs)

person_details(
    "Hello!",
    "Job", "Muli",
    age=30,
    city="  Nairobi",
    profession="Software Engineer"
)

# Output

# Hello!
# Names: ('Job', 'Muli')
# Age: 30
# Additional Info: {'city': '  Nairobi', 'profession': 'Software Engineer'}

# Explanation:

# greeting captures "Hello!".
# *args collects "Job" and "Muli".
# age captures 30 (explicit keyword-only argument).
# **kwargs collects city="Nairobi" and profession="Software Engineer".

# ------------------------------------------------------------------------------------------------

# 5. Unpacking with *args and **kwargs
# You can also unpack arguments into a function using * and **.

# Example 1: Unpacking with *args

def add(a, b, c):
    ''' Unpacking with *args '''
    return a + b + c

numbers = [1, 2, 3]
print(add(*numbers))  # Unpacks the list into 3 arguments

# Output:

# 6

# Example 2: Unpacking with **kwargs

def introduce(name, age, city):
    ''' Unpacking with **kwargs '''
    return f"My name is {name}, I am {age} years old, and I live in {city}."

info = {"name": "Alice", "age": 25, "city": "Nairobi"}
print(introduce(**info))  # Unpacks the dictionary into named arguments

# Output

# My name is Alice, I am 25 years old, and I live in Nairobi.

# ------------------------------------------------------------------------------------------------

# 6. Common Use Cases
# Flexible APIs: Functions or methods with many optional parameters.
# Wrapper Functions: Writing decorators or functions that pass arguments dynamically.

# Example of a Decorator:

def decorator(func):
    ''' Writing decorators '''
    def wrapper(*args, **kwargs):
        print("Before the function call")
        result = func(*args, **kwargs)
        print("After the function call")
        return result
    return wrapper

@decorator
def greeting(name):
    ''' greet decorator implementation '''
    print(f"Hello, {name}!")

greeting("Alice")

# Output

# Before the function call
# Hello, Alice!
# After the function call


# Key Points:
# => Use *args for arbitrary positional arguments.
# => Use **kwargs for arbitrary keyword arguments.
# => Combine them with regular parameters for flexible function signatures.
# => Leverage unpacking to pass arguments dynamically.
