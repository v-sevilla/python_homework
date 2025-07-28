#Task 1
def hello():
    return "Hello!"

print(hello())

#Task 2
def greet(name):
    return f"Hello, {name}!"

print (greet("Name"))

#Task 3
import random

operations_list = ["add", "subtract", "multiply", "divide", "int_divide", "modulo", "power"]
operation = random.choice(operations_list)

def calc(a, b, operation="multiply"):
    try:
        if operation == "divide" and b == 0:
            return f"You can't divide by 0!"
        elif operation == "add":
            return a+b
        elif operation == "subtract":
            return a-b
        elif operation == "multiply":
            return a*b
        elif operation == "divide":
            return a/b
        elif operation == "int_divide":
            return a//b
        elif operation == "modulo":
            return a%b
        elif operation == "power":
            return a**b
    except ZeroDivisionError:
        return f"You can't divide by 0!"
    except TypeError:
        return f"You can't multiply those values!"
    
print(calc(5, 8, operation))

#Task 4
data_types = [float, str, int]
data_type = random.choice(data_types)

def data_type_conversion(value, data_type):
    try:
        if data_type == "float":
            return float(value)
        elif data_type == "str":
            return str(value)
        elif data_type == "int":
            return int(value)
       
    except Exception:
        return(f"You can't convert {value} into a {data_type}.")
    
print(data_type_conversion("nonsense", float))

#Task 5
def grade(*args):
    
    try:
        average_score = sum(args)/len(args)
        
        if average_score >= 90:
            return "A"
        elif average_score >= 80 and average_score <= 89:
            return "B"
        elif average_score >= 70 and average_score <= 79:
            return "C"
        elif average_score >= 60 and average_score <= 69:
            return "D"
        else:
            return "F"

    except Exception:
       return (f"Invalid data was provided.")
print(grade(58, 62, 93, 74, 85))  

#Task 6
def repeat(str, count):
    new_str = ""
    for i in range(count):
        new_str += str
    return new_str

print(repeat("hello", 2))

#Task 7
positional_parameters = ["best", "mean"]
positional_parameter = random.choice(positional_parameters)

def student_scores(positional_parameter, **kwargs):
    if positional_parameter == "mean":
        return sum(kwargs.values())/len(kwargs)
    elif positional_parameter == "best":
        best_score = max(kwargs.values())
        for student, score in kwargs.items():
            if score == best_score:
                return student

print(student_scores(positional_parameter , John = 67, Lilo = 90, Eric = 78, Ella = 82))

#Task 8
exception_words = [ "a", "on", "an", "the", "of", "and", "is", "in"]

def titleize(str):
    string_list = str.split()
    titleized_str = ""

    for i, word in enumerate(string_list):
        if i == 0:
            titleized_str += word.capitalize() + " "
        elif i == len(string_list)-1:
            titleized_str += word.capitalize()
        elif word in exception_words:
            titleized_str += word + " "
        else:
            titleized_str += word.capitalize() + " "

    return titleized_str

print(titleize("a tale of two cities"))

#Task 9
def hangman(secret, guess):
    result = ""
    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"
    return result

print(hangman("difficulty", "ic"))

#Task 10
vowels = ["a", "e", "i", "o", "u"]

def pig_latin(str):
    pig_latin_str = ""
    split_str = str.split()

    for word in split_str:
        pig_latin_word = ""

        if word[0] in vowels:
            pig_latin_word = word + "ay"
        else:
            for i in range(len(word)):
                if word[i] == 'q' and word[i+1] == 'u':
                    pig_latin_word = word[i+2:] + word[:i+2] + "ay"
                    break
            else:
                for i, letter in enumerate(word):
                    if letter in vowels:
                        pig_latin_word = word[i:] + word[:i] + "ay"
                        break
                else:
                    pig_latin_word = word

        pig_latin_str += pig_latin_word + " "

    return pig_latin_str.strip()

print(pig_latin("the quick brown fox"))