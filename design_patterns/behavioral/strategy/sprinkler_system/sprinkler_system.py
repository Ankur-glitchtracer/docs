from typing import Optional, Protocol


class IStrategy(Protocol):
    def water(self):
        ...


class EcoStrategy(IStrategy):
    def water(self):
        print("Running in Eco Mode: 10 minutes at 50% power")


class HeatWaveStrategy(IStrategy):
    def water(self):
        print("Running in Booster Mode: 30 minutes at 100% power")


class RainyStrategy(IStrategy):
    def water(self):
        print("Running on Rainy Mode: 0 minutes")


class Sprinkler:
    def __init__(self) -> None:
        self.strategy: Optional[IStrategy] = None

    def set_strategy(self, mode: IStrategy) -> None:
        self.strategy = mode

    def water_the_garden(self):
        if not self.strategy:
            print("No watering strategy set")
            return

        self.strategy.water()



sprinkler= Sprinkler()

sprinkler.water_the_garden()

sprinkler.set_strategy(RainyStrategy())

sprinkler.water_the_garden()

sprinkler.set_strategy(EcoStrategy())

sprinkler.water_the_garden()

