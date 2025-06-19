import pytest
from statemachine import D3FSM, S0State, S1State, S2State
from state_pattern import Context

input1 = "11101"
input2 = "00100"
input3 = "011"

input_empty = ""
input_wrongchar1 = "1201"
input_wrongchar2 = "01 1"


def test_D3FSM_handle():
    m3 = D3FSM()

    assert m3.handle(input1) == 2
    m3.reset()
    assert m3.handle(input2) == 1
    m3.reset()
    assert m3.handle(input3) == 0
    m3.reset()

    assert m3.handle(input_empty) == False
    m3.reset()
    assert m3.handle(input_wrongchar1) == False
    m3.reset()
    assert m3.handle(input_wrongchar2) == False


def test_D3FSM_transition():
    m3 = D3FSM()

    m3._context.state.handle(1)
    assert type(m3._context.state).__name__ == "S1State"
    m3._context.set_state(S0State())
    m3._context.state.handle(0)
    assert type(m3._context.state).__name__ == "S0State"

    m3._context.set_state(S1State())
    m3._context.state.handle(1)
    assert type(m3._context.state).__name__ == "S0State"
    m3._context.set_state(S1State())
    m3._context.state.handle(0)
    assert type(m3._context.state).__name__ == "S2State"

    m3._context.set_state(S2State())
    m3._context.state.handle(1)
    assert type(m3._context.state).__name__ == "S2State"
    m3._context.set_state(S2State())
    m3._context.state.handle(0)
    assert type(m3._context.state).__name__ == "S1State"