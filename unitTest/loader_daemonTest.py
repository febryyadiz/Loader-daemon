#!/usr/bin/env python
import unittest
import sys
import os

file_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(os.path.dirname(file_dir))

sys.path.append('./loader_daemon')

import loader_daemon as testClass
from unittest import mock
"""
    Constants
"""
name = 'loader_daemon'

"""
    Default Configuration Value
"""
config = {
    'logging':{
        'format':'%(asctime)s %(msecs)d -> %(module)s %(levelname)s : %(message)s',
        'dateformat':'%Y%m%d_%H%M%S',
        'path':'var/log/' + name + '.log',
        'level':'INFO'
    },
    'db':{
        'hostname':'localhost',
        'dbname':'loader_daemon',
        'uname':'root',
        'pwd':''
    }

}

class loader_daemonTesting(unittest.TestCase):
    def setUp(self):
        testClass.logging.info = mock.Mock()
        testClass.datetime = mock.Mock()

        self.data_process = testClass.data_process
        self.thread_function = testClass.thread_function

    def tearDown(self):
        testClass.data_process = self.data_process
        testClass.thread_function = self.thread_function
        
    def data_processTest(self):
        """ Test for data_process function. Case: Positive Case. """
 
        #TODO

    def thread_functionTest(self):
        """ Test for thread_function function. Case: Positive test. """

        #TODO

if __name__ == '__main__':
    unittest.main()
