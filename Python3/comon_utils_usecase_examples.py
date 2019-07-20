#!/home/cloudera/anaconda3/bin/python

import sys
import logging

sys.path.append('/apps/comm_fn_pkg')
import comon_utils as cu

def main():
    cu.set_std_logger(logging.DEBUG, cu.get_std_apps_env('/apps/conf', 'common_env_var.txt', 'config_path', 'LOG_DIR').strip('"'), __file__)

    logging.info('Started')
    logging.info('Log File: ' + cu.LOG_FILE)

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
    ENV = cu.SetStdAppsEnv('/apps/conf', 'common_env_var.txt')
    logging.info('IP_DIR: ' + ENV.IP_DIR)
    logging.info('EXECUTOR_MEMORY: ' + ENV.EXECUTOR_MEMORY)
    

if __name__ == '__main__':
    main()
