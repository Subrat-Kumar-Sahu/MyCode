#!/home/cloudera/anaconda3/bin/python

####################################################################################################
# Description: This is a common utility to set logger, read variable value from a config file and
#              set dynamically, read variable value from a config file using configparser.
# 
# History:
#        2019-07-15 : Subrat Kumar       : Created
#        2019-07-21 : Virat Kohli        : Modified the script to add set_custom_logger
####################################################################################################

#sys.path.append('/apps/comm_fn_pkg')

import os
import re
import sys
import logging
import datetime
import configparser as cp

class SetStdAppsEnv():
    def __init__(self, p_conf_file):
        with open(p_conf_file, 'r') as fh:
            for LINE in fh:
                if re.search("(?=^[^'(#|[)'])(?=^[^\s*$])", LINE):
                    exec('self.' + LINE)

def get_std_apps_env(p_conf_file, p_section_name, p_parameter_name):
    parser = cp.ConfigParser()
    parser.read(p_conf_file)
    return parser.get(p_section_name, p_parameter_name)

def set_std_logger(p_log_level, p_log_file):
    logging.basicConfig(
                        level = p_log_level,
                        format = '%(asctime)s:%(filename)s:%(levelname)-8s:%(message)s',
                        datefmt = '%Y-%m-%d %H:%M:%S',
                        handlers = [logging.FileHandler(p_log_file, 'w'), logging.StreamHandler()]
                       )

def set_custom_logger(p_log_level, p_log_path, p_script_name):
    global LOG_FILE

    LOG_FILE = p_log_path \
               + '/' \
               + os.path.splitext(os.path.basename(p_script_name))[0] \
               + '_' + datetime.datetime.now().strftime("%Y%m%d%H%M%S") \
               + '.log'

    logging.basicConfig(
                        level = p_log_level,
                        format = '%(asctime)s:%(filename)s:%(levelname)-8s:%(message)s',
                        datefmt = '%Y-%m-%d %H:%M:%S',
                        handlers = [logging.FileHandler(LOG_FILE, 'w'), logging.StreamHandler()]
                       )
