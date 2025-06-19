import pytest
from statemachine import D3FSM, S0State, S1State, S2State
from state_pattern import Context


def test_State_setter():
    s0 = S0State()
    c0 = Context(s0)
    s0.context = c0
    assert s0.context == c0


def test_Context_set_state():
    s0 = S0State()
    c0 = Context(s0)
    s0.context = c0
    s2 = S2State()
    s0.context.set_state(s2)
    assert s0.context == c0
    assert s0.context.state == s2