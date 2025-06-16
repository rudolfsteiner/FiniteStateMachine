import logging


# Create and configure logger
def get_logger():
    logging.basicConfig(filename="fsm.log",
                        format='%(asctime)s %(message)s',
                        filemode='w')

    # Creating an object
    logger = logging.getLogger()

    logger.setLevel(logging.DEBUG)
    return logger
