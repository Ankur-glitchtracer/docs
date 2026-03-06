# Think of it like a tree structure: you have "leaves" (the smallest units) and "branches"
# (containers that hold leaves or other branches). The magic is that the 
# client doesn't need to care if they are talking to a leaf or a branch;
# they just call a method, and it works for both.

# The Scenario: A File System
# Imagine we are building a tool to calculate the total size of a directory.

# File (Leaf): Has a name and a specific size.
# Directory (Composite): Has a name and contains a list of both Files and other Directories.

# Your Task: The Organization Chart
# Let's build a system to calculate the total salary of a department.

# 1. The Component (Entity):
# An abstract base class (or interface) with a method get_salary().

# 2. The Leaf (Employee):
# Represents a single person.
# Attributes: name and salary.
# get_salary() simply returns their salary.

# 3. The Composite (Department):
# Represents a collection of employees or sub-departments.
# Attributes: name and a list members.
# Has methods add(entity) and remove(entity).
# The Key: get_salary() must iterate through all members and sum up their salaries.

# Implementation Challenge
# Try to build this structure so that you can create a "Development" department with 5 developers,
# a "Design" department with 2 designers, and then wrap them both into a "Product" department.

# When you call product_dept.get_salary(), it should recursively calculate the total for the entire company.

from abc import ABC, abstractmethod

class Entity(ABC):
    @abstractmethod
    def get_salary(self) -> int:
        pass


class Employee(Entity):
    def __init__(self, name: str, salary: int) -> None:
        self.name : str = name
        self.salary : int = salary

    def get_salary(self) -> int:
        return self.salary


class Department(Entity):
    def __init__(self, name: str) -> None:
        self.name : str = name
        self.members : list[Entity] = []

    def add(self, entity: Entity) -> None:
        self.members.append(entity)

    def remove(self, entity: Entity) -> None:
        if entity in self.members:
            self.members.remove(entity)

    def get_salary(self) -> int:
        salary = 0
        for member in self.members:
            salary += member.get_salary()
        return salary

e1 = Employee(name="A", salary=2)
e2 = Employee(name="B", salary=4)

d1 = Department(name="D")
d1.add(entity=e1)

d2 = Department(name="E")
d2.add(entity=e2)
d2.add(entity=d1)

print(d2.get_salary())
