# The Memento Design Pattern is the "Ctrl+Z" of software design. It is used when you need to capture and restore an object's internal state without violating encapsulation (the idea that an object’s internal data should be private).

# The Challenge: The "Pro Pixel" Text Editor
# Imagine you are building a professional text editor. Users are prone to making mistakes, so they need an Undo feature.

# The Problem Statement
# You have a TextEditor class. This editor has:

# Content: A string of text.

# Cursor Position: An integer.

# Selection Range: A pair of integers.

# You need a way to "save" the current state of these three fields and "restore" them later. However, for security and design reasons, no other class should be allowed to see or touch the editor's private state directly.

# The Three Roles You Need to Implement
# To follow the pattern strictly, you must create three distinct entities:

# The Originator (The Editor): * This is the object whose state you want to save.

# It must have a method to create a "snapshot" of itself.

# It must have a method to restore itself using a previous snapshot.

# The Memento (The Snapshot): * A small, immutable object that stores the state of the Originator.

# Crucially, this object should not have "setters." Once created, the state inside it shouldn't change.

# The Caretaker (The History): * This object is responsible for keeping track of the snapshots.

# Think of it as a Stack. When the user types, it pushes a snapshot. When the user hits undo, it pops the last snapshot and gives it back to the editor.

# Things to Watch Out For
# Encapsulation Leak: The Caretaker should never look inside the Memento. It should treat it like a "black box" that it just holds onto. Only the Originator (Editor) should know how to read the Memento.

# Memory Management: If you save a snapshot every time a user types a single character, you’ll run out of memory quickly. Think about when is the "right" time to trigger a save.

# Your Task
# Create your Editor with content, cursor, and selection.

# Create the Memento class to hold those three values.

# Create a History class that manages a list or stack of these Mementos.

# Write a script where you:

# Type "Hello".

# Save.

# Type " World".

# Undo (the editor should go back to "Hello").


from types import MappingProxyType
from typing import Mapping, Optional
from copy import deepcopy

class Memento:
    def __init__(self, state: dict) -> None:
        self._state: MappingProxyType = MappingProxyType(state)

    @property
    def state(self) -> Mapping:
        return self._state.copy()


class History:
    def __init__(self) -> None:
        self.stack: list[Memento] = []
        self.redo_stack: list[Memento] = []

    def save(self, memento: Memento) -> None:
        self.stack.append(memento)
        self.redo_stack = []

    def undo(self, current_memento: Memento) -> Optional[Memento]:
        if not self.stack: return None
        self.redo_stack.append(current_memento)
        return self.stack.pop()

    def redo(self, current_memento: Memento) -> Optional[Memento]:
        if not self.redo_stack: return None
        self.stack.append(current_memento)
        return self.redo_stack.pop()


class Editor:
    def __init__(self, history: History) -> None:
        self.content: str = ""
        self.cursor: int = 0
        self.selection: tuple = (0, 0)
        self.history: History = history

    def type(self, text: str) -> None:
        self.content += text
        print(self.content)

    def create_snapshot(self) -> Memento:
        state = {
            "content": self.content,
            "cursor": self.cursor,
            "selection": self.selection
        }

        return Memento(state)

    def restore(self) -> None:
        state = self.history.undo(self.create_snapshot())
        if state:
            self.__dict__.update(state.state)
            print("Restoring")
            print(self.content)

    def unrestore(self) -> None:
        state = self.history.redo(self.create_snapshot())
        if state:
            self.__dict__.update(state.state)
            print("Redoing")
            print(self.content)

history = History()
editor = Editor(history)

editor.type("Hello")

history.save(editor.create_snapshot())

editor.type(" World")

history.save(editor.create_snapshot())

editor.type("!")

editor.restore()
editor.restore()

editor.unrestore()
editor.unrestore()

# class NHistory:
#     def __init__(self) -> None:
#         self.history: list[Memento] = []
#         self.future: list[Memento] = []

#     def save(self, snapshot: dict[str, Any]) -> None:
#         memento = Memento(snapshot)
#         self.history.append(memento)
#         self.future = []

#     def undo(self) -> Optional[dict[str, Any]]:
#         if self.history != []:
#             self.future.append(self.history[-1])
#             snapshot = self.history.pop().__dict__.copy()
#             snapshot["content"] = snapshot["_Memento__content"]
#             del snapshot["_Memento__content"]
#             snapshot["cursor"] = snapshot["_Memento__cursor"]
#             del snapshot["_Memento__cursor"]
#             snapshot["selection"] = snapshot["_Memento__selection"]
#             del snapshot["_Memento__selection"]
#             return snapshot

#     def redo(self) -> Optional[dict[str, Any]]:
#         if self.future != []:
#             snapshot = self.future.pop().__dict__.copy()
#             snapshot["content"] = snapshot["_Memento__content"]
#             del snapshot["_Memento__content"]
#             snapshot["cursor"] = snapshot["_Memento__cursor"]
#             del snapshot["_Memento__cursor"]
#             snapshot["selection"] = snapshot["_Memento__selection"]
#             del snapshot["_Memento__selection"]
#             return snapshot

# class NEditor:
#     def __init__(self, history: History):
#         self.content: str = ""
#         self.cursor: int = 0
#         self.selection: tuple = (0, 0)
#         self.history: History = history

#     def type(self, text: str) -> None:
#         self.content += text
#         self.history.future = []
#         print(self.content)

#     def create_snapshot(self) -> dict[str, Any]:
#         return self.__dict__.copy()

#     def restore(self, history: Optional[dict[str, Any]]) -> None:
#         if history:
#             self.__dict__.update(history)
#             print("Restoring")
#             print(self.content)

#     def unrestore(self, history: Optional[dict[str, Any]]) -> None:
#         if history:
#             self.__dict__.update(history)
#             print("Redo")
#             print(self.content)

# history = History()
# editor = Editor(history)

# editor.type("Hello")

# history.save(editor.create_snapshot())

# editor.type(" World")

# history.save(editor.create_snapshot())

# editor.type("!")

# editor.restore(history.undo())
# editor.restore(history.undo())

# editor.unrestore(history.redo())
# editor.unrestore(history.redo())