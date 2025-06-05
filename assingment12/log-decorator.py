import logging
logger = logging.getLogger(_name_ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))

def log_decorator(func):
    def wrapper(*args, **kwargs):
        logger.log(logging.INFO, f"function: {func._name_}")
        if args:
            arg_parameter = args
        else:
            arg_parameter = "none"
        logger.log(logging.INFO, f"positional parameters: {arg_parameter}")
        if kwargs:
            kwargs_parameter = kwargs
        else:
            kwargs_parameter = "none"
        logger.log(logging.INFO, f"keyword parameters: {kwargs_parameter}")
        result = func(*args, **kwargs)
        logger.log(logging.INFO, f"return: {result}")
        return result
    return wrapper

@log_decorator
def hello_world():
    print("Hello, World!")

@log_decorator
def positional_args(*args):
    return True

@log_decorator
def keyword_args(**kwargs):
    return log_decorator

hello_world()
positional_args("Hello", "World")
keyword_args(first="Hello", second="World")
