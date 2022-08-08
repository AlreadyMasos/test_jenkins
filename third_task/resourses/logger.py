import logging
import inspect


def log(lvl=logging.DEBUG):
    log_name = inspect.stack()[1][3]
    logger = logging.getLogger(log_name)
    logger.setLevel(logging.DEBUG)

    hanlder = logging.FileHandler('alog.log', mode='w')
    hanlder.setLevel(lvl)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                  datefmt='%m/%d/%Y %I:%M:%S %p')
    hanlder.setFormatter(formatter)
    logger.addHandler(hanlder)

    return logger

