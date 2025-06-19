from __future__ import annotations
from abc import ABC, abstractmethod


# the context class contains a _state that references the concrete state and setState method to change between states.
class Context:

    _state = None

    @property
    def state(self) -> State:
        return self._state

    def __init__(self, state: State) -> None:
        self.set_state(state)

    def set_state(self, state: State):
        # print(f"Context: Transitioning to {type(state).__name__}")
        self._state = state
        self._state.context = self

    def handle(self, cargo=None):
        self._state.handle(cargo)


class State(ABC):
    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context) -> None:
        self._context = context

    @abstractmethod
    def handle(self, cargo) -> None:
        pass