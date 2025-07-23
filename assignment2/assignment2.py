#Task 2: Read a CSV File
import csv
import traceback

def read_employees():
    employee_data = {}
    employee_rows = []

    try:
        with open("../csv/employees.csv", newline="") as file:
            reader = csv.reader(file)

            for i, employee_row in enumerate(reader):
                if i == 0:
                    employee_data["fields"] = employee_row
                else:
                    employee_rows.append(employee_row)

        employee_data["rows"] = employee_rows
        return employee_data
    
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")

employees = read_employees()
print(employees)

#Task 3: Find the Column Index
def column_index(column_header_name):
    return employees["fields"].index(column_header_name)

employee_id_column = column_index("employee_id")

#Task 4: Find the Employee First Name
def first_name(row_number):
    column_header = column_index("first_name")
    return employees["rows"][row_number][column_header]

#Task 5: Find the Employee
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id

    matches = list(filter(employee_match, employees["rows"]))

    return matches

#Task 6: Find Employee with Lambda
def employee_find_2(employee_id):
    matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))

    return matches

#Task 7: Sort Rows by last_name using Lambda
def sort_by_last_name():
    employees["rows"].sort(key=lambda row: row[column_index("last_name")])

    return employees["rows"]

#Task 8: Create a dict for an Employee
def employee_dict(row):
    dict_result = {}
    fields = employees["fields"]
    
    for i, field_name in enumerate(fields):
        if field_name != "employee_id":
            dict_result[field_name] = row[i]
    
    return dict_result

get_employee_dict = employee_dict(["rows"][0])

print(get_employee_dict)

#Task 9: Dict for all Employees
def all_employees_dict():
    resulting_dict = {}
    employee_id_column = column_index("employee_id")
    
    for row in employees["rows"]:
        employee_id = row[employee_id_column]
        employee_data = employee_dict(row)
        resulting_dict[employee_id] = employee_data
    
    return resulting_dict

get_all_employees_dict = all_employees_dict()

print(get_all_employees_dict)

#Task 10: Use the os Module
import os

def get_this_value():
    return os.getenv("THISVALUE")

#Task 11: Create your own Module
import custom_module

def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret("badpassword")

print(custom_module.secret)

#Task 12: 
def read_csv(filename):
    minutes_data = {}
    minutes_rows = []

    try:
        with open(filename, newline="") as file:
            reader = csv.reader(file)

            for i, minutes_row in enumerate(reader):
                if i == 0:
                    minutes_data["fields"] = minutes_row
                else:
                    minutes_rows.append(tuple(minutes_row))

        minutes_data["rows"] = minutes_rows
        return minutes_data
    
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")

def read_minutes():
    minutes1 = read_csv("../csv/minutes1.csv")
    minutes2 = read_csv("../csv/minutes2.csv")
    
    return minutes1, minutes2

minutes1, minutes2 = read_minutes()

print(minutes1)
print(minutes2)

#Task 13: Create minutes_set
def create_minutes_set():
    minutes_1_set = set(minutes1["rows"])
    minutes_2_set = set(minutes2["rows"])
    combined_minute_sets = minutes_1_set.union(minutes_2_set)

    return combined_minute_sets

minutes_set = create_minutes_set()

#Task 14: Convert to datetime
from datetime import datetime

def create_minutes_list():
    minutes_list_set = list(minutes_set)
    converted_list = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list_set))

    return converted_list

minutes_list = create_minutes_list()

#Task 15: Write out Sorted List
def write_sorted_list():
    sort_by_date = sorted(minutes_list, key=lambda x: x[1])
    datetime_to_str = list(map(lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")), sort_by_date))

    with open('./minutes.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(minutes1["fields"])
        
        for row in datetime_to_str:
            writer.writerow(row)

    return datetime_to_str