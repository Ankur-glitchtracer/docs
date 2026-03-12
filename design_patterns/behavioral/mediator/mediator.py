from abc import ABC, abstractmethod
from typing import List, Optional

# Mediator Interface
class ATCMediator(ABC):
    @abstractmethod
    def request_landing(self, aircraft: 'Aircraft') -> bool:
        pass

    @abstractmethod
    def request_takeoff(self, aircraft: 'Aircraft') -> bool:
        pass

    @abstractmethod
    def notify_runway_clear(self, aircraft: 'Aircraft') -> None:
        pass

# Colleague Interface
class Aircraft(ABC):
    def __init__(self, call_sign: str, mediator: ATCMediator):
        self.call_sign = call_sign
        self.mediator = mediator

    @abstractmethod
    def land(self) -> None:
        pass

    @abstractmethod
    def take_off(self) -> None:
        pass

# Concrete Mediator
class ATC(ATCMediator):
    def __init__(self):
        self.runway_occupied = False
        self.queue: List[Aircraft] = []

    def request_landing(self, aircraft: Aircraft) -> bool:
        if not self.runway_occupied:
            self.runway_occupied = True
            print(f"ATC: Runway cleared for {aircraft.call_sign} to land.")
            return True
        else:
            print(f"ATC: Runway busy. {aircraft.call_sign} added to landing queue.")
            self.queue.append(aircraft)
            return False

    def request_takeoff(self, aircraft: Aircraft) -> bool:
        if not self.runway_occupied:
            self.runway_occupied = True
            print(f"ATC: Runway cleared for {aircraft.call_sign} to take off.")
            return True
        else:
            print(f"ATC: Runway busy. {aircraft.call_sign} added to takeoff queue.")
            self.queue.append(aircraft)
            return False

    def notify_runway_clear(self, aircraft: Aircraft) -> None:
        self.runway_occupied = False
        print(f"ATC: {aircraft.call_sign} has cleared the runway.")
        if self.queue:
            next_aircraft = self.queue.pop(0)
            print(f"ATC: Notifying {next_aircraft.call_sign} that runway is now clear.")
            # In a real system, this would trigger a callback to the aircraft

# Concrete Colleagues
class Boeing(Aircraft):
    def land(self):
        if self.mediator.request_landing(self):
            print(f"Boeing {self.call_sign}: Landing...")
            self.mediator.notify_runway_clear(self)
        else:
            print(f"Boeing {self.call_sign}: Waiting for landing clearance.")

    def take_off(self):
        if self.mediator.request_takeoff(self):
            print(f"Boeing {self.call_sign}: Taking off...")
            self.mediator.notify_runway_clear(self)
        else:
            print(f"Boeing {self.call_sign}: Waiting for takeoff clearance.")

class Airbus(Aircraft):
    def land(self):
        if self.mediator.request_landing(self):
            print(f"Airbus {self.call_sign}: Landing...")
            self.mediator.notify_runway_clear(self)
        else:
            print(f"Airbus {self.call_sign}: Waiting for landing clearance.")

    def take_off(self):
        if self.mediator.request_takeoff(self):
            print(f"Airbus {self.call_sign}: Taking off...")
            self.mediator.notify_runway_clear(self)
        else:
            print(f"Airbus {self.call_sign}: Waiting for takeoff clearance.")

class PrivateJet(Aircraft):
    def land(self):
        if self.mediator.request_landing(self):
            print(f"PrivateJet {self.call_sign}: Landing...")
            self.mediator.notify_runway_clear(self)
        else:
            print(f"PrivateJet {self.call_sign}: Waiting for landing clearance.")

    def take_off(self):
        if self.mediator.request_takeoff(self):
            print(f"PrivateJet {self.call_sign}: Taking off...")
            self.mediator.notify_runway_clear(self)
        else:
            print(f"PrivateJet {self.call_sign}: Waiting for takeoff clearance.")

# Demonstration
if __name__ == "__main__":
    atc = ATC()
    
    b747 = Boeing("B747-101", atc)
    a320 = Airbus("A320-202", atc)
    pjet = PrivateJet("PJ-303", atc)

    b747.land()
    a320.land()
    pjet.take_off()
