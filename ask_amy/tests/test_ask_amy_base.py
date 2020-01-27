import unittest
import logging
import os
import json


class TestCaseASKAmy(unittest.TestCase):
    """ Base class for Testing ask_amy
    """
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    # Create and environment variable ASK_AMY_LOGGING to specify a logging directory
    path = os.getenv('ASK_AMY_LOGGING_DIR', os.path.expanduser('~')) + os.sep
    hdlr = logging.FileHandler(path + 'logfile.log')
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)

    # Helper functions
    def load_json_file(self, file_name):
        path_to_test_data='../data'
        if not os.path.exists(path_to_test_data):
            # Assume we are running tests from project root
            path_to_test_data = "{}/ask_amy/tests/data".format(os.getcwd())

        file_path = "{}/{}".format(path_to_test_data,file_name)
        file_ptr_r = open(file_path, 'r')
        json_data = json.load(file_ptr_r)
        file_ptr_r.close()
        return json_data
