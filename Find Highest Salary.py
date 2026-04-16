from collections import namedtuple
Employee = namedtuple('Employee', ['name', 'salary'])
emp_list = [Employee("Alice", 5000), Employee("Bob", 7000), Employee("Charlie", 6000)]
highest = max(emp_list, key=lambda e: e.salary)
print(highest.name)
