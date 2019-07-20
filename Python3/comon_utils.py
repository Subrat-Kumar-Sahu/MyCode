#!/home/cloudera/anaconda3/bin/python

#sys.path.append('/apps/comm_fn_pkg')

import os
import re
import sys
import logging
import datetime
import configparser as cp


class SetStdAppsEnv():
    def __init__(self, p_path, p_conf_file):

        self.FILENAME = p_path + '/' + p_conf_file

        with open(self.FILENAME, 'r') as fh:
            for LINE in fh:
                if re.search("^[^'(#|[)']", LINE) and LINE.strip():
                    exec('self.' + LINE)

def get_std_apps_env(p_path, p_conf_file, p_section_name, p_section_value):
    FILE_NAME = p_path + '/' + p_conf_file

    parser = cp.ConfigParser()
    parser.read(FILE_NAME)
    return parser.get(p_section_name, p_section_value)

def set_std_logger(p_log_level, p_log_path, p_script_name):
    global LOGFILE

    LOGFILE=p_log_path + '/' + os.path.splitext(os.path.basename(p_script_name))[0] + '_' + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + '.log'

    logging.basicConfig(
                        level = p_log_level,
                        format = '%(asctime)s:%(filename)s:%(levelname)-8s:%(message)s',
                        datefmt = '%Y-%m-%d %H:%M:%S',
                        handlers = [logging.FileHandler(LOGFILE, 'w'), logging.StreamHandler()]
                       )

def set_custom_logger(p_log_level, p_log_path, p_script_name):

    LOGFILE=p_log_path + '/' + os.path.splitext(os.path.basename(p_script_name))[0] + '_' + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + '.log'

    logging.basicConfig(
                        level = p_log_level,
                        format = '%(asctime)s:%(filename)s:%(levelname)-8s:%(message)s',
                        datefmt = '%Y-%m-%d %H:%M:%S',
                        handlers = [logging.FileHandler(LOGFILE, 'w'), logging.StreamHandler()]
                       )
