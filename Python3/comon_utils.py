#!/home/cloudera/anaconda3/bin/python

#sys.path.append('/apps/comm_fn_pkg')

import os
import sys
import logging
import datetime
import configparser as cp


def getCommonPath(p_path, p_conf_file, p_section_name, p_section_value):
    FILE_NAME = p_path + '/' + p_conf_file

    parser = cp.ConfigParser()
    parser.read(FILE_NAME)
    return parser.get(p_section_name, p_section_value)

def setLogger(p_log_path, p_script_name):
    global LOGFILE

    LOGFILE=p_log_path + '/' + os.path.splitext(os.path.basename(p_script_name))[0] + '_' + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + '.log'

    logging.basicConfig(
                        level = logging.DEBUG,
                        format = '%(asctime)s:%(filename)s:%(levelname)-8s:%(message)s',
                        datefmt = '%Y-%m-%d %H:%M:%S',
                        handlers = [logging.FileHandler(LOGFILE, 'w'), logging.StreamHandler()]
                       )
