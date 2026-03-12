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
