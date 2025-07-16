#Task 1
def hello_function():
    return "Hello!"

print(hello_function())

#Task 2
def greet(name):
    return f"Hello, {name}!"

print (greet("Name"))

#Task 3
import random

operations_list = ["add", "subtract", "multiply", "divide", "int_divide", "modulo", "power"]
operation = random.choice(operations_list)

def calculate(a, b, operation):
    if type(a) != int or type(b) != int:
        return f"You can't {operation} those values!"
    elif operation == "divide" and b == 0:
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
    
print(calculate(5, 8, operation))

#Task 4
data_types = [float, str, int]
type = random.choice(data_types)

def data_type_conversion(value, type):
    try:
        return type(value)
    except Exception as e:
        print(f"You can't convert {value} into a {type}")

print(data_type_conversion("nonsense", type))

#Task 5
def find_avg(*args):
    grade = sum(args)/len(args)
    
    if grade >= 90:
        return "A"
    elif grade >= 80 and grade <= 89:
        return "B"
    elif grade >= 70 and grade <= 79:
        return "C"
    elif grade >= 60 and grade <= 69:
        return "D"
    else:
        return "F"

print(find_avg(58, 62, 93, 74, 85))  

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
        if i == 0 or i == len(string_list)-1:
            titleized_str += word.capitalize() + " "
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
        if word[0] == "q" and word[1] == "u":
            pig_latin_str += word[2:] + "quay" + " "
        elif word[0] in vowels:
            pig_latin_str += word + "ay" + " "
        else: 
            for i, letter in enumerate(word):
                if letter in vowels:
                    pig_latin_str += word[i:] + word[:i] + "ay" + " "
                    break
            
    return pig_latin_str

print(pig_latin("the quick brown fox"))