# Your Task: The Gumball Machine
# Let's build a classic Gumball Machine using the State Pattern.

# The Context (GumballMachine):
# Holds the states (e.g., NoQuarterState, HasQuarterState, SoldState).
# Has a count of gumballs.
# Has methods: insert_quarter(), eject_quarter(), turn_crank().

# The State Interface (State):
# Define the same methods: insert_quarter(), eject_quarter(), turn_crank().

# Concrete States:
# NoQuarterState: If you turn the crank, it says "You need to pay first."
# HasQuarterState: If you turn the crank, it transitions the machine to SoldState.
# SoldState: Dispenses a gumball, decreases count, and moves back to NoQuarterState (or OutOfGumballsState).

from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def insert_quarter(self) -> "State":
        pass

    @abstractmethod
    def eject_quarter(self) -> "State":
        pass

    @abstractmethod
    def turn_crank(self, machine: "GumballMachine") -> "State":
        pass


class NoQuarterState(State):
    def insert_quarter(self) -> State:
        return HasQuarterState()

    def eject_quarter(self) -> State:
        return self

    def turn_crank(self, machine: "GumballMachine") -> State:
        print("You need to pay first")
        return self

class HasQuarterState(State):
    def insert_quarter(self) -> State:
        return self

    def eject_quarter(self) -> State:
        return NoQuarterState()

    def turn_crank(self, machine: "GumballMachine") -> State:
        machine.state = SoldState()
        print("Quarter is their now turning the crank")
        return machine.state.turn_crank(machine)


class SoldState(State):
    def insert_quarter(self) -> State:
        return self

    def eject_quarter(self) -> State:
        return self

    def turn_crank(self, machine: "GumballMachine") -> State:
        count = machine.count
        if count > 0:
            print("Has gumballs")
            count = count - 1
            machine.count = count
            machine.state = NoQuarterState()
            return NoQuarterState()
        else:
            machine.state = OutOfGumballsState()
            return OutOfGumballsState()

class OutOfGumballsState(State):
    def insert_quarter(self) -> State:
        print("No Gumballs Left in the Machine")
        return self

    def eject_quarter(self) -> State:
        print("We refill the Gumball soon in the Machine. Thanks for visiting")
        return self

    def turn_crank(self, machine: "GumballMachine") -> State:
        print("No Gumballs Left in the Machine so can not give you anything")
        return self


class GumballMachine:
    def __init__(self, count: int) -> None:
        self.count : int = count
        self.state : State = NoQuarterState()

    def insert_quarter(self) -> None:
        self.state = self.state.insert_quarter()

    def eject_quarter(self) -> None:
        self.state = self.state.eject_quarter()

    def turn_crank(self) -> None:
        self.state = self.state.turn_crank(self)

my_machine = GumballMachine(count=3)

my_machine.turn_crank()
my_machine.insert_quarter()
my_machine.turn_crank()
my_machine.insert_quarter()
my_machine.turn_crank()

my_machine.insert_quarter()
my_machine.turn_crank()
my_machine.insert_quarter()
my_machine.turn_crank()
my_machine.insert_quarter()
my_machine.turn_crank()


