#!/home/cloudera/anaconda3/bin/python

import logging
import sys

sys.path.append('/apps/comm_fn_pkg')
import comon_utils as cu

def main():
    cu.setLogger(cu.getCommonPath('/apps/conf', 'common_path.txt', 'config_path', 'LOG_DIR'), __file__)

    logging.info('Started')

    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')

    checkLogging()

    logging.info('Finished')

def checkLogging():
    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')

if __name__ == '__main__':
    main()

    logging.info('Log File: ' + cu.LOGFILE)
