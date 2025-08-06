import pandas as pd

#Task 1: Introduction to Pandas - Creating and Manipulating DataFrames

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

task1_data_frame = pd.DataFrame(data)
print(task1_data_frame)


task1_with_salary = task1_data_frame.copy()
salary = [70000, 80000, 90000]
task1_with_salary['Salary'] = salary
print(task1_with_salary)


task1_older = task1_with_salary.copy()
age_series = task1_older['Age'] +1
task1_older['Age'] = age_series
print(task1_older)

task1_older.to_csv("employees.csv", index=False)


#Task 2: Loading Data from CSV and JSON

task2_employees = pd.read_csv('employees.csv')
json_employees = pd.read_json('additional_employees.json')
print(json_employees)

more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)


#Task 3: Data Inspection - Using Head, Tail, and Info Methods

first_three = more_employees.head(3)
print(first_three)

last_two = more_employees.tail(2)
print(last_two)

employee_shape = more_employees.shape
print(employee_shape)

print (more_employees.info())


#Task 4: Data Cleanin
dirty_data = pd.read_csv('dirty_data.csv')
clean_data = dirty_data.copy()
print(clean_data)

#Remove duplicate rows from DataFrame
clean_data = clean_data.drop(6)
print(clean_data)

#Replace placeholders with NaN and convert to numeric
clean_data["Age"] = pd.to_numeric(clean_data["Age"], errors="coerce")
print(clean_data)

#Convert Salary to numeric and replace known placeholders (unknown, n/a) with NaN
clean_data["Salary"] = pd.to_numeric(clean_data["Salary"], errors="coerce")
print(clean_data)

#Fill missing numeric values (use fillna).  Fill Age which the mean and Salary with the median
mean_age = clean_data["Age"].mean()
clean_data["Age"] = clean_data["Age"].fillna(mean_age)

median_salary = clean_data["Salary"].median()
clean_data["Salary"] = clean_data["Salary"].fillna(median_salary)
print(clean_data)

#Convert Hire Date to datetime
clean_data["Hire Date"] = pd.to_datetime(clean_data["Hire Date"], format="mixed", errors="coerce")
print(clean_data)

#Strip extra whitespace and standardize Name and Department as uppercase
clean_data["Name"] = clean_data["Name"].str.upper()
clean_data["Department"] = clean_data["Department"].str.upper()

clean_data["Name"] = clean_data["Name"].str.strip()
clean_data["Department"] = clean_data["Department"].str.strip()

print(clean_data)
