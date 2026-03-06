from enum import Enum


class Status(Enum):
    MOVING = 1
    IDLE = 0
    STOPPED = -1


class Direction(Enum):
    UP = 1
    DOWN = -1
    NONE = 0


class Door(Enum):
    OPENED = 1
    CLOSED = 0


def _int_input(msg: str, error_msg: str, min_num: int = 1) -> int:
    while True:
        try:
            num = int(input(msg))
            if(num >= min_num):
                return num
            print(f"Enter more than {min_num}")
        except ValueError:
            print(error_msg)
        except KeyboardInterrupt:
            print("\nQuitting")
            exit()


def _int_input_optional(msg: str, error_msg: str, min_num: int = 0, max_num: int = 0) -> int | None:
    while True:
        try:
            inp = input(msg).strip()
            if inp == "":
                return None
            num = int(inp)
            if(num >= min_num and num <= max_num):
                return num
            print(f"Enter more than equal to {min_num} and less than equal to {max_num}")
        except ValueError:
            print(error_msg)
        except KeyboardInterrupt:
            print("\nQuitting")
            exit()


def _direction_input() -> Direction:
    while True:
        dir_input = input("Enter direction (UP/DOWN): ").strip().upper()
        if dir_input == "UP":
            return Direction.UP
        elif dir_input == "DOWN":
            return Direction.DOWN
        print("Invalid direction. Please enter UP or DOWN.")


class Request:
    def __init__(
            self: Request,
            floor: int,
            elevator: Elevator | None,
            direction: Direction = Direction.NONE
        ) -> None:
        self.direction: Direction = direction   
        self.elevator: Elevator | None = elevator
        self.floor: int = floor

    def ext_request(self: Request, direction: Direction, floor: int) -> Request:
        self.direction = direction
        self.floor = floor
        return self

    def assign_request(self: Request, elevator: Elevator, floor: int) -> Request:
        self.direction = Direction.NONE
        self.elevator = elevator
        self.floor = floor
        return self


class Elevator:
    def __init__(self: Elevator, id: int) -> None:
        self.id = id
        self.current_floor = 0
        self.status: Status = Status.IDLE
        self.direction: Direction = Direction.NONE
        self.door: Door = Door.CLOSED
        self.requests: list[Request] = []

    def is_idle(self: Elevator) -> bool:
        return self.status == Status.IDLE

    def move_floor(self: Elevator):
        self.current_floor += self.direction.value

    def _has_request(self: Elevator, floor: int) -> bool:
        return any(req.floor == floor for req in self.requests)

    def add_request(self: Elevator, request: Request) -> None:
        if self._has_request(request.floor):
            return None

        if not self.requests:
            return self.requests.append(request)
        
        len_request = len(self.requests)

        if self.direction == Direction.UP:
            if request.floor == self.current_floor:
                return self.requests.insert(0,request)
            elif request.floor > self.current_floor:
                for i in range(0, len_request):
                    floor = self.requests[i].floor
                    if floor > request.floor or floor < self.current_floor:
                        return self.requests.insert(i,request)
                return self.requests.append(request)
            else:
                for i in range(0, len_request):
                    floor = self.requests[i].floor
                    if floor < request.floor:
                        return self.requests.insert(i,request)
                return self.requests.append(request)
        else:
            if request.floor == self.current_floor:
                return self.requests.insert(0,request)
            elif request.floor > self.current_floor:
                for i in range(0, len_request):
                    floor = self.requests[i].floor
                    if floor > request.floor:
                        return self.requests.insert(i,request)
                return self.requests.append(request)
            else:
                for i in range(0, len_request):
                    floor = self.requests[i].floor
                    if floor < request.floor or self.current_floor < floor:
                        return self.requests.insert(i,request)
                return self.requests.append(request)

    def get_next_request(self: Elevator) -> Request:
        return self.requests[0]

    def step(self: Elevator) -> None:
        if not self.requests:
            self.status = Status.IDLE
            self.direction = Direction.NONE
            return None
        
        target = self.get_next_request().floor

        if self.current_floor == target:
            self.status = Status.STOPPED
            self.direction = Direction.NONE
            self.door = Door.OPENED
            print(f"Elevator {self.id} stopped at floor {target}")
            self.requests.pop(0)

            self.door = Door.CLOSED

        elif self.current_floor < target:
            self.status = Status.MOVING
            self.direction = Direction.UP
            self.move_floor()

        else:
            self.status = Status.MOVING
            self.direction = Direction.DOWN
            self.move_floor()


class ElevatorController:
    def __init__(self) -> None:
        self.elevators: list[Elevator] = self._init_elevator()
        self.ext_requests: list[Request] = []
        self.floors: int = self._init_floors()

    def _init_elevator(self: ElevatorController) -> list[Elevator]:
        elevators: list[Elevator] = []
        msg = "Enter the number of elevators: "
        erro_msg = "Enter a valid Integer!"
        num_elevators = _int_input(msg=msg,error_msg=erro_msg)

        for i in range(0,num_elevators):
            elevators.append(Elevator(i+1))

        return elevators

    def _init_floors(self: ElevatorController) -> int:
        msg = "Enter the number of floors (greater than 2): "
        error_msg = "Enter a valid number of floors!"
        min_floors = 3
        floors = _int_input(msg=msg, error_msg=error_msg, min_num=min_floors)

        return floors

    def assign_request(self: ElevatorController, request: Request) -> None:
        e = None
        for elevator in self.elevators:
            if elevator.is_idle():
                if not e:
                    e = elevator
                elif abs(request.floor - e.current_floor) > abs(request.floor - elevator.current_floor):
                    e = elevator
        if e:
            request.assign_request(elevator=e, floor=request.floor)
            return e.add_request(request=request)

        for elevator in self.elevators:
            if(elevator.direction == request.direction):
                request.assign_request(elevator=elevator, floor=request.floor)
                return elevator.add_request(request=request)

        for elevator in self.elevators:
            if not e:
                e = elevator
            elif abs(request.floor - e.current_floor) < abs(request.floor - elevator.current_floor):
                e = elevator
        if e:
            request.assign_request(elevator=e, floor=request.floor)
            return e.add_request(request=request)


if __name__ == "__main__":
    controller = ElevatorController()

    while True:
        floor = _int_input_optional("Enter floor for external request: ", "Invalid floor!", min_num=0, max_num=controller.floors-1)
        if floor:
            direction = _direction_input()

            # Create external request
            request = Request(floor=floor, elevator=None, direction=direction)

            # Assign it to elevator
            controller.assign_request(request)
        else:
            print("No external request made this turn.")

        # Internal request
        for elevator in controller.elevators:
            floor = _int_input_optional(
                f"Internal request for elevator {elevator.id}: ",
                "Invalid floor!",
                min_num=0,
                max_num=controller.floors-1
            )
            if floor:
                request = Request(floor=floor, elevator=elevator, direction=direction)
                elevator.add_request(request=request)
            else:
                print(f"No internal request made for elevator {elevator.id}")

            if elevator.requests:
                print(f"Floor Queue for elevator {elevator.id} is as follows: ")
                queue = [str(req.floor) for req in elevator.requests]
                print("Floor Queue: [" + ", ".join(queue) + "]")
            else:
                print(f"Elevator {elevator.id} has no pending requests.")

        # Step each elevator
        for elevator in controller.elevators:
            elevator.step()

        # Print state
        for elevator in controller.elevators:
            print(f"[Elevator {elevator.id}] Floor: {elevator.current_floor}, "
                    f"Status: {elevator.status.name}, Direction: {elevator.direction.name}")
