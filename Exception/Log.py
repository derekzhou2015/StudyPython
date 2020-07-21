#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test class'
__author__ = 'Kerwin'

import logging
import os.path
import time
# step 1 create logger and set logger level
logger = logging.getLogger()
logger.setLevel(logging.INFO)

#step 2  create handler to write into log files.
rq = time.strftime("%Y%m%d%H%M",time.localtime(time.time()))
log_paht = os.path.dirname(os.getcwd()) + '/exception/logs/'
log_name = log_paht + rq + '.log'
fh = logging.FileHandler(log_name, mode='w')
fh.setLevel(logging.DEBUG)  

formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
fh.setFormatter(formatter)
logger.addHandler(fh)

logger.debug('this is a logger debug message')
logger.info('this is a logger info message')
logger.warning('this is a logger warning message')
logger.error('this is a logger error message')
logger.critical('this is a logger critical message')
print("----------------------------------")
