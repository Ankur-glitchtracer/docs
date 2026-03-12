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


class SubscriberList:
    def __init__(self) -> None:
        self.subs: list[Subscriber] = []
    def getSubscriber(self) -> list[Subscriber]:
        return self.subs
    def addSubscriber(self, subscriber: Subscriber) -> None:
        if subscriber not in self.subs:
            self.subs.append(subscriber)
    def deleteSubscriber(self, subscriber: Subscriber) -> None:
        if subscriber in self.subs:
            self.subs.remove(subscriber)
    def alertSignal(self, level: int):
        for subcriber in self.subs:
            subcriber.alert(msg=level)
    def criticalSignal(self, level: int):
        for subcriber in self.subs:
            subcriber.critical(msg=level)


class SmokeSensor:
    def __init__(self) -> None:
        self.alertSmokeLevel = 5
        self.criticalSmokeLevel = 10
        self.subsList = SubscriberList()
    def addSubscriber(self, subscriber: Subscriber) -> None:
        self.subsList.addSubscriber(subscriber)
    def removeSubscriber(self, subscriber: Subscriber) -> None:
        self.subsList.deleteSubscriber(subscriber)
    def trigger(self, level: int):
        if level >= self.criticalSmokeLevel:
            self.subsList.criticalSignal(level)
        elif level >= self.alertSmokeLevel:
            self.subsList.alertSignal(level)
        else:
            print("Safe Smoke Level")
            print("\n")


sensor = SmokeSensor()
sensor.addSubscriber(Siren())
sensor.addSubscriber(Light())

sensor.trigger(3)
sensor.trigger(9)

sensor.addSubscriber(Phone())
sensor.trigger(11)
sensor.trigger(6)

sensor.removeSubscriber(Siren())
sensor.trigger(13)