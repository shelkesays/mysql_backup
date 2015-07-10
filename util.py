__author__ = 'rahul'

import os


def is_non_zero_file(fpath):
    ''' Check if file exist and has content or not
    '''
    return True if os.path.isfile(fpath) and os.path.getsize(fpath) > 0 else False