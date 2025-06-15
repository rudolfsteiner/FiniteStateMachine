class StateMachine:

    def __init__(self, logger=None):
        self.handlers = {}
        self.startState = None
        self.endStates = []
        self.logger = logger

    def add_state(self, name, handler, end_state=0):
        name = name.upper()
        self.handlers[name] = handler
        if end_state:
            self.endStates.append(name)

    def set_start(self, name):
        self.startState = name.upper()

    def run(self, cargo):
        try:
            handler = self.handlers[self.startState]
        except:
            if self.logger:
                self.logger.error("Must call .set_start() before .run()")
            raise InitializationError("Must call .set_start() before .run()")

        while True:
            (newState, cargo, endcondition) = handler(cargo)

            if (newState.upper() in self.endStates) or endcondition:
                # print("reached ", newState)
                return newState
            else:
                handler = self.handlers[newState.upper()]


class ModThreeFA:
    def __init__(self, logger=None):
        self.logger = logger
        self.alphabet = ["0", "1"]
        self.state_value = {"s0_state": 0, "s1_state": 1, "s2_state": 2}
        self.states = ["s0_state", "s1_state", "s2_state"]
        self.statemachine = StateMachine(logger)
        self.statemachine.add_state("s0_state", s0_transitions)
        self.statemachine.add_state("s1_state", s1_transitions)
        self.statemachine.add_state("s2_state", s2_transitions)
        self.statemachine.set_start("s0_state")

    def run(self, input_string):
        if len(input_string) == 0:
            if self.logger:
                self.logger.error(f"Emptyp Input")
            print(f"Error: Empty Input")
            return False  # Invalid input symbol
        for i in range(len(input_string)):
            if input_string[i] not in self.alphabet:
                if self.logger:
                    self.logger.error(f"input at index {str(i)} is not in alphabet {str(self.alphabet)} list")
                print(
                    f"Error: input -- input_string at index {str(i + 1)} is not in alphabet {str(self.alphabet)} list")
                return False  # Invalid input symbol

        last_state = self.statemachine.run(input_string)

        if last_state not in self.states:
            if self.logger:
                self.logger.error(f"the final state -- {last_state} is not a known state")
            print(f"Error: the final state -- {last_state} is not a known state")

        return self.state_value[last_state]


def s0_transitions(x):
    """
    Input must be of the format of binary value format string
    """
    end_condition = False
    if len(x) == 0:
        return ("s0_state", "", True)

    bit = int(x[0])
    if bit == 1:
        newState = "s1_state"
    elif bit == 0:
        newState = "s0_state"

    if len(x[1:]) == 0:
        end_condition = True

    return (newState, x[1:], end_condition)

def s1_transitions(x):
    end_condition = False
    if len(x) == 0:
        return ("s1_state", "", True)
    bit = int(x[0])
    if bit == 1:
        newState = "s0_state"
    elif bit == 0:
        newState = "s2_state"

    if len(x[1:]) == 0:
        end_condition = True
    return (newState, x[1:], end_condition)

def s2_transitions(x):

    end_condition = False
    if len(x) == 0:
        return ("s2_state", "", True)
    bit = int(x[0])
    if bit == 1:
        newState = "s2_state"
    elif bit == 0:
        newState = "s1_state"

    if len(x[1:]) == 0:
        end_condition = True
    return (newState, x[1:], end_condition)

