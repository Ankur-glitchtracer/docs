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
