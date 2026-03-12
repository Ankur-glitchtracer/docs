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
        self._undo: list[Memento] = []
        self._redo: list[Memento] = []

    def save(self, memento: Memento) -> None:
        self._undo.append(memento)
        self._redo.clear()

    def undo(self, current_memento: Memento) -> Optional[Memento]:
        memento = self._undo.pop() if self._undo else None
        if memento:
            self._redo.append(current_memento)

        return memento

    def redo(self, current_memento: Memento) -> Optional[Memento]:
        memento = self._redo.pop() if self._redo else None
        if memento:
            self._undo.append(current_memento)

        return memento


class Editor:
    def __init__(self, history: History) -> None:
        self.content: str = ""
        self.cursor: int = 0
        self.selection: tuple = (0, 0)
        self.history: History = history

    def _restore_from(self, memento: Memento) -> None:
        self.content = memento.state["content"]
        self.cursor = memento.state["cursor"]
        self.selection = memento.state["selection"]

    def begin_edit(self) -> None:
        self.history.save(self.create_snapshot())

    def type(self, text: str) -> None:
        start, end = self.selection
        if start != end:
            self.content = self.content[:start] + text + self.content[end:]
            self.cursor = start + len(text)

        else:
            self.content = self.content[:self.cursor] + text + self.content[self.cursor:]
            self.cursor = self.cursor + len(text)

        self.selection = (self.cursor, self.cursor)

        print(self.content)

    def create_snapshot(self) -> Memento:
        state = {
            "content": self.content,
            "cursor": self.cursor,
            "selection": self.selection
        }

        return Memento(state)

    def restore(self) -> None:
        memento = self.history.undo(current_memento=self.create_snapshot())
        if memento:
            self._restore_from(memento=memento)
            print("Restoring")
            print(self.content)

    def unrestore(self) -> None:
        memento = self.history.redo(current_memento=self.create_snapshot())
        if memento:
            self._restore_from(memento=memento)
            print("Redoing")
            print(self.content)


history = History()
editor = Editor(history)


editor.begin_edit()

editor.type("Hello")

editor.type(" World")
editor.cursor = 5
editor.type("X")
