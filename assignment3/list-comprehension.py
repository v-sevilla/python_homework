#Task 3: List Comprehensions Practice
import csv

def read_employees():   
    with open("../csv/employees.csv", newline="") as file:         
        reader = csv.reader(file)
        employees_data = list(reader)
        names_with_e = []

        employee_names = [row[1] + " " + row[2] for row in employees_data[1:]]     
        print("Full names:", employee_names)  

        for name in employee_names:
            if 'e' in name:
                names_with_e.append(name)
        print("Names containing 'e':", names_with_e)
        
read_employees()