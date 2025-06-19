from statemachine import Context, State, S0State, S1State, S2State


def test_S0State():
    s0 = S0State()
    s0.context=Context(s0)
    s0.handle(1)
    assert type(s0._context.state).__name__ == "S1State"
    s0.handle(0)
    assert type(s0._context.state).__name__ == "S0State"


def test_S1State():
    s1 = S1State()
    s1.context=Context(s1)
    s1.handle(1)
    assert type(s1._context.state).__name__ == "S0State"
    s1.handle(0)
    assert type(s1._context.state).__name__ == "S2State"


def test_S2State():
    s2 = S2State()
    s2.context=Context(s2)
    s2.handle(1)
    assert type(s2._context.state).__name__ == "S2State"
    s2.handle(0)
    assert type(s2._context.state).__name__ == "S1State"





