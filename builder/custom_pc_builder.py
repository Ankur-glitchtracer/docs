# The Challenge: The "Custom PC" Builder
# To truly see the value of a Builder, let's avoid a simple "House" example and
# go with a Workstation Computer Configuration.

# A computer can have many optional parts: different CPUs, varying RAM sizes, 
# multiple storage drives, high-end GPUs, or even liquid cooling. 
# Using a standard __init__ would be a nightmare.

# Your Implementation Checklist
# To implement this properly in Python, try to include these three components:

# The Product: The complex Computer object.

# The Builder Interface: An abstract base class (using the abc module) defining the steps to build the computer (e.g., add_memory(), add_gpu()).

# The Director: A class that takes a builder and executes a specific "recipe" (e.g., a GamingPCMenu or OfficePCMenu).

# A Quick Tip for Pythonic Builders
# While the "Gang of Four" (GoF) approach uses a Director, many Python developers use Fluent Interfaces. This allows you to chain methods like this: my_pc = ComputerBuilder().add_cpu("M3 Max").add_ram(64).build()

# Pro-level Refinement
# Once you have the basic version working, try to implement Validation inside your build() method. For example:
# Ensure a computer cannot be built without a CPU.
# Check if the Power Supply (PSU) is strong enough for the chosen GPU.

# This is where the Builder pattern shines—it ensures that by the time the object is "born," it is guaranteed to be in a valid state.
from abc import ABC, abstractmethod


class Computer:
    def __init__(self) -> None:
        self.cpu : str | None = None
        self.memory : str | None = None
        self.gpu : str | None = None
        self.psu : str | None = None


class Builder(ABC):
    def __init__(self):
        self.computer : Computer = Computer()

    @abstractmethod
    def add_cpu(self, cpu: str) -> Builder:
        pass

    @abstractmethod
    def add_memory(self, memory: str) -> Builder:
        pass

    @abstractmethod
    def add_gpu(self, gpu: str) -> Builder:
        pass

    @abstractmethod
    def add_psu(self, psu: str) -> Builder:
        pass

    @abstractmethod
    def build(self) -> Computer:
        pass


class GamingPCMenu(Builder):
    def add_cpu(self, cpu: str) -> Builder:
        self.computer.cpu = cpu
        return self

    def add_memory(self, memory: str) -> Builder:
        self.computer.memory = memory
        return self

    def add_gpu(self, gpu: str) -> Builder:
        self.computer.gpu = gpu
        return self

    def add_psu(self, psu: str) -> Builder:
        self.computer.psu = psu
        return self

    def build(self) -> Computer:
        print(f"Gaming PC has cpu: {self.computer.cpu}, memory: {self.computer.memory}, gpu: {self.computer.gpu}, psu: {self.computer.psu}")
        computer = self.computer
        self.computer = Computer()
        return computer

# Goal usage:
my_builder = GamingPCMenu()
pc = my_builder.add_cpu("Intel i9").add_gpu("RTX 4090").build()

