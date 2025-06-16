from statemachine import s0_transitions, s1_transitions, s2_transitions

input_s0_1 = "101"
input_s0_0 = "0"
input_s1_1 = "1"
input_s1_0 = "010"
input_s2_1 = "111"
input_s2_0 = "010"

def test_transitions():
    assert s0_transitions(input_s0_1) == ('s1_state', '01', False)
    assert s0_transitions(input_s0_0) == ('s0_state', '', True)
    assert s1_transitions(input_s1_1) == ('s0_state', '', True)
    assert s1_transitions(input_s1_0) == ('s2_state', '10', False)
    assert s2_transitions(input_s2_1) == ('s2_state', '11', False)
    assert s2_transitions(input_s2_0) == ('s1_state', '10', False)






