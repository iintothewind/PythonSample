# coding=UTF-8
import logging
import warnings
import os

warnings.filterwarnings('ignore')

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')
log = logging.getLogger('jira')

base_dir = os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../'))
report_base_dir = os.path.join(base_dir, "report")


def make_dirs(file_name):
    complete_file_name = os.path.join(base_dir, file_name)
    if not os.path.exists(os.path.dirname(complete_file_name)):
        os.makedirs(os.path.dirname(complete_file_name))
    return complete_file_name
