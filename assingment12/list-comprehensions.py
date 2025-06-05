import pandas as pd

df = pd.read_csv("../csv/employees.csv")
employee_names = [row[1]["first_name"] + " " + row[1]["last_name"] for row in df.iterrows()]
print(employee_names)

e_names = [name for name in employee_names if "e" in name]
print(e_names)