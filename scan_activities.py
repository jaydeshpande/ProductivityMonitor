import platform
from AppKit import NSWorkspace
import time
import os
from datetime import datetime
import csv

#TODO parent directory is needed when activity tracker starts working over several days
parent_directory = '/Users/JD/Desktop/hobby-codes/ProductivityMonitor'

class activity_scanner:
    scanner_start_time = datetime.today()
    timeLogDir = 'TimeLog'
    storage_folder = str(scanner_start_time.year) + '-' + \
                     str(scanner_start_time.month) + '-' + str(scanner_start_time.day)
    storage_directory = parent_directory + '/' + timeLogDir + '/' + storage_folder
    if (os.path.isdir(storage_directory)) == True:
        os.chdir(storage_directory)
        if (os.path.isfile('timeHistory.csv') == True):
            pass
        else:
            with open('timeHistory.csv', 'a') as csvfile:
                fieldnames = ['Timestamp', 'Application']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
    else:
        os.mkdir(storage_directory)
        os.chdir(storage_directory)

    @staticmethod
    def get_window_title():
        '''
        Function returns window titles
        :return: String - name of the window
        '''
        if (platform.system() == 'Darwin'):
            active_app_name = (NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName'])
            return active_app_name
        else:
            openwindow = None
            # openwindow = win32gui.GetWindowText (w.GetForegroundWindow())
            # TODO developing this on Mac - to be tested on windows separately
            return openwindow

    def update_timelog(self, freq=2):
        '''
        Function to attach time stamps
        :return: Returns updated application directory
        '''
        current_active = self.get_window_title()
        self.update_time_objects(current_active)
        time.sleep(freq)

    def update_time_objects(self, current_active):
        self.save_time_objects(current_active)

    @staticmethod
    def get_time_stamp():
        timestamp = datetime.now()
        return timestamp

    @staticmethod
    def get_time_spent(t1, t2):
        time_spent = t2 - t1
        return time_spent.seconds

    @staticmethod
    def save_time_objects(current_active):
        with open('timeHistory.csv', 'a') as csvfile:
            dtobj = datetime.today()
            timestamp = str(dtobj.month) + '/' + str(dtobj.day) + \
                        '/' + str(dtobj.year) + ':' + str(dtobj.hour)  + '/' \
                        + str(dtobj.minute) + '/' + str(dtobj.second)
            fieldnames = ['timestamp', 'Application']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'timestamp': timestamp, 'Application': current_active})

def run():
    '''
    Function run the activity scanner
    :return: none
    '''
    today = activity_scanner()
    while True:
        today.update_timelog()

if __name__ == "__main__":
    run()