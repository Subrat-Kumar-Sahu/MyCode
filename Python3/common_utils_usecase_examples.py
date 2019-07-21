#!/home/cloudera/anaconda3/bin/python

import os
import sys
import logging
import datetime

sys.path.append('/apps/comm_fn_pkg')
import common_utils as cu

def main():
    global ENV

    ENV = cu.SetStdAppsEnv('/apps/conf/common_env_var.txt')

    LOG_FILE = ENV.LOG_DIR + '/' + os.path.splitext(os.path.basename(__file__))[0] + '_' + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + '.log'

    cu.set_std_logger(logging.DEBUG, LOG_FILE)

    logging.info('Started')
    logging.info('Log File: ' + LOG_FILE)

    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')

    check_logging()
    check_env_setting()

    logging.info('Finished')

def check_logging():
    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')

def check_env_setting():
    logging.info('IP_DIR: ' + ENV.IP_DIR)
    logging.info('EXECUTOR_MEMORY: ' + ENV.EXECUTOR_MEMORY)
    logging.info('EXECUTOR_MEMORY: ' + cu.get_std_apps_env('/apps/conf/common_env_var.txt', 'spark1_param', 'EXECUTOR_MEMORY').strip('"'))
    

if __name__ == '__main__':
    main()
