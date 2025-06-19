from __future__ import annotations
from abc import ABC, abstractmethod
from state_pattern import Context, State


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
    _context = None # handle the state pattern

    def __init__(self, context, alphabet):
        self._context = context
        self._alphabet = alphabet

    @abstractmethod
    def handle(self, cargo):
        pass


class D3FSM(FiniteStateMachine):
    def __init__(self, context=Context(S0State()), alphabet=("0", "1"), logger=None):
        super().__init__(context, alphabet)
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
            if cargo[i] not in self._alphabet:
                if self.logger:
                    self.logger.error(f"input at index {str(i)} is not in alphabet {str(self._alphabet)} list")
                print(
                    f"Error: input -- cargo at index {str(i + 1)} is not in alphabet {str(self._alphabet)} list")
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

