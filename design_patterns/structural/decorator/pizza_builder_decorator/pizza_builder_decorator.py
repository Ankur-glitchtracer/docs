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