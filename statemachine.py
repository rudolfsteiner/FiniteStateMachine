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


class S0State(State):
    def handle(self, cargo):
        if cargo == 1:
            self._context.set_state(S1State())
        elif cargo == 0:
            self._context.set_state(self)
        else:
            raise ValueError(f"Wrong Cargo value: {cargo}, should be 1/0")


class S1State(State):
    def handle(self, cargo):
        if cargo == 1:
            self._context.set_state(S0State())
        elif cargo == 0:
            self._context.set_state(S2State())
        else:
            raise ValueError(f"Wrong Cargo value: {cargo}, should be 1/0")


class S2State(State):
    def handle(self, cargo):
        if cargo == 1:
            self._context.set_state(self)
        elif cargo == 0:
            self._context.set_state(S1State())
        else:
            raise ValueError(f"Wrong Cargo value: {cargo}, should be 1/0")


class FiniteStateMachine:
    _context = None

    def __init__(self, context):
        self._context = context

    def handle(self, cargo):
        pass


class D3FSM(FiniteStateMachine):
    def __init__(self, context=Context(S0State()), logger=None):
        super().__init__(context)
        self.alphabet = ["0", "1"]
        self.stateValue = {"S0State": 0, "S1State": 1, "S2State": 2}
        self.logger = logger

    def handle(self, cargo: str):
        # check empty input
        if len(cargo) == 0:
            if self.logger:
                self.logger.error(f"Empty Input")
            print(f"Error: Empty Input")
            return False  # Invalid input symbol

        # check any non-1/0 char
        for i in range(len(cargo)):
            if cargo[i] not in self.alphabet:
                if self.logger:
                    self.logger.error(f"input at index {str(i)} is not in alphabet {str(self.alphabet)} list")
                print(
                    f"Error: input -- cargo at index {str(i + 1)} is not in alphabet {str(self.alphabet)} list")
                return False  # Invalid input symbol

        for char in cargo:
            self._context.handle(int(char))

        return self.stateValue[type(self._context.state).__name__]


    def reset(self):
        """
        back to the initial stage S0State
        :return:
        """
        self._context.set_state(S0State())

