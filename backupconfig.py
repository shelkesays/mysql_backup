__author__ = 'rahul'

import os
import time
from util import is_non_zero_file


class BackupConfig(object):

    def __init__(self):
        pass

    def getDestination(self, destinationdir=None):
        ''' Getting current datetime to create separate backup folder like "12012013-071334".
        '''
        filestamp = time.strftime('%m-%d-%Y-%H%M%S')
        if destinationdir:
            return os.path.join(destinationdir, filestamp)
        else:
            return filestamp

    def createPath(self, path):
        ''' Check if backup folder already exists or not. If not will create it.
        '''
        if not os.path.exists(path):
            os.makedirs(path)

    def isMultiBackup(self, listfile, default):
        ''' Code for checking if you want to take single backup or assigned multiple backups in list file.
        '''
        multi = False
        print "checking for backup names file."
        if is_non_zero_file(listfile):
            multi = True
            print "List file found..."
            print "Starting backup listed in " + listfile
        else:
            multi = False
            print "List file not found..."
            print "Starting backup of " + default
        return multi