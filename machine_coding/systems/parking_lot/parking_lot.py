from abc import ABC, abstractmethod
from enum import Enum
from typing import List, Optional


class VehicleSize(Enum):
    """Represents the physical size category of a vehicle or parking spot."""
    MOTORCYCLE = 0
    COMPACT = 1
    LARGE = 2


class Vehicle(ABC):
    """Abstract base class representing a generic vehicle."""

    def __init__(self, vehicle_size: VehicleSize, license_plate: str, required_spots: int) -> None:
        """
        Initializes a Vehicle.

        Args:
            vehicle_size (VehicleSize): The size category of the vehicle.
            license_plate (str): Unique identifier for the vehicle.
            required_spots (int): Number of consecutive spots required to park.
        """
        self.vehicle_size: VehicleSize = vehicle_size
        self.license_plate: str = license_plate
        self.required_spots: int = required_spots
        self.spots_taken: List['ParkingSpot'] = []

    def clear_spots(self) -> None:
        """Frees all spots currently occupied by this vehicle."""
        for spot in self.spots_taken:
            spot.remove_vehicle()
        self.spots_taken.clear()

    def take_spot(self, spot: 'ParkingSpot') -> None:
        """Assigns a parking spot to this vehicle."""
        self.spots_taken.append(spot)

    @abstractmethod
    def can_fit_in_spot(self, spot: 'ParkingSpot') -> bool:
        """Determines if the vehicle physically fits into a specific spot."""
        pass



class Motorcycle(Vehicle):
    """Represents a motorcycle."""

    def __init__(self, license_plate: str) -> None:
        super().__init__(VehicleSize.MOTORCYCLE, license_plate, required_spots=1)

    def can_fit_in_spot(self, spot: 'ParkingSpot') -> bool:
        # Motorcycles can fit in any spot size
        return True


class Car(Vehicle):
    """Represents a compact car."""

    def __init__(self, license_plate: str) -> None:
        super().__init__(VehicleSize.COMPACT, license_plate, required_spots=1)

    def can_fit_in_spot(self, spot: 'ParkingSpot') -> bool:
        # Cars fit in COMPACT or LARGE spots
        return spot.spot_size in (VehicleSize.COMPACT, VehicleSize.LARGE)


class Bus(Vehicle):
    """Represents a large bus requiring multiple consecutive spots."""

    def __init__(self, license_plate: str) -> None:
        super().__init__(VehicleSize.LARGE, license_plate, required_spots=5)

    def can_fit_in_spot(self, spot: 'ParkingSpot') -> bool:
        # Buses only fit in LARGE spots
        return spot.spot_size == VehicleSize.LARGE


class ParkingSpot:
    """Represents an individual parking spot."""

    def __init__(self, level: 'Level', row: int, spot_number: int, spot_size: VehicleSize) -> None:
        """
        Initializes a ParkingSpot.

        Args:
            level (Level): The floor level this spot belongs to.
            row (int): The row identifier.
            spot_number (int): Unique identifier on the level.
            spot_size (VehicleSize): The size capacity of the spot.
        """
        self.level: 'Level' = level
        self.row: int = row
        self.spot_number: int = spot_number
        self.spot_size: VehicleSize = spot_size
        self.vehicle: Optional[Vehicle] = None

    def is_available(self) -> bool:
        """Checks if the spot is currently empty."""
        return self.vehicle is None

    def can_fit_vehicle(self, vehicle: Vehicle) -> bool:
        """Checks if a specific vehicle can park in this spot."""
        if not self.is_available():
            return False
        return vehicle.can_fit_in_spot(self)

    def park_vehicle(self, vehicle: Vehicle) -> bool:
        """Parks a vehicle in this spot."""
        if not self.can_fit_vehicle(vehicle):
            return False
        self.vehicle = vehicle
        vehicle.take_spot(self)
        return True

    def remove_vehicle(self) -> None:
        """Removes the currently parked vehicle, freeing the spot."""
        self.vehicle = None
        self.level.spot_freed()


class Level:
    """Represents a single floor within the parking lot."""

    def __init__(self, floor: int, spots: List[ParkingSpot]) -> None:
        """
        Initializes a Level.

        Args:
            floor (int): The floor number.
            spots (List[ParkingSpot]): The pre-initialized spots on this floor.
        """
        self.floor: int = floor
        self.spots: List[ParkingSpot] = spots
        self.available_spots: int = len(spots)

    def spot_freed(self) -> None:
        """Increments the available spot counter."""
        self.available_spots += 1

    def park_vehicle(self, vehicle: Vehicle) -> bool:
        """
        Attempts to find space and park the vehicle on this level.

        Args:
            vehicle (Vehicle): The vehicle to park.

        Returns:
            bool: True if successfully parked, False otherwise.
        """
        if self.available_spots < vehicle.required_spots:
            return False

        starting_spot_idx = self._find_available_spots(vehicle)
        if starting_spot_idx < 0:
            return False
            
        return self._park_starting_at_spot(starting_spot_idx, vehicle)

    def _find_available_spots(self, vehicle: Vehicle) -> int:
        """Finds an index with enough consecutive spots for the vehicle."""
        consecutive_spots = 0
        for i, spot in enumerate(self.spots):
            if spot.can_fit_vehicle(vehicle):
                consecutive_spots += 1
                if consecutive_spots == vehicle.required_spots:
                    return i - (vehicle.required_spots - 1)
            else:
                consecutive_spots = 0
        return -1

    def _park_starting_at_spot(self, start_idx: int, vehicle: Vehicle) -> bool:
        """Parks the vehicle across the required consecutive spots."""
        for i in range(start_idx, start_idx + vehicle.required_spots):
            self.spots[i].park_vehicle(vehicle)
            self.available_spots -= 1
        return True


class ParkingLot:
    """Orchestrator class managing multiple levels of the parking infrastructure."""

    def __init__(self, levels: List[Level]) -> None:
        """
        Initializes the ParkingLot.

        Args:
            levels (List[Level]): The levels composing the parking lot.
        """
        self.levels: List[Level] = levels

    def park_vehicle(self, vehicle: Vehicle) -> bool:
        """
        Attempts to park a vehicle in the lot by delegating to individual levels.

        Args:
            vehicle (Vehicle): The vehicle needing a spot.

        Returns:
            bool: True if the vehicle was parked successfully.
        """
        for level in self.levels:
            if level.park_vehicle(vehicle):
                print(f"Successfully parked {vehicle.__class__.__name__} [{vehicle.license_plate}] on Level {level.floor}")
                return True
        print(f"Failed to park {vehicle.__class__.__name__} [{vehicle.license_plate}]: Lot is full.")
        return False


# -----------------------------
# Demo Usage
# -----------------------------
if __name__ == "__main__":
    # Create 10 spots for Level 1 (5 Compact, 5 Large)
    level_1_spots = []
    # Create a dummy level reference first to pass into spots
    level_1 = Level(floor=1, spots=[])
    for i in range(5):
        level_1_spots.append(ParkingSpot(level_1, row=1, spot_number=i, spot_size=VehicleSize.COMPACT))
    for i in range(5, 10):
        level_1_spots.append(ParkingSpot(level_1, row=1, spot_number=i, spot_size=VehicleSize.LARGE))
    level_1.spots = level_1_spots
    level_1.available_spots = len(level_1_spots)

    lot = ParkingLot([level_1])

    # Instantiate Vehicles
    moto = Motorcycle("MOTO-123")
    car = Car("CAR-456")
    bus = Bus("BUS-789")

    # Park Vehicles
    lot.park_vehicle(moto)  # Fits anywhere, takes first compact spot
    lot.park_vehicle(car)   # Takes next compact spot
    lot.park_vehicle(bus)   # Scans and takes all 5 Large spots

    # The lot is now mostly full. Try parking another bus
    bus2 = Bus("BUS-999")
    lot.park_vehicle(bus2)  # Will fail

    # Bus leaves, clearing 5 large spots
    bus.clear_spots()
    print("Bus 1 left the lot.")
    
    # Try parking bus 2 again
    lot.park_vehicle(bus2)  # Will now succeed
