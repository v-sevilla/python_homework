#Task 1: Writing and Testing a Decorator
import logging

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        if args:
            positional_argument = list(args)
        else:
            positional_argument = "none"
    
        if kwargs:
            keyword_parameter = dict(kwargs)
        else:
            keyword_parameter = "none"
    
        result = func(*args, **kwargs)

        log_message = (f"function: {func.__name__} "
               f"positional parameters: {positional_argument} "
               f"keyword parameters: {keyword_parameter} "
               f"return: {result}")
        logger.log(logging.INFO, log_message)

        return result
    return wrapper

@logger_decorator
def hello_world():
    print("Hello, World!")

@logger_decorator
def random_num_positional_arguments(*args):
    return True

@logger_decorator
def random_num_keyword_arguments(**kwargs):
    return logger_decorator

hello_world()
random_num_positional_arguments(1, "b", "test")
random_num_keyword_arguments(name="Luna", age=7, animal="Dog")