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