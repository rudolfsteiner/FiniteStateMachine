class StateMachine:

    def __init__(self, logger=None):
        self.handlers = {}
        self.startState = None
        self.endStates = []
        self.logger = logger

    def add_state(self, name, handler, end_state=0):
        """
        add state
        :param name: name of the state
        :param handler: transition funtion
        :param end_state: 1 if it is a end state, 0 otherwise
        :return:
        """
        name = name.upper()
        self.handlers[name] = handler
        if end_state:
            self.endStates.append(name)

    def set_start(self, name):
        """
        must call .set_start() before .run()
        :param name: name of the start state
        :return:
        """
        if name.upper() not in self.handlers.keys():
            raise ValueError(f"Please add state {name.upper} before set it as the start state")
        self.startState = name.upper()

    def run(self, cargo):
        """
        Processing input string
        If there is end states, uses end_condition to mark the end state.
        Set the end_condition True if all the char is processed.
        :param cargo: alphabet string input
        :return: name of the end state if successful, else False
        """
        try:
            handler = self.handlers[self.startState]
        except:
            if self.logger:
                self.logger.error("Must call .set_start() before .run()")
            return False

        while True:
            (newState, cargo, endcondition) = handler(cargo)

            if (newState.upper() in self.endStates) or endcondition:
                return newState
            else:
                handler = self.handlers[newState.upper()]


class ModThreeFA:
    def __init__(self, logger=None):
        self.logger = logger
        self.alphabet = ["0", "1"]
        self.stateValue = {"s0_state": 0, "s1_state": 1, "s2_state": 2}
        self.states = ["s0_state", "s1_state", "s2_state"]
        self.stateMachine = StateMachine(logger)
        self.stateMachine.add_state("s0_state", s0_transitions)
        self.stateMachine.add_state("s1_state", s1_transitions)
        self.stateMachine.add_state("s2_state", s2_transitions)
        self.stateMachine.set_start("s0_state")

    def run(self, input_string:str):
        if len(input_string) == 0:
            if self.logger:
                self.logger.error(f"Empty Input")
            print(f"Error: Empty Input")
            return False  # Invalid input symbol
        for i in range(len(input_string)):
            if input_string[i] not in self.alphabet:
                if self.logger:
                    self.logger.error(f"input at index {str(i)} is not in alphabet {str(self.alphabet)} list")
                print(
                    f"Error: input -- input_string at index {str(i + 1)} is not in alphabet {str(self.alphabet)} list")
                return False  # Invalid input symbol

        last_state = self.stateMachine.run(input_string)

        if last_state not in self.states:
            if self.logger:
                self.logger.error(f"the final state -- {last_state} is not a known state")
            print(f"Error: the final state -- {last_state} is not a known state")

        return self.stateValue[last_state]


def s0_transitions(x:str):
    """
    transition for s0 state
    :param x: input string
    :return:
        new state,
        input string for the next transition function
        True if all alphabet processed, thus reach the end state, False otherwise
    """
    end_condition = False
    if len(x) == 0:
        raise ValueError("Empty Input")

    bit = int(x[0])
    if bit == 1:
        new_state = "s1_state"
    else:
        new_state = "s0_state"

    if len(x[1:]) == 0:
        end_condition = True

    return (new_state, x[1:], end_condition)

def s1_transitions(x:str):
    """
    transition for s1 state
    :param x: input string
    :return:
        new state,
        input string for the next transition function
        True if all alphabet processed, thus reach the end state, False otherwise
    """
    end_condition = False
    if len(x) == 0:
        raise ValueError("Empty Input")
    bit = int(x[0])
    if bit == 1:
        new_state = "s0_state"
    else:
        new_state = "s2_state"

    if len(x[1:]) == 0:
        end_condition = True
    return (new_state, x[1:], end_condition)

def s2_transitions(x:str):
    """
    transition for s2 state
    :param x: input string
    :return:
        new state,
        input string for the next transition function
        True if all alphabet processed, thus reach the end state, False otherwise
    """

    end_condition = False
    if len(x) == 0:
        raise ValueError("Empty Input")

    bit = int(x[0])
    if bit == 1:
        new_state = "s2_state"
    else:
        new_state = "s1_state"

    if len(x[1:]) == 0:
        end_condition = True
    return (new_state, x[1:], end_condition)

