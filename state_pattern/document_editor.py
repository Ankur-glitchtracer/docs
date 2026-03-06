# The State pattern is often confused with a simple if/else or switch statement.
# However, it's designed for objects that change their behavior entirely based on their internal state.

# The Scenario: A Document Editor
# Imagine a Document that can be in three states: Draft, Moderation, and Published.

# If Draft: The publish() method moves it to Moderation.
# If Moderation: The publish() method moves it to Published (if the user is an admin).
# If Published: The publish() method does nothing.

# Instead of one giant class with if state == "DRAFT":, you create a State Interface and concrete classes for each state.
# The Document (Context) simply delegates the work to the current state object.

from abc import abstractmethod


class User:
    def __init__(self, is_admin: bool) -> None:
        self.is_admin : bool = is_admin

class State:
    @abstractmethod
    def currentState(self) -> None:
        pass

    @abstractmethod
    def nextState(self, user: User) -> "State":
        pass


class Draft(State):
    def currentState(self) -> None:
        print("Current State is Draft...")

    def nextState(self, user: User) -> State:
        print("Moving from Draft state to Moderation state")
        return Moderation()


class Moderation(State):
    def currentState(self) -> None:
        print("Current State is Moderation...")

    def nextState(self, user: User) -> State:
        if user.is_admin:
            print("User is Admin so publishing it!")
            return Published()
        print("User is not Admin so cannot publish it!")
        return self


class Published(State):
    def currentState(self) -> None:
        print("Current State is Published...")

    def nextState(self, user: User) -> State:
        print("Already Published!")
        return self


class Document:
    def __init__(self, state: State) -> None:
        self.state : State = state

    def publish(self, user: User) -> None:
        self.state = self.state.nextState(user=user)


draft = Draft()
user = User(is_admin=False)
admin_user = User(is_admin=True)

my_document = Document(state=draft)

my_document.state.currentState()
my_document.publish(user=user)
my_document.state.currentState()
my_document.publish(user=user)

my_document.publish(user=admin_user)
my_document.state.currentState()

my_document.publish(user=user)
