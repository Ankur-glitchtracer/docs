from abc import ABC, abstractmethod

# -----------------------------
# Abstract Base Class for Vehicles
# -----------------------------
class Vehicle(ABC):
    def __init__(self, number_plate):
        self.number_plate = number_plate

    @abstractmethod
    def vehicle_type(self):
        pass


class Car(Vehicle):
    def vehicle_type(self):
        return "Car"


class Bike(Vehicle):
    def vehicle_type(self):
        return "Bike"


# -----------------------------
# Parking Spot
# -----------------------------
class ParkingSpot:
    def __init__(self, spot_id, spot_type):
        self.spot_id = spot_id
        self.spot_type = spot_type  # e.g., "Car" or "Bike"
        self.is_free = True
        self.vehicle = None

    def park_vehicle(self, vehicle):
        if not self.is_free:
            raise Exception("Spot already occupied")
        if vehicle.vehicle_type() != self.spot_type:
            raise Exception("Wrong vehicle type for this spot")
        self.vehicle = vehicle
        self.is_free = False

    def remove_vehicle(self):
        if self.is_free:
            raise Exception("Spot is already empty")
        self.vehicle = None
        self.is_free = True


# -----------------------------
# Parking Lot
# -----------------------------
class ParkingLot:
    def __init__(self, name):
        self.name = name
        self.spots = []

    def add_spot(self, spot):
        self.spots.append(spot)

    def find_free_spot(self, vehicle_type):
        for spot in self.spots:
            if spot.is_free and spot.spot_type == vehicle_type:
                return spot
        return None

    def park_vehicle(self, vehicle):
        spot = self.find_free_spot(vehicle.vehicle_type())
        if not spot:
            print(f"No free spot available for {vehicle.vehicle_type()}")
            return
        spot.park_vehicle(vehicle)
        print(f"{vehicle.vehicle_type()} parked at spot {spot.spot_id}")

    def remove_vehicle(self, number_plate):
        for spot in self.spots:
            if not spot.is_free and spot.vehicle.number_plate == number_plate:
                spot.remove_vehicle()
                print(f"Vehicle {number_plate} removed from spot {spot.spot_id}")
                return
        print("Vehicle not found.")


# -----------------------------
# Demo Usage
# -----------------------------
if __name__ == "__main__":
    lot = ParkingLot("TechPark")

    # Add spots
    lot.add_spot(ParkingSpot(1, "Car"))
    lot.add_spot(ParkingSpot(2, "Car"))
    lot.add_spot(ParkingSpot(3, "Bike"))

    # Vehicles
    car1 = Car("KA-01-HH-1234")
    bike1 = Bike("KA-09-BB-4321")

    lot.park_vehicle(car1)
    lot.park_vehicle(bike1)
    lot.remove_vehicle("KA-01-HH-1234")
