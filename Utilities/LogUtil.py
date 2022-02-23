import logging
import time
from time import gmtime

class Logger():

    def __init__(self, logger, file_level=logging.INFO):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        fmt = logging.Formatter('%(asctime)s - %(filename)s: [%(lineno)s] - [%(levelname)s] - %(message)s')
        # curr_time = time.strftime("%d-%m-%Y")
        curr_time = time.strftime("%d-%b-%Y %H_%M_%S")
        self.LogFileName = '..\\Logs\\log' + curr_time + '.txt'
        # "a" to append the logs in same file, 'w' to generate new logs and delete old one
        fh = logging.FileHandler(self.LogFileName, mode='a')
        fh.setFormatter(fmt)
        fh.setLevel(file_level)
        self.logger.addHandler(fh)