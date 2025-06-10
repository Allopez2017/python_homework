def type_decorator(type_of_output):
    def decorator(func):
        def wrapper(*args, **kwargs):
            x = func(*args, **kwargs)
            return type_of_output(x)
        return wrapper
    return decorator

@type_decorator(str)
def return_integer():
    return

@type_decorator(int)
def return_string():
    return "not a number"

y = return_integer()
print(type(y)._name_)

try:
    y = return_string()
    print("An error occured")
except ValueError:
    print("Cannot convert string to integer")