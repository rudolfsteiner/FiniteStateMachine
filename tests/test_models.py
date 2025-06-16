import pytest
from statemachine import ModThreeFA, StateMachine

input1 = "11101"
input2 = "00100"
input3 = "011"

input_empty = ""
input_wrongchar1 = "1201"
input_wrongchar2 = "01 1"


def test_ModThreeFA():
    m3 = ModThreeFA()

    assert m3.run(input1) == 2
    assert m3.run(input2) == 1
    assert m3.run(input3) == 0

    assert m3.run(input_empty) == False
    assert m3.run(input_wrongchar1) == False
    assert m3.run(input_wrongchar2) == False

    assert m3.stateMachine.startState == "S0_STATE"