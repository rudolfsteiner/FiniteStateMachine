from utils import get_logger
from statemachine import D3FSM, Context, State, S0State, S1State, S2State


def main():
    logger = get_logger()
    m3 = D3FSM(logger=logger)
    while True:
        inputString = input("Enter your input, must be the format of 0/1 string, Enter q to quit:")
        if inputString == "q":
            break

        result = m3.handle(inputString)
        if result is not False:
            print(f"Result: {str(result)}")
        m3.reset()

main()