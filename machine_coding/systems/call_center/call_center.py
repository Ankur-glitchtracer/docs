from abc import ABC, abstractmethod
from collections import deque
from enum import Enum
from typing import Optional, Deque, Sequence


class Rank(Enum):
    """Represents the rank hierarchy of an employee in the call center."""
    OPERATOR = 0
    SUPERVISOR = 1
    DIRECTOR = 2


class CallState(Enum):
    """Represents the lifecycle state of a customer call."""
    READY = 0
    IN_PROGRESS = 1
    COMPLETE = 2


class Call:
    """Encapsulates a customer call requiring a minimum employee rank."""

    def __init__(self, rank: Rank) -> None:
        """
        Initializes a Call.

        Args:
            rank (Rank): The minimum rank required to handle this call.
        """
        self.state: CallState = CallState.READY
        self.rank: Rank = rank
        self.employee: Optional['Employee'] = None


class Employee(ABC):
    """Abstract base class representing a generic call center employee."""
    
    def __init__(self, employee_id: str, name: str, rank: Rank, call_center: 'CallCenter') -> None:
        self.employee_id: str = employee_id
        self.name: str = name
        self.rank: Rank = rank
        self.call: Optional[Call] = None
        self.call_center: 'CallCenter' = call_center

    def take_call(self, call: Call) -> None:
        """
        Assigns a call to the employee and updates its state.

        Args:
            call (Call): The call to be handled.
        """
        self.call = call
        self.call.employee = self
        self.call.state = CallState.IN_PROGRESS

    def complete_call(self) -> None:
        """Completes the current call and notifies the call center to free the employee."""
        if self.call:
            self.call.state = CallState.COMPLETE
            self.call_center.notify_call_completed(self.call)
            self.call = None

    @abstractmethod
    def escalate_call(self) -> None:
        """Escalates the current call to a higher-ranking employee tier."""
        pass

    def _escalate_call(self) -> None:
        """Internal helper to reset the call state and trigger the center's escalation protocol."""
        if self.call:
            self.call.state = CallState.READY
            call_to_escalate = self.call
            self.call = None
            self.call_center.notify_call_escalated(call_to_escalate)


class Operator(Employee):
    """Represents an operator (Tier 1) employee."""

    def __init__(self, employee_id: str, name: str, call_center: 'CallCenter') -> None:
        super().__init__(employee_id, name, Rank.OPERATOR, call_center)

    def escalate_call(self) -> None:
        if self.call:
            self.call.rank = Rank.SUPERVISOR
            self._escalate_call()


class Supervisor(Employee):
    """Represents a supervisor (Tier 2) employee."""

    def __init__(self, employee_id: str, name: str, call_center: 'CallCenter') -> None:
        super().__init__(employee_id, name, Rank.SUPERVISOR, call_center)

    def escalate_call(self) -> None:
        if self.call:
            self.call.rank = Rank.DIRECTOR
            self._escalate_call()


class Director(Employee):
    """Represents a director (Tier 3) employee."""

    def __init__(self, employee_id: str, name: str, call_center: 'CallCenter') -> None:
        super().__init__(employee_id, name, Rank.DIRECTOR, call_center)

    def escalate_call(self) -> None:
        raise NotImplementedError("Directors are the highest tier and must handle the call.")


class CallCenter:
    """Orchestrator class that manages employee pools and dispatches incoming calls."""

    def __init__(self, operators: Sequence[Operator], supervisors: Sequence[Supervisor], directors: Sequence[Director]) -> None:
        self.operators: Sequence[Operator] = operators
        self.supervisors: Sequence[Supervisor] = supervisors
        self.directors: Sequence[Director] = directors
        self.queued_calls: Deque[Call] = deque()

    def dispatch_call(self, call: Call) -> None:
        """
        Dispatches a call to an available employee matching or exceeding the required rank.
        Queues the call if no suitable employee is available.

        Args:
            call (Call): The call to be dispatched.
        """
        employee: Optional[Employee] = None
        
        if call.rank == Rank.OPERATOR:
            employee = self._dispatch_to_group(call, self.operators)
            
        if employee is None and call.rank.value <= Rank.SUPERVISOR.value:
            employee = self._dispatch_to_group(call, self.supervisors)
            
        if employee is None and call.rank.value <= Rank.DIRECTOR.value:
            employee = self._dispatch_to_group(call, self.directors)
            
        if employee is None:
            self.queued_calls.append(call)

    def _dispatch_to_group(self, call: Call, employees: Sequence[Employee]) -> Optional[Employee]:
        """Iterates through an employee group to find an available handler."""
        for employee in employees:
            if employee.call is None:
                employee.take_call(call)
                return employee
        return None

    def notify_call_escalated(self, call: Call) -> None:
        """Re-enters an escalated call into the dispatch routing logic."""
        self.dispatch_call(call)

    def notify_call_completed(self, call: Call) -> None:
        """Triggered when an employee finishes a call; pulls the next priority call from the queue."""
        if self.queued_calls:
            next_call = self.queued_calls.popleft()
            self.dispatch_call(next_call)
