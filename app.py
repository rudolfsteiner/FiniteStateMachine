from utils import get_logger
from statemachine import ModThreeFA

def main():
    logger = get_logger()
    m3 = ModThreeFA()
    while True:
        input_string = input("Enter your input, must be the format of 0/1 string, Enter q to quit:")
        if input_string == "q":
            break
        result = m3.run(input_string)
        if result is not False:
            print(f"Result: {str(result)}")

main()