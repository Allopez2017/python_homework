#Task 2
import csv
def read_employees():
    key_value_pairs = {}
    rows = []
    try:
        with open("minutes.csv", "r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            header = next(csv_reader)
            key_value_pairs['fields'] = header

            for row in csv_reader:
                rows.append(row)
            key_value_pairs['rows'] = rows
    except FileNotFoundError:
        print("The file was not found")
    except Exception as e:
        print(f"An error has occured: {e}")
    return key_value_pairs

#Task 3
def column_list(column):
    if column in employees["fields"]:
        return employees["fields"].index(column)
    else:
        print (f"Column'{column}' not found")
        return -1
employees = read_employees()
employee_id_column = column_list("employee_id")

#Task 4
def first_name(row_number):
    first_name_list = column_list("first_name")
    if first_name_list == -1:
        return None
    row = employees["rows"][row_number]
    return row[first_name_list]

#Task 5
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches = list(filter(employee_match, employees["rows"]))
    return matches

#Task 6
def employee_find_2(employee_id):
    matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id, employees["rows"]))
    return matches

#Task 7
def sort_by_last_name():
    last_name_list = column_list("last name")
    employees["rows"].sort(key=lambda row: row[last_name_list])
    return employees["rows"]
sort_by_last_name()
print(employees)

#Task 8
def employee_dict(row):
    employee_data = {}
    for index, field in enumerate(employees["fields"]):
        if field != "employee_id":
            employee_data[field] = row[index]
    return employee_data

#Task 9
def all_employees_dict():
    all_employee_data = {}
    for row in employees["rows"]:
        employee_id = row[column_list("employee_id")]
        employee_data = employee_dict(row)
        all_employee_data[employee_id] = employee_data
    return all_employee_data
print(all_employees_dict)

#Task 10
import os
def get_this_value():
    return os.environ.get("THISVALUE")

#Task 11
import custom_module
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)
set_that_secret("new_secret_string")
print(custom_module.secret)

#Task 12
import csv
def read_minutes():
    minutes1 = {}
    minutes2 = {}
    try:
        with open('../csv/minutes1.csv', 'r') as file1:
            csv_reader = csv.reader(file1)
            header1 = next(csv_reader)
            minutes1["fields"] = header1
            rows1 = [tuple(row) for row in csv_reader]
            minutes1["rows"] = rows1
    except FileNotFoundError:
        print("The file '../csv/minutes1.csv' was not found")
    try:
        with open('../csv/minutes2.csv', 'r') as file2:
            csv_reader = csv.reader(file2)
            header2 = next(csv_reader)
            minutes2["fields"] = header2
            rows2 = [tuple(row) for row in csv_reader]
            minutes2["rows"] = rows2
    except FileNotFoundError:
        print("The file '../csv/minutes1.csv' was not found")
    return minutes1, minutes2

#Task 13
def create_minutes_set():
    minutes1, minutes2 = read_minutes()
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    union_set = set1.union(set2)
    return union_set

#Task 14
from datetime import datetime
def create_minutes_list():
    minutes_set = create_minutes_set()
    result_list = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_set))
    return result_list
minutes_list = create_minutes_list()
print(minutes_list)

#Task 15
def write_sorted_list():
    global minutes_list
    minutes_list_sorted = sorted(minutes_list, key=lambda x: x[1])
    minutes_list_converted = list(map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), minutes_list_sorted))
    try:
        with open('./minutes.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(minutes1["fields"])
            writer.writerows(minutes_list_converted)
    except Exception as e:
        print(f"Error while writing to CSV: {e}")
    return minutes_list_converted
write_sorted_list()
with open("./minutes.csv", "r") as file:
    file_content = file.read()
    print(file_content)