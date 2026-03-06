# Abstract Factory.

# The Problem: Consistent UI Themes
# While the Factory Method is great for creating one type of object (a Document), 
# the Abstract Factory is designed to create families of related or dependent objects.

# Imagine you are building a cross-platform UI toolkit.
# If the user is on Windows, every element (Buttons, Checkboxes, Sliders) must look like Windows.
# If the user is on Mac, every element must look like Mac.

# The Constraint: You must never mix them. You don't want a Mac Button appearing inside a Windows-themed app.

# Your Implementation Task
# 1. The Products (Interfaces):
# Create a Button interface with a render() method.
# Create a Checkbox interface with a render() method.

# 2. Concrete Products (Windows):
# WindowsButton (returns "Rendering Windows Button")
# WindowsCheckbox (returns "Rendering Windows Checkbox")

# 3. Concrete Products (Mac):
# MacButton (returns "Rendering Mac Button")
# MacCheckbox (returns "Rendering Mac Checkbox")

# 4. The Abstract Factory (The Interface): Create a UIFactory interface with two methods:
# create_button() -> Button
# create_checkbox() -> Checkbox

# 5. Concrete Factories:
# Create a WindowsFactory that returns Windows products.
# Create a MacFactory that returns Mac products.

# The Goal
# Your client code should look like this:
# def start_app(factory: UIFactory):
#     button = factory.create_button()
#     checkbox = factory.create_checkbox()
#     print(button.render())
#     print(checkbox.render())

# # To switch the entire UI theme, I only change this one line:
# current_factory = WindowsFactory() 
# start_app(current_factory)

from abc import ABC, abstractmethod

class Product(ABC):
    @abstractmethod
    def render(self) -> str:
        pass


class Button(Product):
    @abstractmethod
    def render(self) -> str:
        pass

class Checkbox(Product):
    @abstractmethod
    def render(self) -> str:
        pass

class Slider(Product):
    @abstractmethod
    def render(self) -> str:
        pass

# Windows Products
class WindowsButton(Button):
    def render(self) -> str:
        return "Rendering Windows Button"


class WindowsCheckbox(Checkbox):
    def render(self) -> str:
        return "Rendering Windows Checkbox"


class WindowsSlider(Slider):
    def render(self) -> str:
        return "Rendering Windows Slider"

# Mac Products
class MacButton(Button):
    def render(self) -> str:
        return "Rendering Mac Button"


class MacCheckbox(Checkbox):
    def render(self) -> str:
        return "Rendering Mac Checkbox"


class MacSlider(Slider):
    def render(self) -> str:
        return "Rendering Mac Slider"

# Abstract Factory
class UIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass

    @abstractmethod
    def create_slider(self) -> Slider:
        pass


class WindowsFactory(UIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()

    def create_slider(self) -> Slider:
        return WindowsSlider()


class MacFactory(UIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()

    def create_slider(self) -> Slider:
        return MacSlider()

def start_app(factory: UIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    print(button.render())
    print(checkbox.render())

# To switch the entire UI theme, I only change this one line:
current_factory = WindowsFactory() 
start_app(current_factory)
