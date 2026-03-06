# DECORATOR SYSTEM DESIGN - Build your own Pizza shop
# The Problem: The "Build-Your-Own" Pizza Shop
# Imagine you are writing a point-of-sale system for a pizza parlor.

# Every pizza has a base description and a cost.

# Customers can add multiple toppings (extra cheese, pepperoni, mushrooms, olives, etc.).

# Some toppings might be added twice (double cheese).

# The price of the final pizza is the base price plus the sum of all toppings.

# The Challenge
# If you used standard inheritance, you would need classes like CheesePizza, CheesePepperoniPizza, MushroomOlivePizza, and so on. This is impossible to maintain.

# Your Implementation Task
# 1. Define the Interface: Create a Pizza interface (or abstract class) with two methods:

# getDescription(): returns a String.

# getCost(): returns a double.

# 2. Create a Concrete Component: Create a class PlainPizza that implements Pizza. It costs $10.00 and its description is "Thin crust dough".

# 3. Implement the Decorator: Create an abstract ToppingDecorator class that implements the Pizza interface and contains a reference to a Pizza object.

# 4. Create Concrete Decorators: Create classes like Cheese, Pepperoni, and Mushroom.

# Each of these should take a Pizza object in its constructor.

# getCost() should return the price of the current pizza + the cost of that specific topping.

# getDescription() should append the topping name to the existing description.

# Test Case
# Once you’ve built it, try to run this logic in your main method:

# // Start with a plain pizza
# Pizza myPizza = new PlainPizza(); 

# // Add cheese
# myPizza = new Cheese(myPizza);

# // Add pepperoni
# myPizza = new Pepperoni(myPizza);

# // Add double cheese!
# myPizza = new Cheese(myPizza);

# System.out.println("Order: " + myPizza.getDescription());
# System.out.println("Total Cost: $" + myPizza.getCost());
# Goal: Your output should dynamically chain the descriptions and sum up the costs without you ever having created a "DoubleCheesePepperoniPizza" class.



# from collections import defaultdict


# class Pizza:
#     def __init__(self) -> None:
#         self.description: str = ""
#         self.descriptions: dict[str, int] = defaultdict(int)
#         self.cost: float = 0.0

#     def getDescription(self) -> str:
#         desc = ""
#         for key, val in self.descriptions.items():
#             if val == 1:
#                 desc += key
#             else:
#                 desc += f"Double{key}"

#         desc += self.description
#         return desc

#     def setDescription(self, desc: str) -> None:
#         self.descriptions[desc] += 1

#     def getCost(self) -> float:
#         return self.cost

#     def setCost(self, cost: float) -> None:
#         self.cost += cost


# class PlainPizza(Pizza):
#     def __init__(self) -> None:
#         self.description: str = "Thin crust dough"
#         self.descriptions: dict[str, int] = defaultdict(int)
#         self.cost: float = 10.00

#     def getDescription(self) -> str:
#         return super().getDescription()

#     def setDescription(self, desc: str) -> None:
#         super().setDescription(desc=desc)

#     def getCost(self) -> float:
#         return super().getCost()

#     def setCost(self, cost: float) -> None:
#         super().setCost(cost=cost)


# class ToppingDecorator():
#     def __init__(self, pizza: Pizza) -> None:
#         self.description: str = pizza.getDescription()
#         self.cost: float = pizza.getCost()


# class Cheese(ToppingDecorator):
#     def __init__(self, pizza: Pizza) -> None:
#         pizza.setDescription(desc="Cheese")
#         pizza.setCost(cost=5)


# class Pepperoni(ToppingDecorator):
#     def __init__(self, pizza: Pizza) -> None:
#         pizza.setDescription(desc="Pepperoni")
#         pizza.setCost(cost=6)


# class Mushroom(ToppingDecorator):
#     def __init__(self, pizza: Pizza) -> None:
#         pizza.setDescription(desc="Mushroom")
#         pizza.setCost(cost=7)


# class Olive(ToppingDecorator):
#     def __init__(self, pizza: Pizza) -> None:
#         pizza.setDescription(desc="Olive")
#         pizza.setCost(cost=3)


# myPizza = PlainPizza()

# Cheese(pizza=myPizza)

# Mushroom(pizza=myPizza)

# Mushroom(pizza=myPizza)

# print(myPizza.getDescription())
# print(myPizza.getCost())


from abc import ABC, abstractmethod

class Pizza(ABC):
    @abstractmethod
    def getDescription(self) -> str:
        pass

    @abstractmethod
    def getCost(self) -> float:
        pass


class PlainPizza(Pizza):
    def getDescription(self) -> str:
        return "Thin crust dough"

    def getCost(self) -> float:
        return 10.00


class ToppingDecorator(Pizza):
    def __init__(self, pizza: Pizza) -> None:
        self.pizza = pizza
    
    def getDescription(self) -> str:
        return self.pizza.getDescription()
    
    def getCost(self) -> float:
        return self.pizza.getCost()


class Cheese(ToppingDecorator):
    def getDescription(self) -> str:
        return self.pizza.getDescription() + ", Cheese"
    
    def getCost(self) -> float:
        return self.pizza.getCost() + 5.00


class Pepperoni(ToppingDecorator):
    def getDescription(self) -> str:
        return self.pizza.getDescription() + ", Pepperoni"
    
    def getCost(self) -> float:
        return self.pizza.getCost() + 6.00


class Mushroom(ToppingDecorator):
    def getDescription(self) -> str:
        return self.pizza.getDescription() + ", Mushroom"
    
    def getCost(self) -> float:
        return self.pizza.getCost() + 7.00

class Olive(ToppingDecorator):
    def getDescription(self) -> str:
        return self.pizza.getDescription() + ", Olive"
    
    def getCost(self) -> float:
        return self.pizza.getCost() + 3.00

class DiscountDecorator(ToppingDecorator):
    def getDescription(self) -> str:
        return self.pizza.getDescription() + ", Discount Applied"
    
    def getCost(self) -> float:
        return self.pizza.getCost() * 0.9  # Apply a 10% discount    

# Test Case
if __name__ == "__main__":
    # Start with a plain pizza
    myPizza = PlainPizza()
    # Add cheese
    myPizza = Cheese(myPizza)
    # Add pepperoni
    myPizza = Pepperoni(myPizza)
    # Add double cheese!
    myPizza = Cheese(myPizza)

    myPizza = DiscountDecorator(myPizza)  # Apply discount
    print("Order: " + myPizza.getDescription())
    print("Total Cost: $" + str(myPizza.getCost()))