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
