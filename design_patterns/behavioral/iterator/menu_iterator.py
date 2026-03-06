# he Iterator Pattern lets you step through a complex data structure (like your nested Departments, a Linked List, or a Hash Map) 
# in a standard way (usually next() and has_next()) without the client needing to know how the data is stored.

# The Scenario: The Diner & Pancake House Merge
# Imagine two restaurants merge. One stores its menu items in a List, the other in a Dictionary.
# We want to create a Waitress who can print both menus using a single loop, without needing to write two different types of for loops.

class Dinner:
    def __init__(self) -> None:
        self.items : list[str] = []

    def get_items(self) -> list[str]:
        return self.items

    def add_item(self, item: str) -> None:
        self.items.append(item)

    def remove_item(self, item: str) -> None:
        if item in self.items:
            self.items.remove(item)


class Pancake:
    def __init__(self) -> None:
        self.dishes : dict[str, int] = {}

    def get_dishes(self) -> dict[str, int]:
        return self.dishes

    def add_dish(self, dish: str, price: int) -> None:
        self.dishes[dish] = price

    def delete_dish(self, dish: str) -> None:
        self.dishes.pop(dish, None)


class Merger:
    def __init__(self, dinner: Dinner, pancake: Pancake) -> None:
        self.dinner : Dinner = dinner
        self.item_count = dinner.items.__sizeof__()
        self.pancake : Pancake = pancake
        self.dish_count = pancake.dishes.__sizeof__()
        self.count : int = 0
        self.iter = iter(self.dinner.get_items())

    def has_next(self) -> bool:
        if self.count > self.item_count + self.dish_count:
            return False
        return True

    def next(self):
        self.count = self.count + 1
        try:
            next(self.iter)
        except:
            self.iter = iter(self.pancake.get_dishes())


class Waitress:
    def __init__(self, merger: Merger) -> None:
        self.merger : Merger = merger

    def menu(self) -> None:
        while self.merger.has_next():
            self.merger.next()

# Created Dinner object and add items
dinner = Dinner()
dinner.add_item("Grilled Chicken")
dinner.add_item("Caesar Salad")
dinner.add_item("Garlic Bread")
dinner.add_item("Chocolate Cake")

# Created Pancake object and add dishes with prices
pancake_menu = Pancake()
pancake_menu.add_dish("Classic Pancake", 5)
pancake_menu.add_dish("Blueberry Pancake", 7)
pancake_menu.add_dish("Chocolate Chip Pancake", 8)
pancake_menu.add_dish("Banana Walnut Pancake", 9)

merger = Merger(dinner=dinner, pancake=pancake_menu)

waitress = Waitress(merger=merger)

waitress.menu()
