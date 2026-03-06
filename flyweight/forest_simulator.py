# # The FLYWEIGHT DESIGN PATTERN
# The Flyweight pattern is all about optimization.
# It’s the pattern you reach for when your application is running out of RAM
# because you have thousands (or millions) of similar objects.

# The Core Concept: Intrinsic vs. Extrinsic State
# The trick to Flyweight is splitting an object's data into two parts:

# Intrinsic State: Data that is constant across many objects
# (e.g., the texture/image of a tree in a video game). This is stored in the "Flyweight" object.

# Extrinsic State: Data that is unique to each instance
# (e.g., the X, Y coordinates of that specific tree). This is passed in from the outside.

# Your Task: The Forest Simulator
# Imagine we are building a game like Minecraft. We want to render 1,000,000 trees,
# but we don't want to create 1,000,000 copies of the heavy "Tree Sprite" data.

# 1. The Flyweight (TreeType):
# This class contains the "heavy" shared data: name, color, and texture_data (you can just use a long string for this).
# It should have a method draw(x, y) that prints: "Drawing a {color} {name} at ({x}, {y})".

# 2. The Flyweight Factory (TreeFactory):
# This is the "manager." It keeps a dictionary (cache) of TreeType objects.
# It should have a method get_tree_type(name, color, texture_data).
# If the type exists, return it; if not, create it, store it, and then return it.

# 3. The Context (Tree):
# This is the "lightweight" object. It only stores the unique data: x, y, and a reference to a TreeType.

# 4. The Client (Forest):
# Has a list of Tree objects.
# Has a method plant_tree(x, y, name, color, texture_data) that uses the factory to get a type and adds a new tree to the list.

# Try implementing this! After you write it,
# print the memory address (id()) of the TreeType objects
# within your trees to prove that 1,000 "Oak" trees are all sharing the exact same type instance.

from dataclasses import dataclass

@dataclass(frozen=True)
class TreeType:
    name : str
    color : str
    texture_data : str

    def draw(self, x: int, y: int) -> None:
        print(f"Drawing a {self.color} {self.name} at ({x}, {y})")


class TreeFactory:
    def __init__(self) -> None:
        self.tree_types : dict[tuple[str, str, str], TreeType] = {}

    def get_tree_type(self, name: str, color: str, texture_data: str) -> TreeType:
        key = (name, color, texture_data)
        if key in self.tree_types:
            return self.tree_types[key]

        tree_type = TreeType(name, color, texture_data)
        self.tree_types[key] = tree_type
        return tree_type


class Tree:
    def __init__(self, x: int, y: int, tree_type: TreeType) -> None:
        self.x : int = x
        self.y : int = y
        self.tree_type : TreeType = tree_type

    def draw(self) -> None:
        self.tree_type.draw(x=self.x, y=self.y)


class Forest:
    def __init__(self, tree_factory: TreeFactory) -> None:
        self.tree_factory : TreeFactory = tree_factory
        self.trees : list[Tree] = []

    def plant_tree(self, x: int, y: int, name: str, color: str, texture_data: str) -> None:
        tree_type = self.tree_factory.get_tree_type(name, color, texture_data)
        print(id(tree_type))
        tree = Tree(x, y, tree_type)
        self.trees.append(tree)

my_flyweight = TreeFactory()
my_simulation = Forest(tree_factory=my_flyweight)

my_simulation.plant_tree(x=1, y=2, name="Oak", color="Brown", texture_data="lorem lipsum")
my_simulation.plant_tree(x=2, y=2, name="Oak", color="Brown", texture_data="lorem lipsum")
my_simulation.plant_tree(x=3, y=2, name="Oak", color="Brown", texture_data="lorem lipsum")
my_simulation.plant_tree(x=4, y=2, name="Oak", color="Brown", texture_data="lorem lipsum")
my_simulation.plant_tree(x=5, y=2, name="Oak", color="Brown", texture_data="lorem lipsum")
my_simulation.plant_tree(x=6, y=2, name="Oak", color="Brown", texture_data="lorem lipsum")
my_simulation.plant_tree(x=7, y=2, name="Oak", color="Brown", texture_data="lorem lipsum")
my_simulation.plant_tree(x=8, y=2, name="Oak", color="Brown", texture_data="lorem lipsum")
my_simulation.plant_tree(x=9, y=2, name="Oak", color="Brown", texture_data="lorem lipsum")
my_simulation.plant_tree(x=1, y=3, name="Oak", color="Brown", texture_data="lorem lipsum")
my_simulation.plant_tree(x=1, y=4, name="Oak", color="Brown", texture_data="lorem lipsum")
my_simulation.plant_tree(x=1, y=5, name="Oak", color="Brown", texture_data="lorem lipsum")
my_simulation.plant_tree(x=1, y=6, name="Oak", color="Brown", texture_data="lorem lipsum")
my_simulation.plant_tree(x=1, y=7, name="Oak", color="Brown", texture_data="lorem lipsum")

print("\n--- Drawing all trees ---")
for tree in my_simulation.trees:
    tree.draw()

print("\n--- Verifying shared TreeType instances ---")
tree_type_ids = {id(tree.tree_type) for tree in my_simulation.trees}
print(f"Unique TreeType instances: {len(tree_type_ids)}")
print(f"TreeType ids: {tree_type_ids}")

# print("\n--- Attempting to mutate frozen TreeType (should fail) ---")
# try:
#     first_tree = my_simulation.trees[0]
#     first_tree.tree_type.color = "Green"  # ❌ should raise
# except Exception as e:
#     print(type(e).__name__, ":", e)
