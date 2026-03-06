# OBSERVER DESIGN PATTERN

from collections import defaultdict
from typing import Optional, Protocol


class Subscriber(Protocol):
    def alert(self, msg: Optional[int]):
        ...

    def critical(self, msg: Optional[int]):
        ...


class Siren(Subscriber):
    def alert(self, msg: Optional[int]):
        print(f"The smoke level is {msg}")

    def critical(self, msg: Optional[int]):
        print("Loud Sounding Siren")


class Light(Subscriber):
    def alert(self, msg: Optional[int]):
        print("Yellow lights flashing")

    def critical(self, msg: Optional[int]):
        print("Red lights flashing")


class Phone(Subscriber):
    def alert(self, msg: Optional[int]):
        print(f"Send Alert notification to the user for smoke level reached: {msg}")
    
    def critical(self, msg: Optional[int]):
        print(f"Sent Critical notification to the user for smoke level reached: {msg}")


class EventBus:
    def __init__(self) -> None:
        self._subscribers: dict[str, list[Subscriber]] = defaultdict(list)

    def subscribe(self, topic: str, instance: Subscriber) -> None:
        if instance not in self._subscribers[topic]:
                self._subscribers[topic].append(instance)

    def unsubscribe(self, topic: str, instance: Subscriber) -> None:
        if topic in self._subscribers:
            if instance in self._subscribers[topic]:
                self._subscribers[topic].remove(instance)

    def publish(self, topic: str, msg: int, type: str) -> None:
        if topic in self._subscribers:
            if type == "critical":
                for subscriber in self._subscribers[topic]:
                    subscriber.critical(msg)
            elif type == "alert":
                for subscriber in self._subscribers[topic]:
                    subscriber.alert(msg)


class SmokeSensor:
    def __init__(self, bus: EventBus) -> None:
        self.alertSmokeLevel = 5
        self.criticalSmokeLevel = 10
        self.bus = bus

    def trigger(self, level: int):
        if level >= self.criticalSmokeLevel:
            self.bus.publish(topic="smoke_warning", msg=level, type="critical")
        elif level >= self.alertSmokeLevel:
            self.bus.publish(topic="smoke_warning", msg=level, type="alert")
        else:
            print("Safe Smoke Level")
            print("\n")


bus = EventBus()

sensor = SmokeSensor(bus)

my_siren = Siren()
my_light = Light()
my_phone = Phone()

bus.subscribe(topic="smoke_warning", instance=my_siren)
bus.subscribe(topic="smoke_warning", instance=my_light)

sensor.trigger(3)
sensor.trigger(9)

bus.subscribe(topic="smoke_warning", instance=my_phone)

sensor.trigger(11)
sensor.trigger(6)

bus.unsubscribe(topic="smoke_warning", instance=my_siren)
sensor.trigger(13)
