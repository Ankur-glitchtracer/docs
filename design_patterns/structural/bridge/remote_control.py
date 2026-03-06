# BRIDGE DESIGN PATTERN
# The Problem: The "Class Explosion"
# Imagine you have a Shape class with subclasses Circle and Square. Now you want to add colors: Red and Blue. If you use standard inheritance, you end up with:

# RedCircle, BlueCircle, RedSquare, BlueSquare...

# If you add a Triangle, you need 2 more classes. If you add Green, you need 3 more. This is a Cartesian Product nightmare.

# The Solution: The Bridge
# The Bridge pattern says: "Prefer Composition over Inheritance." You split the concept into two independent hierarchies:
# The Abstraction: (The "Entity" like Shape)
# The Implementation: (The "Platform" or "Trait" like Color)

# By "bridging" them, a Shape has a Color instead of being a RedCircle.

# Your Task: The Remote Control & Device
# We are going to build a system where Remote Controls (Abstraction) operate Devices (Implementation).
# 1. The Implementation (The "Platform"):
# Create an interface Device with methods: is_enabled(), enable(), disable(), and set_volume(percent).
# Create concrete classes TV and Radio.

# 2. The Abstraction (The "Interface"):
# Create a class RemoteControl. It should take a Device in its __init__.
# Add a method toggle_power() that checks is_enabled() and calls enable() or disable() accordingly.
# Add volume_up() which calls set_volume().

# 3. The Refined Abstraction (The "Evolution"):
# Create AdvancedRemoteControl that inherits from RemoteControl.
# Add a new method mute() that sets the device volume to 0.

# Can you implement this so that an AdvancedRemoteControl can work with both a TV and a Radio without changing any code in the Radio class?
# from abc import ABC, abstractmethod

class Device:
    def __init__(self) -> None:
        self.volume : int = 10
        self.status : bool = False

    def is_enabled(self) -> bool:
        return self.status

    def enable(self) -> None:
        self.status = True

    def disable(self) -> None:
        self.status = False

    def set_volume(self, volume: int) -> None:
        self.volume = volume
        print(f"The Volume is set to {self.volume}")

    def get_volume(self) -> int:
        return self.volume


class RemoteControl:
    def __init__(self, device: Device) -> None:
        self.device : Device = device

    def toggle_power(self) -> None:
        if self.device.is_enabled():
            print("The Power was ON. Toggling it!")
            self.device.disable()
        else:
            print("The Power was OFF. Togging it!")
            self.device.enable()

    def volume_up(self) -> None:
        current = self.device.get_volume()
        self.device.set_volume(current + 1)


class AdvanceRemoteControl(RemoteControl):
    def mute(self):
        self.device.set_volume(0)
        print("The Volume is now Mute")


my_device = Device()

my_remote = AdvanceRemoteControl(my_device)

my_remote.toggle_power()

my_remote.volume_up()
my_remote.volume_up()
my_remote.volume_up()

my_remote.mute()

my_remote.volume_up()
my_remote.volume_up()

